#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
string CJ="welcome to code jam";

int dp[501][20];
string S;
int solve(int start,int from)
{
    int &ans=dp[start][from];
    if(ans!=-1) return ans;
    if(from==19) return ans=1; 
    if(start==S.size()) return ans=0;
    
    ans=0;
    if(S[start]==CJ[from])
       ans=ans+solve(start+1,from+1)%10000;
    ans=ans+solve(start+1,from);
    ans=ans%10000;
    return ans;
}
    
    
int main()
{
    freopen("WCJ.in","r",stdin);
    freopen("WCJ.out","w",stdout);
    int T;
    cin>>T;
    int K=T;
    getchar();
    while(T--)
    {
              
              memset(dp,-1,sizeof(dp));
              getline(cin,S);
              int L=S.length();
              int ans=0;
              ans=solve(0,0)%10000;
              printf("Case #%d: %.4d\n",K-T,ans);
    }
    
         
}
                      
              
              
