#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#define sqr(x) ((x)*(x))
using namespace std;

const int maxn = 1000 + 10;
struct stu
{
    int r,id;
} r[maxn];
int n,w,l;
bool flag = false;
double ans[maxn][2];

double dist(double x1, double y1, double x2, double y2)
{
    return sqrt(sqr(x1-x2)+sqr(y1-y2));
}

bool check(int cur, double x, double y)
{
    for (int i = 0; i < cur; ++i)
        if (dist(x, y, ans[i][0], ans[i][1]) < r[i].r + r[cur].r)
            return false;
    return true;
}

double cal(int cur, double x, double low, double up)
{
    if (up - low < 1e-4) return up;
    double mid = (low + up) / 2;
    if (check(cur, x, mid))
        return cal(cur, x, low, mid);
    else
        return cal(cur, x, mid, up);
}

void work()
{
    double lx=0, ly=0;
    for (int i = 1; i < n; ++i)
    {
        if (r[i].r == 72609)
        {
            ++i;
            --i;
        }
        double x=lx+r[i].r+r[i-1].r,y;
        if (x > w +1e-8)
            x = 0;

        if (!check(i, x, l))
        {
            flag = true;
            return;
        }
        y = cal(i, x, 0, l);
        ans[i][0] = x;
        ans[i][1] = y;
        lx = x; ly = y;
    }
}

bool cmp(stu x, stu y)
{
    return x.r < y.r;
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int tot;
    scanf("%d",&tot);
    for (int tc=1;tc<=tot;++tc)
    {
        scanf("%d%d%d", &n, &w, &l);
        for (int i = 0; i < n; ++i)
        {
            r[i].id = i;
            scanf("%d", &r[i].r);
        }
        sort(r, r + n, cmp);

        printf("Case #%d: ", tc);

        work();

        if (flag)
        {
            puts("fail");
            return 0;
        }
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (r[j].id == i)
                    printf("%.6lf %.6lf ", ans[j][0], ans[j][1]);
        printf("\n");
    }
    return 0;
}

/*
#include <cstdio>
#include <cmath>
#define sqr(x) ((x)*(x))
const int maxt = 100, maxn = 20;
int r[maxn];
double ans[maxt][maxn][2];

double dist(double x1, double y1, double x2, double y2)
{
    return sqrt(sqr(x1-x2)+sqr(y1-y2));
}

int main()
{
    freopen("a.out", "r",stdin);
    for (int i = 0; i < 45; ++i)
    {
        char x = 'a';
        while (x != ':') scanf(" %c", &x);
        for (int j = 0; j < 10; ++j)
            scanf("%lf %lf", &ans[i][j][0], &ans[i][j][1]);
    }
    freopen("a.in","r",stdin);
    int tmp;
    scanf("%d",&tmp);
    for (int i = 0; i < 5; ++i)
    {
        int n,w,l;
        scanf("%d%d%d",&n,&w,&l);
        for (int j = 0; j < n; ++j)
        {
            int tmp;
            scanf("%d",&tmp);
        }
    }
    for (int i = 0;i < 45; ++i)
    {
        int n,w,l;
        scanf("%d%d%d",&n,&w,&l);
        for (int j = 0; j < n;++j)
            scanf("%d",&r[j]);
        bool flag = false;
        for (int j = 0; j < n; ++j)
            for (int k = j+1; k < n;++k)
                if (dist(ans[i][j][0], ans[i][j][1], ans[i][k][0], ans[i][k][1]) < r[j]+r[k])
                {
                    printf("%d %d\n", j,k);
                    flag = true;
                    break;
                }
        if (flag)
        {
            printf("%d\n", i+6);
            return 0;
        }
    }
    return 0;
}
*/
