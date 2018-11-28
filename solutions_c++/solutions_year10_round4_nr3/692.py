#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int a[105][105], b[105][105];

bool zero() {
    int i, j;
    for (i = 1; i <= 100; ++i)
        for (j = 1; j <= 100; ++j)
            if (a[i][j])
                return 0;
    return 1;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int t, i, n, cnt, j, cas = 0, ax, ay, bx, by, x, y;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        memset(a, 0, sizeof(a));
        for (i = 0; i < n; ++i) {
            scanf("%d %d %d %d", &ax, &ay, &bx, &by);
            if (ax > bx) swap(ax, bx);
            if (ay > by) swap(ay, by);
            for (x = ax; x <= bx; ++x)
                for (y = ay; y <= by; ++y)
                    a[x][y] = 1;
        }
        cnt = 0;
        while (!zero()) {
            ++cnt;
            memset(b, 0, sizeof(b));
            for (i = 1; i <= 100; ++i)
                for (j = 1; j <= 100; ++j)
                    if (!a[i][j]) {
                        if (a[i - 1][j] && a[i][j - 1])
                            b[i][j] = 1;
                        else
                            b[i][j] = 0;
                    } else {
                        if (!a[i - 1][j] && !a[i][j - 1])
                            b[i][j] = 0;
                        else
                            b[i][j] = 1;
                    }
            memcpy(a, b, sizeof(b));
        }
        printf("Case #%d: %d\n", ++cas, cnt);
    }
    return 0;
}
