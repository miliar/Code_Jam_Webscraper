#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std;

const int maxn = 10;
int cases, cas = 1, n;
double x[maxn], y[maxn], r[maxn];

double dist(double x1, double y1, double x2, double y2) {
    double x = x1 - x2, y = y1 - y2;
    return sqrt(x * x + y * y);
}

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%lf%lf%lf", &x[i], &y[i], &r[i]);
        }
        if (n == 1) {
            printf("Case #%d: %.10lf\n", cas++, r[0]);
        } else if (n == 2) {
            printf("Case #%d: %.10lf\n", cas++, max(r[0], r[1]));
        } else if (n == 3) {
            double d[3];
            for (int i = 0; i < 3; ++i) {
                int j = (i + 1) % 3;
                d[i] = (dist(x[i], y[i], x[j], y[j]) + r[i] + r[j]) / 2.0;
            }
            double ans = 1e100;
            for (int i = 0; i < 3; ++i) {
                int k = (i + 2) % 3;
                ans = min(ans, max(d[i], r[k]));
            }
            printf("Case #%d: %.10lf\n", cas++, ans);
        }
    }
    return 0;
}
