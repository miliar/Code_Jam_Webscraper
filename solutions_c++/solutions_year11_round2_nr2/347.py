#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define N 2005

struct Node {
    int x, c;
    bool operator < (const Node & b) const {
        return x < b.x;
    }
};

int n, d;
Node a[N];

bool ch(double dt) {
    double lx, rx;
    rx = -1e30;
    for (int i = 0; i < n; ++i) {
        lx = max(rx + d, a[i].x - dt);
        rx = lx + (a[i].c - 1) * d;
        if (rx - a[i].x > dt) return 0;
    }
    return 1;
}

double solve() {
    scanf("%d %d", &n, &d);
    for (int i = 0; i < n; ++i)
        scanf("%d %d", &a[i].x, &a[i].c);
    sort(a, a + n);
    double l = 0, r = 1e13;
    while (r - l > 1e-7) {
        double mid = (l + r) * 0.5;
        if (ch(mid)) r = mid;
        else l = mid;
    }
    return (l + r) * 0.5;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--)
        printf("Case #%d: %.8lf\n", ++cas, solve());
    return 0;
}
