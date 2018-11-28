#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define MAXN 12
#define MAXM 2048
using namespace std;

long long dp[MAXM+1][MAXN+1][MAXN+1];
int pr[MAXN+1][MAXM+1];
int mm[MAXM+1];
int n,m;

long long solve(int x,int p,int c)
{
    if(dp[x][p][c]!=-1)
    {
        return dp[x][p][c];
    }
    if(p==0)
    {
        if(c>=mm[x])
        {
            dp[x][p][c]=0;
        }
        else
        {
            dp[x][p][c]=1000000000000000000LL;
        }
        return dp[x][p][c];
    }
    dp[x][p][c]=1000000000000000000LL;
    dp[x][p][c]=min(dp[x][p][c],solve((x<<1)-1,p-1,c+1)+solve(x<<1,p-1,c+1)+pr[p][x]);
    dp[x][p][c]=min(dp[x][p][c],solve((x<<1)-1,p-1,c)+solve(x<<1,p-1,c));
    return dp[x][p][c];
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,c,t;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d",&n);
        m=1<<n;
        for(i=1;i<=m;i++)
        {
            scanf("%d",&mm[i]);
            mm[i]=n-mm[i];
        }
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=1<<(n-i);j++)
            {
                scanf("%d",&pr[i][j]);
            }
        }
        memset(dp,-1,sizeof(dp));
        printf("Case #%d: %I64d\n",c+1,solve(1,n,0));
    }
    return 0;
}
