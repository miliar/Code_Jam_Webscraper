#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

int n;

double cal(double* a,double* b)
{
    int i;
    double sum=0;
    
    for(i=0;i<n;++i)
        sum+=a[i]*b[i];
    return sum;
}

int main()
{
    int re,i,cas;
    double a[1024],b[1024],best;
    
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    for(scanf("%d",&re),cas=1;re--;++cas){
        scanf("%d",&n);
        for(i=0;i<n;++i)
            scanf("%lf",&a[i]);
        for(i=0;i<n;++i)
            scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n,greater<double>());
        best=cal(a,b);
        printf("Case #%d: %.0lf\n",cas,best);
    }
}
