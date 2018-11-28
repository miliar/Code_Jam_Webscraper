#include <stdio.h>
#include <string.h>
int a[1010];
double d[1010],out[1010];
double sum;
int n;
bool check(int id,double x)
{
    double num=a[id]+x*sum/100.0;
    double tsum=0;
    for (int i=0;i<n;i++)
    {
        if (num>a[i]) tsum+=(num-a[i])*100.0/sum;
    }
    if (tsum>=100+1e-10) return true;
    return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1; ii<=T; ii++)
    {
        scanf("%d",&n);
        int zeros=0;
        sum=0;
        for (int i=0; i<n; i++)
        {
            scanf("%d",&a[i]);
            sum+=a[i];
        }
        for (int i=0;i<n;i++)
        {
            double l=0,r=100;
            for (int j=0;j<1000;j++)
            {
                double mid=(l+r)/2.0;
                if (check(i,mid)) r=mid;
                else l=mid;
            }
            out[i]=l;
        }
        printf("Case #%d:",ii);
        for (int i=0;i<n;i++)
            printf(" %.10f",out[i]);
        puts("");
    }
    return 0;
}
