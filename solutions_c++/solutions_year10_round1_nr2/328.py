#include<iostream>
#include<string.h>
#include<algorithm>
#include<cmath>
using namespace std;
int a[101];
int dp[101][257];
int b[101];
int MINCOST;
int calc(int x,int y,int z)
{
    if (x==y) return 0;
    if (z==0) return -1;
    return ((abs(x-y)-1)/z);
}
int main()
{
    int cas,i,j,k,d,I,n,m;
    int tcas=0;
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&cas);
    while (cas--)
    {
       scanf("%d%d%d%d",&d,&I,&m,&n);
       for (i=1;i<=n;i++)
       scanf("%d",&a[i]);
       memset(dp,0x1f,sizeof(dp));
       for (i=0;i<256;i++)
       dp[0][i]=0;
       for (i=1;i<=n;i++)
       {
          
           for (j=0;j<256;j++)
           { dp[i][j]=dp[i-1][j]+d;
               for (k=0;k<256;k++)
               if (abs(j-k)<=m)
               dp[i][j]=min(dp[i][j],dp[i-1][k]+abs(j-a[i]));
           }
           for (k=0;k<256;k++)
           {
               if (abs(a[i]-k)>m&&m!=0)
               dp[i][a[i]]=min(dp[i][a[i]],calc(a[i],k,m)*I+dp[i-1][k]);
           }
       }
       int MIN=999999999;
       for (i=0;i<256;i++)
       MIN=min(MIN,dp[n][i]);
       printf("Case #%d: %d\n",++tcas,MIN);
    }
}
          
