#include<stdio.h>
#include<string.h>
#include<math.h>
#define INF (1<<28)
int a[201];
int abs(int x)
{
    return (x>0)?x:-x;
}
int min(int a,int b)
{
    return (a<b)?a:b;
}
int f[101][300];
int main()
{
    int index,t,d,ins,m,n;
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d",&t);
    for (index=1;index<=t;index++)
    {
        scanf("%d%d%d%d",&d,&ins,&m,&n);
        for (int i=1;i<=n;i++)
            scanf("%d",a+i);
        for (int j=0;j<=255;j++)
                f[1][j]=abs(j - a[1]);
        for (int i=2;i<=n;i++)
            for (int j=0;j<=255;j++)
            {
                f[i][j]=INF;
                for (int k=0;k<=255;k++)
                {
                    if (j==k) f[i][j]=min(f[i][j],f[i-1][k]+d);
                    int dis=abs(j-k);
                    int cost=abs(j-a[i]);
                    if (dis<=m)
                        f[i][j]=min(f[i][j],f[i-1][k]+cost);
                    else
                        if (m) f[i][j]=min(f[i][j],
                                           f[i-1][k]+cost+(ceil((dis+0.0)/m)-1)*ins);
                    
                }
            }
        printf("Case #%d: ",index);
        int ans=INF;
        for(int i=0;i<=255;i++) 
            ans=min(ans,f[n][i]);
        printf("%d\n",ans);
    }
}
