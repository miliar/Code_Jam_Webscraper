#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxn = 10000 + 10;
struct vine
{
    int x,l;
} a[maxn];
bool flag;
int n, len, f[maxn];

int min(int x, int y)
{
    if (x<y) return x;
    return y;
}

int max(int x,int y)
{
    if (x>y) return x;
    return y;
}

void work()
{
    flag = false;
    f[1] = min(a[1].x, a[1].l) * 2;
    if (f[1] >= len)
    {
        flag = true;
        return;
    }
    for (int i = 2; i <= n; ++i)
    {
        for (int j = 1; j < i; ++j)
            if (f[j] >= a[i].x)
                f[i] = max(f[i], a[i].x + min(a[i].x - a[j].x, a[i].l));
        if (f[i] >= len)
        {
            flag = true;
            return;
        }
    }
}

bool cmp(vine x, vine y)
{
    return x.x < y.x;
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int tot;
    scanf("%d",&tot);
    for (int tc = 1; tc <= tot; ++tc)
    {
        scanf("%d",&n);
        for (int i = 1; i <= n; ++i)
            scanf("%d %d",&a[i].x,&a[i].l);
        memset(f,0,sizeof(f));
        scanf("%d",&len);

        sort(a + 1, a + n + 1, cmp);
        work();

        printf("Case #%d: ", tc);
        if (flag)
            puts("YES");
        else
            puts("NO");
    }
    return 0;
}
