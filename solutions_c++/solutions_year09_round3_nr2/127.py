#include <cstdio>
#include <cmath>

#include <algorithm>

using namespace std;

template<typename T>
T Sqr(T x) {
    return x*x;
}

int main() {
    // freopen("input.txt", "r", stdin);
    // freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
    freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);

    int nT;
    scanf("%d", &nT);
    for (int t = 0; t < nT; ++t) {
        int n;
        scanf("%d", &n);
        double x = 0;
        double y = 0;
        double z = 0;
        double vx = 0;
        double vy = 0;
        double vz = 0;
        for (int i = 0; i < n; ++i) {
            double dx, dy, dz, dvx, dvy, dvz;
            scanf("%lf%lf%lf%lf%lf%lf", &dx, &dy, &dz, &dvx, &dvy, &dvz);
            x += dx;
            y += dy;
            z += dz;
            vx += dvx;
            vy += dvy;
            vz += dvz;
        }
        x /= n;
        y /= n;
        z /= n;
        vx /= n;
        vy /= n;
        vz /= n;

        double d0 = sqrt( Sqr(x) + Sqr(y) + Sqr(z) );
        double t0 = 0;
        double v2 = Sqr(vx) + Sqr(vy) + Sqr(vz);
        if (fabs(v2) > 1E-10) {
            double minT = -(x*vx + y*vy + z*vz) / v2;
            if (minT >= 0) {
                double x2 = x + minT*vx;
                double y2 = y + minT*vy;
                double z2 = z + minT*vz;
                double d1 = sqrt( Sqr(x2) + Sqr(y2) + Sqr(z2) );
                if (d1 < d0) {
                    d0 = d1;
                    t0 = minT;
                }
            }
        }

        printf("Case #%d: %.10lf %.10lf\n", t + 1, d0, t0);
    }
    
    return 0;
}
