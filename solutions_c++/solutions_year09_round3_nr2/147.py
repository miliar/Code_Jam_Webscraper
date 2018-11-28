#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    freopen("B.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int ca = 1;
    while (t--) {
        double a = 0, b = 0, c = 0, d = 0, e = 0, f = 0;
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            double x, y, z, vx, vy, vz;
            scanf("%lf %lf %lf %lf %lf %lf", &x, &y, &z, &vx, &vy, &vz);
            a += x;
            b += vx;
            c += y;
            d += vy;
            e += z;
            f += vz;
        }
        a /= n;
        b /= n;
        c /= n;
        d /= n;
        e /= n;
        f /= n;
        double A = b * b + d * d + f * f;
        double B = 2 * (e * f + c * d + a * b);
        double C = a * a + c * c + e * e;
        printf("Case #%d: ", ca++);
        if (fabs(A) < 1e-8) {
            printf("%.8lf %.8lf\n", sqrt(fabs(C)), 0.0);
        }
        else {
            double x = -B / A / 2;
            if (x < 0) {
                printf("%.8lf %.8lf\n", sqrt(fabs(C)), 0.0);
            }
            else {
                double ans = A * x * x + B * x + C;
                printf("%.8lf %.8lf\n", sqrt(fabs(ans)), fabs(x));
            }
        }
    }
    return 0;
}
