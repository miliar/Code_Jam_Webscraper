#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int g[20][20], r, c, d;

int main() {
    int tot_t;
    scanf("%d", &tot_t);
    for (int cur_t = 0; cur_t < tot_t; ++cur_t) {
        scanf("%d%d%d", &r, &c, &d);
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                scanf("%1d", &g[i][j]);
                g[i][j] += d;
            }
        }
        int ans = 1;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                for (int k = 3; i + k <= r && j + k <= c; ++k) {
                    double sumx = 0, sumy = 0;
                    for (int x = i; x < i + k; ++x) {
                        double cx = i + k / 2.0;
                        double cy = j + k / 2.0;
                        int lower = x == i || x == i + k - 1 ? j + 1 : j;
                        int upper = x == i || x == i + k - 1 ? j + k - 1 : j + k;
                        for (int y = lower; y < upper; ++y) {
                            sumx += (x + 0.5 - cx) * g[x][y];
                            sumy += (y + 0.5 - cy) * g[x][y];
                        }
                    }
                    if (fabs(sumx) < 1e-9 && fabs(sumy) < 1e-9) {
                        ans = max(ans, k);
                    }
                }
            }
        }
        if (ans >= 3) {
            printf("Case #%d: %d\n", cur_t + 1, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", cur_t + 1);
        }
    }
    return 0;
}

