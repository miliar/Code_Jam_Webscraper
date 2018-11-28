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

#define MOD 1000000007
vector<int> signs;

vector<map<int,int> > dp;

//int dp[105][500010];
int n;

int solve(int val, int id)
   {
      if(dp[id][val]>0)return dp[id][val];
      int ret=1;
      
      
      
      for(int i=id+1;i<n;i++)
         {
            if(val<signs[i])
               {
                  ret+=solve(signs[i],i);
                  ret%=MOD;
               }
               
         }
      return dp[id][val]=ret;
   }

int main()
{
   int NC;
   cin>>NC;
   
   
   for(int ic=0;ic<NC;ic++)
      {
         //   memset(dp,-1,sizeof(dp));
         signs.clear();
         long long m,X,Y,Z;
         cin>>n>>m>>X>>Y>>Z;
         vector<int> a;
         
         vector<map<int,int> > td(n+1);
         
         dp=td;
         
         REP(i,m)
            {
               int temp;
               cin>>temp;
               a.push_back(temp);
            }
         
         
         REP(i,n)
            {
               signs.push_back(a[i%m]);
               //    cout<<a[i%m]<<" ";
               a[i%m]=(X*a[i%m]+Y*(i+1))%Z;
            }
         int res=0;
         for(int i = n-1;i>=0;i--)
            {
               res+=solve(signs[i],i);
               res%=MOD;
            }
         cout<<"Case #"<<(ic+1)<<": "<<res<<endl;
      }
   return 0;
}
