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

int tr[10010];
int lv;
int dp[10010][2];
bool ok[10010];

int solve(int id, int val)
   {
      int &ret=dp[id][val];
      if(ret>-1)return ret;
      
      ret=20000;
      //cout<<"asdf"<<ok[id]<<endl;
      //cout<<id;
      //cout<<tr[id];
      if(id>=lv)
         {
            if(tr[id]==val)ret=0;
         }
      else
         {
            if(tr[id]==1)
               {
                  if(val==0)
                     {
                        ret=min(ret,solve(id*2+1,0)+solve(id*2+2,1));
                        ret=min(ret,solve(id*2+1,1)+solve(id*2+2,0));
                        ret=min(ret,solve(id*2+1,0)+solve(id*2+2,0));
                        if(ok[id])ret=min(ret,1+solve(id*2+1,0)+solve(id*2+2,0));
                     }
                  if(val==1)
                     {
                        ret=min(ret,solve(id*2+1,1)+solve(id*2+2,1));
                        if(ok[id])ret=min(ret,1+solve(id*2+1,0)+solve(id*2+2,1));
                        if(ok[id])ret=min(ret,1+solve(id*2+1,1)+solve(id*2+2,0));
                        if(ok[id])ret=min(ret,1+solve(id*2+1,1)+solve(id*2+2,1));
                     }
               }
            if(tr[id]==0)
               {
                  if(val==0)
                     {
                        ret=min(ret,solve(id*2+1,0)+solve(id*2+2,0));
                        if(ok[id])ret=min(ret,1+solve(id*2+1,1)+solve(id*2+2,0));
                        if(ok[id])ret=min(ret,1+solve(id*2+1,0)+solve(id*2+2,1));
                     }
                  if(val==1)
                     {
                        if(ok[id])ret=min(ret,1+solve(id*2+1,1)+solve(id*2+2,1));
                        ret=min(ret,solve(id*2+1,0)+solve(id*2+2,1));
                        ret=min(ret,solve(id*2+1,1)+solve(id*2+2,0));
                        ret=min(ret,solve(id*2+1,1)+solve(id*2+2,1));
                     }
               }
            
         }
      //cout<<id<<" "<<val<<" "<<ret<<endl;
      return ret;
   }

int main()
{
   int NC;
   cin>>NC;
   for(int ic=0;ic<NC;ic++)
      {
         int m;
         cin>>m;
         //tr.clear();
         int goal;
         cin>>goal;
         memset(dp,-1,sizeof(dp));
         int tmp,g;
          lv=(m-1)/2;
          // cout<<lv;
          int i;
             for(i=0;i<((m-1)/2);i++)
            {
               cin>>tmp;
               cin>>g;
               tr[i]=tmp;
               ok[i]=(g==1);
            }
          for(;i<m;i++)
             {
                 cin>>tmp;
                 tr[i]=tmp;
             }
          // cout<<i;
         int res=solve(0,goal);
         if(res>=20000)
            {
               cout<<"Case #"<<(ic+1)<<": IMPOSSIBLE"<<endl;
            }
         else cout<<"Case #"<<(ic+1)<<": "<<res<<endl;
      }
   return 0;
}
