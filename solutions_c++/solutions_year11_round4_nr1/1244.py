#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int MAXX = 1000010;
int x, s, r, n;
double t;
int a[MAXX];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases;
    scanf("%d", &cases);
    for (int k = 1; k <= cases; ++k) {
        printf("Case #%d: ", k);
        scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
        
        for (int i = 0; i < x; ++i) {
            a[i] = 0;
        }
        for (int i = 0; i < n; ++i) {
            int b, e, w;
            scanf("%d%d%d", &b, &e, &w);
            for (int j = b; j < e; ++j) {
                a[j] = w;
            }
        }
        double ans = 0;
        for (int i = 0; i < x; ++i) {
            ans +=  1. / (s + a[i]);
        }
        sort(a, a + x);
        for (int i = 0; i < x; ++i) {
            if (t <= 0) break;
            if (t >= 1. / (r + a[i])) {
               ans -= 1. / (s + a[i]) - 1. / (r + a[i]);
               t -= 1. / (r + a[i]);
            } else {
                ans -= (r + a[i]) * t / (s + a[i]) - t;
                t = 0;
            }
        }
        printf("%.11lf\n", ans);
        
    }
    return 0;
}
