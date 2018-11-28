#include <cstdio>
#include <cmath>

const double eps = 1e-8;
int T, c, d;
int v[300], p[300];
double ret;

bool test(double t) {
    double last = -1e20;
    for (int i = 0; i < c; i++) {
        for (int j = 0; j < v[i]; j++) {
            double dest = last + d;
            if (fabs(dest - p[i]) <= t + eps) {
                last = dest;
            } else if (dest < p[i] - eps) {
                last = p[i] - t;
            } else {
                return false;
            }
        }
    }
    return true;
}

double bs(long long l, long long len) {
    while (len > 0) {
        long long mid = l + len / 2;
        bool f = test(mid * 0.5);
        if (f) {
            len /= 2;
        } else {
            l = mid + 1;
            len = len - (len / 2) - 1;
        }
    }
    return l * 0.5;
}

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d%d", &c, &d);
        for (int i = 0; i < c; i++)
            scanf("%d%d", &p[i], &v[i]);
        /*
        for (int i = 0; i < 100000; i++) {
            if (test(i * 0.5)) {
                ret = i * 0.5;
                break;
            }
        }
        */
        if (!test(500000000000000))
            puts("err!");
        printf("Case #%d: %.20lf\n", t, bs(0, 1000000000000000));
    }
}
