#include <cstdio>
#include <iostream>
#include <memory>
#include <algorithm>
#define MAXM 10000
using namespace std;

int dp[MAXM+1][2];
int g[MAXM+1],c[MAXM+1];
int m,v,x,y;

void DFS(int u,int k)
{
    int i,j;
    if((u<<1)>=m)
    {
        dp[u][g[u]]=0;
        dp[u][g[u]^1]=100000000;
        return;
    }
    dp[u][0]=100000000;
    dp[u][1]=100000000;
    if(g[u]==1)
    {
        for(i=0;i<=1;i++)
        {
            for(j=0;j<=1;j++)
            {
                if(dp[u<<1][i]==-1)
                {
                    DFS(u<<1,i);
                }
                if(dp[(u<<1)+1][j]==-1)
                {
                    DFS((u<<1)+1,j);
                }
                if((dp[u<<1][i]!=100000000)&&(dp[(u<<1)+1][j]!=100000000))
                {
                    dp[u][i&j]=min(dp[u][i&j],dp[u<<1][i]+dp[(u<<1)+1][j]);
                }
            }
        }
        if(c[u]==1)
        {
            for(i=0;i<=1;i++)
            {
                for(j=0;j<=1;j++)
                {
                    if(dp[u<<1][i]==-1)
                    {
                        DFS(u<<1,i);
                    }
                    if(dp[(u<<1)+1][j]==-1)
                    {
                        DFS((u<<1)+1,j);
                    }
                    if((dp[u<<1][i]!=100000000)&&(dp[(u<<1)+1][j]!=100000000))
                    {
                        dp[u][i|j]=min(dp[u][i|j],dp[u<<1][i]+dp[(u<<1)+1][j]+1);
                    }
                }
            }
        }
    }
    else
    {
        for(i=0;i<=1;i++)
        {
            for(j=0;j<=1;j++)
            {
                if(dp[u<<1][i]==-1)
                {
                    DFS(u<<1,i);
                }
                if(dp[(u<<1)+1][j]==-1)
                {
                    DFS((u<<1)+1,j);
                }
                if((dp[u<<1][i]!=100000000)&&(dp[(u<<1)+1][j]!=100000000))
                {
                    dp[u][i|j]=min(dp[u][i|j],dp[u<<1][i]+dp[(u<<1)+1][j]);
                }
            }
        }
        if(c[u]==1)
        {
            for(i=0;i<=1;i++)
            {
                for(j=0;j<=1;j++)
                {
                    if(dp[u<<1][i]==-1)
                    {
                        DFS(u<<1,i);
                    }
                    if(dp[(u<<1)+1][j]==-1)
                    {
                        DFS((u<<1)+1,j);
                    }
                    if((dp[u<<1][i]!=100000000)&&(dp[(u<<1)+1][j]!=100000000))
                    {
                        dp[u][i&j]=min(dp[u][i&j],dp[u<<1][i]+dp[(u<<1)+1][j]+1);
                    }
                }
            }
        }
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,k,t;
    scanf("%d",&t);
    for(k=0;k<t;k++)
    {
        memset(dp,-1,sizeof(dp));
        scanf("%d %d",&m,&v);
        x=(m-1)>>1;
        for(i=1;i<=x;i++)
        {
            scanf("%d %d",&g[i],&c[i]);
        }
        y=(m+1)>>1;
        for(i=y;i<=m;i++)
        {
            scanf("%d",&g[i]);
        }
        DFS(1,v);
        printf("Case #%d: ",k+1);
        if(dp[1][v]<100000000)
        {
            printf("%d\n",dp[1][v]);
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
