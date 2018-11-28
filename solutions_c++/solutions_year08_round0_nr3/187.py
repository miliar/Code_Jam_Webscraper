#include <cstdio>
#include <cmath>

int T;
double f, R, t, r, g, x, y, a;

double area1(double y1, double y2, double r) {
        double a = r*r*(acos(y1/r) - acos(y2/r));
        return (a + y2*sqrt(r*r - y2*y2) - y1*sqrt(r*r - y1*y1))/2;
}

double area(double x1, double x2, double y1, double y2, double r) {
//      printf("\narea %lf %lf %lf %lf %lf\n", x1, y1, x2, y2, r);
        if (x2*x2 + y2*y2 <= r*r)
                return (x2 - x1)*(y2 - y1);
        if (x1*x1 + y2*y2 <= r*r && x2*x2 + y1*y1 <= r*r) {
                double t = sqrt(r*r - y2*y2);
                return (t - x1)*(y2 - y1) + area1(t, x2, r) - y1*(x2 - t);
        }
        if (x1*x1 + y2*y2 <= r*r)
                return area1(y1, y2, r) - x1*(y2 - y1);
        if (x2*x2 + y1*y1 <= r*r)
                return area1(x1, x2, r) - y1*(x2 - x1);
        double t = sqrt(r*r - x1*x1);
//      printf("t = %lf\n", t);
        return area1(y1, t, r) - x1*(t - y1);
        return 0;
}

int main() {
        scanf("%d", &T);
        for (int k = 1; k <= T; ++k) {
                printf("Case #%d: ", k);
                scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
                if (g <= 2*f) {
                        puts("1.000000");
                        continue;
                }
                g -= 2*f;
                r += f;
                a = R*R*acos(0)*2;
                R -= t + f;
                t = 0;
                for (x = r; x < R; x += g + 2*r)
                        for (y = r; x*x + y*y < R*R; y += g + 2*r) {
                                double z = area(x, x + g, y, y + g, R);
//                              printf("%lf\n", z);
                                t += z;
                        }
                printf("%.6lf\n", 1 - 4*t/a);
        }
        return 0;
}
