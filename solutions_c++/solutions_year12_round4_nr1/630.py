#include <cstdio>
#include <algorithm>

using namespace std;

int n,m,a[10100],b[10100],f[10100];

int main()
{
    freopen("Swinging.in","r",stdin);
    freopen("Swinging.out","w",stdout);
    int tt,t,i,j,tmp,s;
    scanf("%d",&tt);
    for (t = 1;t<=tt;t++)
    {
        scanf("%d",&n);
        for (i = 1;i<=n;i++) scanf("%d%d",&a[i],&b[i]);
        for (i = 1;i<=n;i++) b[i]=min(b[i],a[i]);
        scanf("%d",&m);
        for (i = n;i>=1;i--)
        {
            tmp=b[i]+1;
            if (m-a[i]<=tmp) tmp=m-a[i];
            for (j = i+1;j<=n;j++)
            {
                s=a[j]-a[i];
                if (s>b[i] || s<f[j] || f[j]==-1) continue;
                if (s<tmp) tmp=s;
                break;
            }
            if (tmp>b[i]) f[i]=-1; else f[i]=tmp;
        }
        printf("Case #%d: ",t);
        if (f[1]!=-1) printf("YES\n"); else printf("NO\n");
    }
}
