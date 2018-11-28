#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXQ = 1000,MAXS=100,INF=1000000;
string line;//[1000];
string searchEngines[MAXS+10];
string queryString[MAXQ+10];
int dp[MAXQ+10][MAXS+10],isok[MAXQ+10][MAXS+10];

int toInt(string str)
{
   istringstream iss(str);
   int val;iss>>val;
   return val;   
}

int solve(int S, int Q)
{
   if(Q==0) return 0;
    memset(isok,0,sizeof(isok));
   
    for(int i=0;i<Q;i++) for(int j=0;j<S;j++)  dp[i][j]=INF;

    for(int i=0;i<Q;i++) {
      for(int j=0;j<S;j++) {
         if(queryString[i]==searchEngines[j])continue;
         isok[i][j]=1;
      }
    }
    
    for(int i=0;i<S;i++) if(isok[0][i])dp[0][i]=0;

    int ret=INF;    
    
    for(int i=1;i<Q;i++) {
         for(int cur=0;cur<S;cur++) {
            if(!isok[i][cur])continue;
            dp[i][cur]=dp[i-1][cur];
            for(int prev=0;prev<S;prev++) {
               dp[i][cur]=min(dp[i][cur],dp[i-1][prev]+1);  
            }
         }
    }
   
    for(int i=0;i<S;i++) {
      if(isok[Q-1][i]) ret=min(ret,dp[Q-1][i]);
    } 
    
    
    return ret;
    
}

int main()
{
   freopen("A-large.in","r",stdin);
   freopen("test2.out","w",stdout);
   int tc,caseCount=1;
   cin>>tc;cin.ignore();
   
   while(tc--) {
      int S;
      cin>>S;cin.ignore();
      for(int i=0;i<S;i++) {
         getline(cin,line);
         searchEngines[i]=line;
      }
      int Q;
      cin>>Q;cin.ignore();
      for(int i=0;i<Q;i++) {
         getline(cin,line);
         queryString[i]=line;
         
      }
      cout<<"Case #"<<caseCount++<<": "<<solve(S,Q)<<endl;
      
   }
   return 0;
}
