#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

struct node
{
    int d,l;
}a[65536];

int T;
int n;
int d;
int f[16484];
int b[16384];
bool flag=false;

bool cmp(node a,node b)
{
    return a.d<b.d;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int w=1;w<=T;w++)
    {
        scanf("%d",&n);
        memset(b,0,sizeof(b));
        for (int i=1;i<=n;i++)
            scanf("%d%d",&(a[i].d),&(a[i].l));
        memset(f,0,sizeof(f));
        f[1]=a[1].d;
        scanf("%d",&d);
        sort(a+1,a+1+n,cmp);
        flag=false;
        for (int i=1;i<=n;i++)
            if (f[i]>0)
            {
                if (a[i].d+f[i]>=d) {flag=true;break;}
                for (int j=i+1;j<=n;j++)
                    if (a[j].d<=a[i].d+f[i])
                        f[j]=max(f[j],min(a[j].d-a[i].d,a[j].l));
                    else break;
            }
        printf("Case #%d: ",w);
        if (flag) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
