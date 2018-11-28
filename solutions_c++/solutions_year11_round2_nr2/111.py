#include <cstdio>
#include <algorithm>
#define MaxN 210
using namespace std;

struct Node {
    int p, v;
    bool operator < (const Node& a) const {
        return p < a.p;
    }
}a[MaxN];

int n, D;

const double eps = 1e-12;

bool check(double t)
{
    double pre = -1e14;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < a[i].v; ++j) {
            if (pre + D > a[i].p + t) return 0;
            pre = max(pre + D, a[i].p - t);
        }
    }
    return 1;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d%d", &n, &D);
        int V = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", &a[i].p, &a[i].v);
            V += a[i].v;
        }
        sort(a, a+n);
        double l = 0.0, r = (double)V*D;
        for (int iter = 0; iter < 1000; ++iter) {
            double d = (l+r) / 2.0;
            if (check(d)) r = d;
            else l = d;
        }
        printf("Case #%d: %.12f\n", cas, (l+r)/2);
    }
    return 0;
}
