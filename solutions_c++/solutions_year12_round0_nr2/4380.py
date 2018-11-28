#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
int dp[110][110];
int A[110];
int N,S,P;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("kengdiea_LB.out","w",stdout);
    int i,j,k,T,tt=0;

    scanf("%d",&T);
    while(T--)
    {
        tt++;
        scanf("%d%d%d",&N,&S,&P);
        for(i=1;i<=N;i++) scanf("%d",&A[i]);
        memset(dp,0,sizeof(dp));
        for(i=1;i<=N;i++)
        {
            if((A[i]+2)/3>=P) dp[i][0]=dp[i-1][0]+1;
            else dp[i][0]=dp[i-1][0];
            for(j=1;j<=S;j++)
            {
                if((A[i]+2)/3>=P) dp[i][j]=dp[i-1][j]+1;
                else dp[i][j]=dp[i-1][j];
                if(A[i]==0)
                {
                    if(P>0) dp[i][j]=max(dp[i][j],dp[i-1][j-1]);
                    else dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1);
                }
                else if(A[i]%3==0)
                {
                    if(A[i]/3+1>=P) dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1);
                    else dp[i][j]=max(dp[i][j],dp[i-1][j-1]);
                }
                else if(A[i]%3==1)
                {
                    if(A[i]/3+1>=P) dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1);
                    else dp[i][j]=max(dp[i][j],dp[i-1][j-1]);
                }
                else
                {
                    if(A[i]/3+2>=P) dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1);
                    else dp[i][j]=max(dp[i][j],dp[i-1][j-1]);
                }
            }
        }printf("Case #%d: %d\n",tt,dp[N][S]);
    }
    return 0;
}
