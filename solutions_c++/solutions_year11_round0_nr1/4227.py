#include <stdio.h>
#include <string.h>
#define maxn 110
#define inf 1<<30
bool flag[maxn];
int pos[maxn],dp[maxn][maxn][maxn];
int min(int a,int b)
{
    return (a<b) ? a:b;
}
int max(int a,int b)
{
    return (a>b) ? a:b;
}
int abs(int a)
{
    return (a>0)  ?a:-a;
}
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("a.out","w",stdout);
    int casee,n;
    scanf("%d",&casee);
    for(int tt=1;tt<=casee;tt++)
    {
        int ans=inf;
        scanf("%d",&n);
        char tmp[2];
        for(int i=0;i<n;i++)
        {
            scanf("%s",tmp);
            if(tmp[0]=='O') flag[i]=0;
            else flag[i]=1;
            scanf("%d",&pos[i]);
        }
        for(int i=0;i<=n;i++)
        {
            for(int j=1;j<=100;j++)
            {
                for(int k=1;k<=100;k++)
                dp[i][j][k]=inf;
            }
        }
        dp[0][1][1]=0;
        for(int i=1;i<=100;i++)
        {
            for(int j=1;j<=100;j++)
            {
                dp[0][i][j]=(i>j)?(i-1):(j-1);
            }
        }
        for(int k=0;k<n;k++)
        {
            if(flag[k]==0)
            {
                for(int j=1;j<=100;j++)
                {
                    dp[k+1][pos[k]][j]=min(dp[k+1][pos[k]][j],dp[k][pos[k]][j]+1);
                    if(j-1>0)  dp[k+1][pos[k]][j]=min(dp[k+1][pos[k]][j],dp[k][pos[k]][j-1]+1);
                    if(j+1<101)dp[k+1][pos[k]][j]=min(dp[k+1][pos[k]][j],dp[k][pos[k]][j+1]+1);
                    for(int ii=1;ii<=100;ii++)
                    {
                        for(int jj=1;jj<=100;jj++)
                        {
                            dp[k+1][ii][jj]=min(dp[k+1][ii][jj],dp[k+1][pos[k]][j]+max(abs(ii-pos[k]),abs(jj-j)));
                        }
                    }
                }
            }
            else
            {
                for(int i=1;i<=100;i++)
                {
                    dp[k+1][i][pos[k]]=min(dp[k+1][i][pos[k]],dp[k][i][pos[k]]+1);
                    if(i-1>0)  dp[k+1][i][pos[k]]=min(dp[k+1][i][pos[k]],dp[k][i-1][pos[k]]+1);
                    if(i+1<101)dp[k+1][i][pos[k]]=min(dp[k+1][i][pos[k]],dp[k][i+1][pos[k]]+1);
                    for(int ii=1;ii<=100;ii++)
                    {
                        for(int jj=1;jj<=100;jj++)
                        {
                            dp[k+1][ii][jj]=min(dp[k+1][ii][jj],dp[k+1][i][pos[k]]+max(abs(ii-i),abs(jj-pos[k])));
                        }
                    }
                }
            }
        }
        for(int i=1;i<=100;i++)
        {
            for(int j=1;j<=100;j++)
            {
                ans=min(ans,dp[n][i][j]);
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
