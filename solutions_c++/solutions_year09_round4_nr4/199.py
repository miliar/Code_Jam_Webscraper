#include <cstdio>
#include <cmath>
#include <algorithm>
using std::sort;
using std::max;

inline double sqr(double x) {
    return x * x;
}

struct Point {
    double x, y, r;
    double dis(const Point& rhs) const {
        double norm = sqrt(sqr(x - rhs.x) + sqr(y - rhs.y));
        norm += r + rhs.r;
        return norm;
    }
};

int main() {
    int t, T, i;
    int n;
    Point p[10];

    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%d", &n);
        for (i = 0; i < n; i++)
            scanf("%lf%lf%lf", &p[i].x, &p[i].y, &p[i].r);
        if (n == 1) {
            printf("%.10lf\n", p[0].r);
            continue;
        } else if (n == 2) {
            printf("%.10lf\n", max(p[0].r, p[1].r));
            continue;
        }
        double ans[3] = {
            max(p[0].dis(p[1]) / 2, p[2].r),
            max(p[0].dis(p[2]) / 2, p[1].r),
            max(p[1].dis(p[2]) / 2, p[0].r)
        };
        sort(ans, ans + 3);
        printf("%.10lf\n", ans[0]);
    }
}
