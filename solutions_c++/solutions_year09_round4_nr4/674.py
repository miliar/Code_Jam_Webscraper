#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int t, n;
double x[3], y[3], r[3];

void solve();

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}

void solve() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf("%lf%lf%lf", &x[i], &y[i], &r[i]);
    if (n == 1) {
        printf("Case #%d: %.7lf\n", ++t, r[0]);
        return;
    }
    if (n == 2) {
        printf("Case #%d: %.7lf\n", ++t, max(r[0], r[1]));
        return;
    }
    if (n == 3) {
        double d1 = max(r[0] * 2.0, sqrt((x[2] - x[1]) * (x[2] - x[1]) + (y[2] - y[1]) * (y[2] - y[1])) + r[1] + r[2]);
        double d2 = max(r[1] * 2.0, sqrt((x[2] - x[0]) * (x[2] - x[0]) + (y[2] - y[0]) * (y[2] - y[0])) + r[2] + r[0]);
        double d3 = max(r[2] * 2.0, sqrt((x[1] - x[0]) * (x[1] - x[0]) + (y[1] - y[0]) * (y[1] - y[0])) + r[1] + r[0]);
        printf("Case #%d: %.7lf\n", ++t, min(min(d1, d2), d3) / 2.0);
    }
}
