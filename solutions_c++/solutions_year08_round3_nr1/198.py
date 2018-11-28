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

int main()
{
   int NC;
   cin>>NC;
   for(int ic=0;ic<NC;ic++)
      {
         int P,K,L;
         cin>>P;
         cin>>K;
         cin>>L;
         vector<int> fr;
         REP(i,L){
            int temp;
            cin>>temp;
            fr.push_back(temp);
         }
         sort(fr.rbegin(),fr.rend());
         
         int ans=0;
         REP(j,SZ(fr))
            {
               ans+=fr[j]*(j/K+1);
               //cout<<ans<<endl;
            }

         cout<<"Case #"<<(ic+1)<<": "<<ans<<endl;
      }
   return 0;
}
