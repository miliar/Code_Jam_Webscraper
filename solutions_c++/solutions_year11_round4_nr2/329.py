#include <cstdio>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <queue>
#define sys system("pause")
using namespace std;
typedef long long ll;
ll cx[610][610], cy[610][610], c[610][610];
ll dx[610][610], dy[610][610], d[610][610];
int g[610][610];

int main() {
  //      freopen("a.in", "r", stdin);
  //   freopen("a.txt", "w", stdout);
    int T, cas = 1;
    int n, m, k;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d%d", &n, &m, &d);
        memset(cx, 0, sizeof(cx));
        memset(cy, 0, sizeof(cy));
        memset(c, 0, sizeof(c));
        memset(dx, 0, sizeof(dx));
        memset(dy, 0, sizeof(dy));
        memset(d, 0, sizeof(d));
        char ch;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                cin >> ch;
                g[i][j] = ch - '0';
                dx[i][j] = (ll) (k + g[i][j]) * i;
                dy[i][j] = (ll) (k + g[i][j]) * j;
                cx[i][j] = dx[i][j];
                cy[i][j] = dy[i][j];
                d[i][j] = (k + g[i][j]);
                c[i][j] = d[i][j];
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                dx[i][j] += dx[i][j - 1];
                dy[i][j] += dy[i][j - 1];
                d[i][j] += d[i][j - 1];
            }
        }
        for (int j = 1; j <= m; j++) {
            for (int i = 1; i <= n; i++) {
                dx[i][j] += dx[i - 1][j];
                dy[i][j] += dy[i - 1][j];
                d[i][j] += d[i - 1][j];
            }
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int len = min(n - i, m - j);
                while (len + 1 >= 3) {
                    ll ddx = dx[i + len][j + len] + dx[i - 1][j - 1] - dx[i - 1][j + len] - dx[i + len][j - 1]
                            - cx[i][j] - cx[i][j + len] - cx[i + len][j] - cx[i + len][j + len];
                    ll ddy = dy[i + len][j + len] + dy[i - 1][j - 1] - dy[i - 1][j + len] - dy[i + len][j - 1]
                            - cy[i][j] - cy[i][j + len] - cy[i + len][j] - cy[i + len][j + len];
                    ll dd = d[i + len][j + len] + d[i - 1][j - 1] - d[i - 1][j + len] - d[i + len][j - 1]
                            - c[i][j] - c[i][j + len] - c[i + len][j] - c[i + len][j + len];
                    if (len & 1) {
                        ddx *= 2;
                        ddy *= 2;
                        int x = (i + i + len);
                        int y = (j + j + len);
                        if (ddx - dd * x == 0LL && ddy - dd * y == 0LL) {
                            ans = max(ans, len + 1);
                        }
                    } else {
                        int x = (i + i + len) / 2;
                        int y = (j + j + len) / 2;
                        if (ddx - dd * x == 0LL && ddy - dd * y == 0LL) {
                            ans = max(ans, len + 1);
                        }
                    }
                    len--;
                }
            }
        }
        printf("Case #%d: ", cas++);
        if (ans >= 3) {
            printf("%d\n", ans);
        } else {
            puts("IMPOSSIBLE");
        }
        //sys;
    }
    return 0;
}
