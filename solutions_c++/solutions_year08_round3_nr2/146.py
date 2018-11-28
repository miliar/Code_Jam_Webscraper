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

#define llong long long 

string s;
int gg;
int n;
llong res;

bool check(llong a)
   {
      if(a%7==0 || a%5==0 || a%3==0 || a%2==0 || a==0)return true;
      else return false;
   }
void rec(int from, int to)
   {
      llong num;
      sscanf(s.substr(from,to-from+1).c_str(),"%lld",&num);
      
      if(to==n-1)
         {
            res+=num;
            if(check(res))gg++;
            res-=num;
            if(from>0)
               {
                  res-=num;
                  if(check(res))gg++;
                  res+=num;
               }   
            return;
         }
     
      res+=num;
      rec(to+1,to+1);
      res-=num;
      if(from>0)
         {
            res-=num;
            rec(to+1,to+1);
            res+=num;
         }
      
      rec(from,to+1);
       
                            
   }

int main()
{
   int NC;
   cin>>NC;
   for(int ic=0;ic<NC;ic++)
      {
         gg=0;
         res=0;
         cin>>s;
         n=s.size();
         rec(0,0);
         cout<<"Case #"<<(ic+1)<<": "<<gg<<endl;
      }
   return 0;
}
