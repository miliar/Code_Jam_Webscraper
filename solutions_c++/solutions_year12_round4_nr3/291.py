#include <cstdio>
#include <algorithm>

using namespace std;

int n,ans[2010],k[2010],inf=1<<20,h[2010];

int main()
{
    freopen("Mountain.in","r",stdin);
    freopen("Mountain.out","w",stdout);
    int t,tt,i,j,p,tmp;
    bool ok;
    scanf("%d",&tt);
    for (t = 1;t<=tt;t++)
    {
        scanf("%d",&n);
        for (i = 1;i<n;i++) scanf("%d",&h[i]);
        p=1;ok=true;
        for (i = 1;i<n;i++)
            for (j = i+1;j<h[i];j++)
            if (h[j]>h[i]) { ok=false;break; }
        printf("Case #%d:",t);
        if (!ok) { printf(" Impossible\n");continue; }
        ans[n]=inf;k[n]=1;
        for (i = n;i>1;i--)
        {
            p=-1;
            for (j = 1;j<i;j++)
                if (h[j]==i) { p=j;break; }
            if (p==-1) continue;
            tmp=ans[i]-(i-p)*k[i];
            for (j = 1;j<i;j++)
            if (h[j]==i)
            {
                ans[j]=tmp;
                k[j]=(ans[i]-ans[j]) / (i-j) + 1;
            }
        }
        tmp=inf;
        for (i = 1;i<=n;i++) tmp=min(tmp,ans[i]);
        for (i = n;i>=1;i--)
        {
            ans[i]-=tmp-1;
        }
        for (i = 1;i<=n;i++) printf(" %d",ans[i]);
        printf("\n");
    }
}
