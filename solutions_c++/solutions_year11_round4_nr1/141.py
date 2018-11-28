#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 5000;
int e[N], b[N], w[N];

struct point {
    int speed, len;
    point(int x = 0, int y = 0):speed(x), len(y) {}
} a[N];

bool cmp(const point &a, const point &b) {
    return (a.speed < b.speed);
}

int main() {
    int tt, cas;
    int S, R, N, X;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas ++) {
        double t;
        scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);
        int tot = 0, m = 0;
        for (int i = 0; i < N; i ++) {
            scanf("%d%d%d", &b[i], &e[i], &w[i]);
            tot += e[i] - b[i];
            a[m ++] = point(w[i], e[i] - b[i]);
        }
        if (tot < X) a[m ++] = point(0, X - tot);
        sort(a, a + m, cmp);
        double ans = 0;
        for (int i = 0; i < m; i ++) {
            double t1 = (double)a[i].len / (a[i].speed + S);
            double t2 = (double)a[i].len / (a[i].speed + R);
            if (t2 < t) {
                ans += t2;
                t -= t2;
            } else {
                if (((double)a[i].len - (double)t * (R + a[i].speed)) / (S + a[i].speed) < 0) printf("Error!!\n");
                ans += t + ((double)a[i].len - (double)t * (R + a[i].speed)) / (S + a[i].speed);
                t = 0;
            }
        }
        printf("Case #%d: %.10f\n", cas, ans);
    }
    return 0;
}

