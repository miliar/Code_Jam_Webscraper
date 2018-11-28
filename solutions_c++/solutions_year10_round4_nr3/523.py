#include <stdio.h>
#include <string.h>
#include <algorithm>
#define MaxN 110
using namespace std;

bool a[MaxN][MaxN], b[MaxN][MaxN];
int T, t, r1, c1, r2, c2, n, m, ans;

bool in(int x, int y)
{
    return x > 0 && y > 0;
}

void print()
{
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j)
            putchar(a[i][j] ? '1' : '0');
        puts("");
    }
    puts("");
}

bool check()
{
    bool found = 0;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) {
            if (a[i][j] == 1) {
                if ((!in(i-1, j) || a[i-1][j] == 0) && (!in(i, j-1) || a[i][j-1] == 0)) b[i][j] = 0;
                else b[i][j] = 1;
            }
            else {
                if (in(i-1, j) && in(i, j-1) && a[i-1][j] == 1 && a[i][j-1] == 1) b[i][j] = 1;
                else b[i][j] = 0;
            }
            if (b[i][j] == 1) found = 1;
        }
    memcpy(a, b, sizeof(bool)*MaxN*MaxN);
    //print();
    return found;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        ans = 1;
        scanf("%d", &t);
            memset(a, 0, sizeof(a));
        while (t--) {
            scanf("%d%d%d%d", &r1, &c1, &r2, &c2);
            n = max(max(n, r1), r2);
            m = max(max(m, c1), c2);
            for (int r = r1; r <= r2; ++r)
                for (int c = c1; c <= c2; ++c)
                    a[r][c] = 1;
        }
        while (check()) ++ans;
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
