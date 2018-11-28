#include<iostream>
using namespace std;
const int maxm=12;
const int maxn=1<<maxm;
int dp[maxn][maxm],a[maxn],c[maxn],m,n,cases,tt;
int infi=1<<29;
void init()
{
     scanf("%d",&m);
     n=(1<<m)-1;
     int i,x,y,j;
     for (i=0;i<(1<<(m-1));i++)
     {
         scanf("%d%d",&x,&y);
         a[i]=m-min(x,y);
     }  
     for (i=m-1;i>=0;i--)
     {
         for (j=0;j<(1<<i);j++)
         scanf("%d",&c[(1<<i)+j]);
     }
     for (i=1;i<=n;i++)
         for (j=0;j<=m;j++) dp[i][j]=infi;
}

void dfs(int x)
{
     int i;
     if (x*2<=n)
     {
        dfs(x*2);
        dfs(x*2+1);
        for (i=0;i<=m;i++)
        {
            dp[x][i]<?=dp[x*2][i]+dp[x*2+1][i];
            if (i<m)
            dp[x][i]<?=dp[x*2][i+1]+dp[x*2+1][i+1]+c[x];
        }
     }
     else
     {
         for (i=a[x-(1<<(m-1))];i<=m;i++) dp[x][i]=0;
         dp[x][a[x-(1<<(m-1))]-1]=c[x];
     }
}

void print()
{
     printf("Case #%d: %d\n",tt+1,dp[1][0]);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        init();
        dfs(1);
        print();
    }
    return 0;
}
