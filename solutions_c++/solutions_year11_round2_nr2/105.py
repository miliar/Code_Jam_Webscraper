#include <iostream>
#include <cmath>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int p[1000000], d, c, n;

int main() {
    int tot_t;
    scanf("%d", &tot_t);
    for (int cur_t = 0; cur_t < tot_t; ++cur_t) {
        scanf("%d%d", &c, &d);
        n = 0;
        for (int i = 0; i < c; ++i) {
            int a, b;
            scanf("%d%d", &a, &b);
            while (b--) {
                p[n++] = a;
            }
        }

        double low = 0, high = 1e12 + 10;
        for (int iter = 0; iter < 70; ++iter) {
            double mid = (low + high) / 2;
            double last = p[0] - mid;
            bool ok = true;

            for (int i = 1; i < n; ++i) {
                if (last + d > p[i] + mid) {
                    ok = false;
                    break;
                }
                last = max(last + d, p[i] - mid);
            }

            if (ok) {
                high = mid;
            } else {
                low = mid;
            }
        }

        char buf[20];
        double tmp;
        sprintf(buf, "%.1f", (low + high) / 2);
        sscanf(buf, "%lf", &tmp);

        if (fabs(tmp - (low + high) / 2) >= 1e-6 && fabs(1 - tmp / ((low + high) / 2)) >= 1e-6) {
            puts("WARN!");
        }

        printf("Case #%d: %.10f\n", cur_t + 1, (low + high) / 2);
    }
    return 0;
}
