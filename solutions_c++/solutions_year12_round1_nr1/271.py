#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int tn;
int n,m;
double ans;
double p[131072];
double f[131072];
double e[131072];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tn);
    for (int w=1;w<=tn;w++)
    {
        scanf("%d%d",&n,&m);
        for (int i=1;i<=n;i++)
            scanf("%lf",p+i);
        f[0]=1;
        for (int i=1;i<=n;i++)
            f[i]=f[i-1]*p[i];
        ans=2+m;
        for (int i=0;i<=n;i++)
        {
            e[i]=(i*2+m-n+1)*f[n-i]+(i*2+m-n+1+m+1)*(1.0-f[n-i]);
            if (e[i]<ans) ans=e[i];
        }
        printf("Case #%d: %.6lf\n",w,ans);
    }
    return 0;
}
