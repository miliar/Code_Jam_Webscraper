#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define eps 1e-8
#define max(a,b)    a>b?a:b;
#define min(a,b)    a<b?a:b;
#define INF 0x3fffffff
int pos[105],n,c,d;
int check(double t)
{
    double pre=pos[1]-t;
    for(int i=2;i<=n;i++)
    {
        if(pre+d<=pos[i])
        {
            if(pos[i]-t<=pre+d)
            {
                pre=pre+d;
            }
            else
            {
                pre=pos[i]-t;
            }
        }
        else
        {
            if(pos[i]+t>=pre+d)
            {
                pre=pre+d;
            }
            else
            {
                return 0;
            }
        }
    }
    return 1;
}
double bifind(double l,double r)
{
    while(r-l>eps)
    {
        double mid=(l+r)/2;
        int mark=check(mid);
        if(mark)    r=mid;
        else        l=mid;
    }
    return r;
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        scanf("%d%d",&c,&d);
        n=0;
        for(int i=1;i<=c;i++)
        {
            int x,num;
            scanf("%d%d",&x,&num);
            for(int j=1;j<=num;j++)
            {
                n++;
                pos[n]=x;
            }
        }
        double ans=bifind(0,d*n);
        printf("Case #%d: %f\n",cas,ans);
    }
    return 0;
}
