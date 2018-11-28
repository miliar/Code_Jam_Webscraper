#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;


typedef long double DOUBLE;

int     n, D;
int     pos [300];
int     cnt [300];

void init()
{
    scanf("%d%d", &n, &D);
    for (int i = 0; i < n; i ++)
        scanf("%d%d", pos + i, cnt + i);
}

bool checkOK(DOUBLE move)
{
    DOUBLE prev = - 1e20;
    for (int i = 0; i < n; i ++)
    {
        DOUBLE start = max(prev + D, pos[i] - move);
        DOUBLE end = start + (cnt[i] - 1) * D;
        if (fabs(end - pos[i]) > move + 1e-8) return 0;
        prev = end;
    }
    return 1;
}

void solve()
{
    DOUBLE low = 0.0;
    DOUBLE upp = 1e13;

    DOUBLE mid;

    //while (upp - low > 1e-9)
    for (int t = 0; t < 1000; t ++)
    {
        mid = (low + upp) / 2.0;
        if (checkOK(mid))
            upp = mid;
        else
            low = mid;
    }

    printf("%.8lf\n", upp);
    fprintf(stderr, "%.8lf\n", upp);
}

int main()
{    
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-at2.out", "w", stdout);

    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    //freopen("in.txt", "r", stdin);

    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t ++)
    {
        init();
        
        printf("Case #%d: " , t);
        fprintf(stderr, "Case #%d: " , t);
        solve();
    }

    return 0;
}