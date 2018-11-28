# include <iostream>
# include <cstdio>
# include <cstring>
# include <vector>
# include <set>
# include <cmath>
# include <queue>
# include <string>
# define MAXN 100
using namespace std;

int main()
{
    int t, n, k, b, ti, i, j, nl, ans, sl;
    double temp;
    scanf("%d", &t);
    int r[MAXN], v[MAXN];
    for (int tt = 1; tt <= t; tt++) {
        nl = 0;
        sl = 0;
        ans = 0;
        scanf("%d%d%d%d", &n, &k, &b, &ti);
        for (i = 0; i < n; i++) {
            scanf("%d", &r[i]);
        }
        for (i = 0; i < n; i++) {
            scanf("%d", &v[i]);
        }
        for (i = n - 1; i >= 0; i--) {
            temp = double(b - r[i]) / double(v[i]);
            if (temp < double(ti) || fabs(temp - double(ti)) < 1e-9) {
                ans += nl;
                sl++;
            }
            else {
                nl++;
            }
            if (sl >= k) {
                break;
            }
        }
        if (sl >= k) {
            printf("Case #%d: %d\n", tt, ans);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n", tt);
        }
    }
    return 0;
}
