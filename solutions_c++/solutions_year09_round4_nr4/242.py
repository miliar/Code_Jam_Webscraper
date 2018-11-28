#include<math.h>
#include<stdio.h>
#include<string.h>
int x[11],y[11],r[11];
double min(double x,double y)
{
    return (x>y)?y:x;
}
double max(double x,double y)
{
    return (x>y)?x:y;
}
double dis(int a,int b)
{
    return r[a]+r[b]+sqrt((x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b]));
}
int main()
{
    int t;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out","w",stdout);
    scanf("%d",&t);
    for (int tt=1;tt<=t;tt++)
    {
        int n;
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
            scanf("%d%d%d",x+i,y+i,r+i);
        double ans,ans1,ans2,ans3;
        if (n==1) ans=r[1];
        if (n==2) ans=max(r[1],r[2]);
        if (n==3)
        {
            ans1=max(dis(1,2),r[3])/2;
            ans2=max(dis(2,3),r[1])/2;
            ans3=max(dis(3,1),r[2])/2;
            ans=min(ans1,min(ans2,ans3));
        }
        printf("Case #%d: %.8lf\n",tt,ans);
    }
}