#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX 510
#define MAXN 1000100
#define INF 1e10

using namespace std;

const double eps = 1e-12;
double p[MAXN], pp[MAXN];

int n, c;
double d;

bool check(const double t) {
    int i = 0, j = 0;

    for (i = 0; i < n; i++) p[i] = pp[i];
    p[0] -= t;
    for (i = 1; i < n; i++) {
        if (p[i] + t < p[i - 1] + d) return false;
        p[i] = p[i] - t < p[i - 1] + d ? p[i - 1] + d : p[i] - t;
    }

    return true;
}

double solve() {
    double low = 0, high = INF, mid;

    if (n == 1) return 0;
    while (high - low > eps) {
        mid = (low + high) / 2;
        if (check(mid)) high = mid;
        else low = mid;
    }

    return (low + high) / 2;
}

int main() {
    int t, cnt = 1, i, j, v;
    double tp;


    //freopen("B-small-attempt4.in", "r", stdin);
    //freopen("B-small-attempt4.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d %lf", &c, &d);
        n = 0;
        for (i = 0; i < c; i++) {
            scanf("%lf %d", &tp, &v);
            for (j = 0; j < v; j++) pp[n++] = tp;
        }
        sort(pp, pp + n);
        printf("Case #%d: %lf\n", cnt++, solve());
    }


    return 0;
}
