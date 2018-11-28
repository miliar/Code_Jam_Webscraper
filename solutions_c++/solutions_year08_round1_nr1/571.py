#include<iostream>
#include<algorithm>
using namespace std;
#define MAXSIZE 800

int n;
double v[MAXSIZE],v1[MAXSIZE];

int main()
{
    int T,i,j;
    double ans;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for (i=1;i<=T;i++)
    {
        scanf("%d",&n);
        for (j=0;j<n;j++)
            scanf("%lf",v+j);
        std::sort(v,v+n);
        for (j=0;j<n;j++)
            scanf("%lf",v1+j);
        std::sort(v1,v1+n);
        ans=0;
        for (j=0;j<n;j++)
        {
            ans+=v[j]*v1[n-1-j];
        }
        printf("Case #%d: %.0lf\n",i,ans);
    }
}
