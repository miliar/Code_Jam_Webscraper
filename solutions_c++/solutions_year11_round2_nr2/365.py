#include<iostream>
using namespace std;
const int maxn=210;
double s[maxn],e[maxn];
double eps=1e-10;
int a[maxn],b[maxn],n,lim;
int check(double x)
{
    int i;
    for (i=0;i<n;i++)
    {
        if (i==0) s[i]=a[i]-x;
        else s[i]=max(e[i-1]+lim,a[i]-x);
        e[i]=s[i]+(b[i]-1)*lim;
        if (e[i]>a[i]+x) return 0;
    }    
    return 1;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,tt,cases;
    double l,r,mid;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        scanf("%d%d",&n,&lim);
        for (i=0;i<n;i++)
        scanf("%d%d",&a[i],&b[i]);
        l=-eps;
        r=1e13;
        while (l+eps<r)
        {
              mid=(l+r)/2;
              if (check(mid)) r=mid;
              else l=mid;
        }
        printf("Case #%d: %.10lf\n",tt+1,r);
    }
    return 0;
}
