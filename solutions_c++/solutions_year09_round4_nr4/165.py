#include <stdio.h>
#include <math.h>
int tests,n,x[100],y[100],r[100];
double dis[110][110];
int sqr(int x)
{
    return x*x;
}
int main()
{
    freopen("d1.in","r",stdin);
    freopen("d1.out","w",stdout);
    scanf("%d",&tests);

    for (int t0=1;t0<=tests;t0++)
    {
        scanf("%d",&n);
        for (int i=0;i<n;i++)
        {
            scanf("%d%d%d",&x[i],&y[i],&r[i]);
        }                 
//        printf("%d\n",tests);       
//        if (n>3) continue;
//
//        printf("%d\n",n);
        for (int i=0;i<3;i++)
        {
            for (int j=0;j<3;j++)
              dis[i][j]=sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j])+0.0)+r[i]+r[j];
        }
        double ans;
        if (n==1) ans=dis[0][0];
        else if (n==2) ans=dis[0][0]>?dis[1][1];
        else
        {
            ans=dis[0][0]>?dis[1][2];
            ans<?=dis[1][1]>?dis[0][2];
            ans<?=dis[2][2]>?dis[0][1];
        }
        printf("Case #%d: %.5f\n",t0,ans/2);
    }
}
