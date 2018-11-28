#include <stdio.h>
#include <algorithm>
using namespace std;
#define MaxN 1010

struct Point {
    int x, y;
    bool operator < (const Point &a) const {return x < a.x;}
}a[MaxN];

int T, n, ans;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) scanf("%d%d", &a[i].x, &a[i].y);
        sort(a, a+n);
        ans = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < i; ++j)
                if (a[j].y > a[i].y) ++ans;
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
