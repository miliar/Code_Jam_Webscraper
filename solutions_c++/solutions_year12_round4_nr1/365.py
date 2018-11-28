#include <cstdio>
#include <algorithm>
using namespace std;
int d[10010],b[10010],q[10010],a[10010];
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        int n;
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
            scanf("%d%d",&d[i],&b[i]);
        int D;
        scanf("%d",&d[++n]);
        int l,r;
        q[l=r=1]=d[1]*2;
        a[1]=d[1];
        bool flag=true;
        for (int i=2;i<=n;i++)
        {
            while (l<=r && q[l]<d[i])
                l++;
            if (l>r)
            {
                flag=false;
                break;
            }
            int len=min(d[i]-a[l],b[i]);
            if (d[i]+len>q[r])
            {
                q[++r]=d[i]+len;
                a[r]=d[i];
            }
        }
        static int id=0;
        printf("Case #%d: %s\n",++id,flag?"YES":"NO");
    }
    return(0);
}

