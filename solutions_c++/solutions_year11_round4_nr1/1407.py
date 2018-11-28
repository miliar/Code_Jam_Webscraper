#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define N 1000005

int u[N], v[N], a[N];

bool cmp(int l, int r) {
    return 1.0 / u[l] + 1.0 / v[r] < 1.0 / u[r] + 1.0 / v[l];
}

double solve() {
    int x, v0, u0, t, n;
    scanf("%d %d %d %d %d", &x, &v0, &u0, &t, &n);
    for (int i = 0; i < x; ++i) {
        v[i] = v0;
        u[i] = u0;
    }
    for (int i = 0; i < n; ++i) {
        int b, e, w;
        scanf("%d %d %d", &b, &e, &w);
        for (int j = b; j < e; ++j) {
            v[j] += w;
            u[j] += w;
        }
    }
    for (int i = 0; i < x; ++i)
        a[i] = i;
    sort(a, a + x, cmp);
    double ret = 0, left = t;
    for (int i = 0; i < x; ++i) {
        int k = a[i];
        if (left < 1e-8) {
            ret += 1.0 / v[k];
        } else {
            double delta = min(left, 1.0 / u[k]);
            double dis = delta * u[k];
            ret += delta + (1 - dis) / v[k];
            left -= delta;
        }
    }
    return ret;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--)
        printf("Case #%d: %.8lf\n", ++cas, solve());
    return 0;
}
