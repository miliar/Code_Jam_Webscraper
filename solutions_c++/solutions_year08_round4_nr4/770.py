#include <algorithm>
#include <list>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
 
using namespace std;
 
#define REP(a,b) for(int a=0;(int)a<(b);++a)
#define TR(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();a++) 
#define SZ(a) (int)a.size()
#define ALL(a) (a).begin(),(a).end()   

int perm[20];

int main()
{
   int NC;
   cin>>NC;
   for(int ic=0;ic<NC;ic++)
      {
         int k;
         string t;
         cin>>k>>t;
         int n = (int)t.size();
         string a(n,'a');
         
         int res=n+1;
         int tres;
         REP(i,k)
            {
               perm[i]=i+1;
            }
         
         sort(perm,perm+k);
         
         do
            {
               REP(i,n/k)
                  {
                     REP(j,k)
                        {
                           a[i*k+j]=t[i*k+perm[j]-1];
                        }
                  }
               
               char g='-';
               tres=0;
               REP(i,n)
                  {
                     if(a[i]!=g)
                        {
                           g=a[i];
                           tres++;
                        }
                  }
               res=min(res,tres);
            }while(next_permutation(perm,perm+k));
         
         cout<<"Case #"<<(ic+1)<<": "<<res<<endl;
      }
   return 0;
}
