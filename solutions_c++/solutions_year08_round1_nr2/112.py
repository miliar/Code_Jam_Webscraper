#include <cstdio>
#include <cstring>
#include <cstdlib>
const int maxn = 2010;
struct data
{
    int x,y;
} f[maxn][maxn];
int t[maxn];
int M[maxn];
int a[maxn];
bool flag[maxn];
int i,j,k,m,n;

bool work()
{
    bool b = true;
    memset(a,0,sizeof(a));
    memset(flag,0,sizeof(flag));
    for (i = 1; i <= m; ++i)
    {
        for (j = 1; j <= t[i]; ++j)
            if (a[f[i][j].x] == f[i][j].y)
            {
                flag[i] = true;
                break;
            }
    }
    while (true)
    {
        b = true;
        for (i = 1;i <= m; ++i)
            if (!flag[i])
                b = false;
        if (b)
            break;
        for (i = 1; i <= m; ++i)
            if (!flag[i])
                if (a[M[i]])
                    return false;
                else a[M[i]] = 1;
        memset(flag,0,sizeof(flag));
        for (i = 1; i <= m; ++i)
        {
            for (j = 1; j <= t[i]; ++j)
                if (a[f[i][j].x] == f[i][j].y)
                {
                    flag[i] = true;
                    break;
                }
        }
    }
    return true;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Test;
    scanf("%d",&Test);
    for (int T = 1; T <= Test; ++T)
    {
        scanf("%d%d",&n,&m);
        for (i = 1;i <= m; ++i)
        {
            scanf("%d",t+i);
            for (j = 1; j <= t[i]; ++j)
            {
                scanf("%d%d",&f[i][j].x,&f[i][j].y);
                if (f[i][j].y == 1)
                    M[i] = f[i][j].x;
            }
        }
        printf("Case #%d: ",T);
        if (!work())
            printf("IMPOSSIBLE\n");
        else 
        {
            for (i = 1;i < n; ++i)
                printf("%d ",a[i]);
            printf("%d\n",a[n]);
        }
    }
    return 0;
}
