#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
const int MAXN = 201;
int n, d;
struct data {
    int p, v;
    bool operator <(const data& d) const {
        return p < d.p;
    }
}a[MAXN];

bool check(double mid) {
    double last = a[0].p - mid + d * (a[0].v - 1);
    if (last - a[0].p > mid) return 0;
    for (int i = 1; i < n; i++) {
        if (a[i].p - mid - last >= d) {
            if (-mid + d * (a[i].v - 1) <= mid) {
                last = a[i].p - mid + d * (a[i].v - 1);
            } else {
                return 0;
            }
        } else {
            if (last + d - a[i].p > mid) return 0;
            if (last + d + d * (a[i].v - 1) - a[i].p <= mid) {
                last = last + d + d * (a[i].v - 1);
            } else {
                return 0;
            }
        }
        
    }
    return 1;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T++) {
        scanf("%d%d", &n, &d);
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &a[i].p, &a[i].v);
        }
        sort(a, a + n);
        double l = 0, r = 1e9;
        while (fabs(r - l) > 1e-4) {
            double mid = (l + r) / 2;
            if (check(mid)) {
                r = mid;
            } else {
                l = mid;
            }
        }
        printf("Case #%d: %.3lf\n", T, l);
    }
}
