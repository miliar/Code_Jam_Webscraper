#include <cstdio>
#include <algorithm>
using namespace std;

const double eps = 1e-8;

int sgn(double x) {return (x > eps) - (x < -eps);}

int w[110][110];

int n, m, d;

bool check(int a, int b, int c, int d)
{
    double x = 0.0, y = 0.0, cx = (a + c + 1) * 0.5, cy = (b + d + 1) * 0.5;
    for (int i = a; i <= c; ++i)
        for (int j = b; j <= d; ++j) {
            if ((i == a || i == c) && (j == b || j == d)) continue;
            x += (i + 0.5 - cx) * (w[i][j] + d);
            y += (j + 0.5 - cy) * (w[i][j] + d);
        }
//    if (a == 1 && b == 1 && c == 5 && d == 5) printf("%.3f %.3f\n", x, y);
    return sgn(x) == 0 && sgn(y) == 0;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        int ans = 0;
        scanf("%d%d%d", &n, &m, &d);
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) {
            char ch;
            scanf(" %c", &ch);
            w[i][j] = ch - '0';
        }
        for (int i = 0; i < n - 2; ++i)
            for (int j = 0; j < m - 2; ++j)
                for (int r = i + 2; r < n; ++r) {
                    int c = r + j - i;
                    if (check(i, j, r, c)) ans = max(ans, r - i + 1);
                }
        printf("Case #%d: ", cas);
        if (ans == 0) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
    return 0;
}
