#include <cstdio>
#include <cmath>
using namespace std;
#ifndef M_PI
#define M_PI (2*acos(0))
#endif
const double EXP = 1e-12;
double Face(const double &x1, const double &y1,
        const double &g, const double &R)
{
    bool up, right;
    double x2, y2, x3, y3, x4, y4;
    double angle;
    x2 = x1 + g, y2 = y1 + g;
    up = (x1*x1+y2*y2 <= R*R);
    right = (x2*x2+y1*y1 <= R*R);
    if ((!up) && (!right)) {
        x3 = x1, y3 = sqrt(R * R - x3 * x3);
        y4 = y1, x4 = sqrt(R * R - y4 * y4);
        angle = fabs(acos((x3*x4+y3*y4)/(R*R)));
        return (y3-y1)*(x4-x1)*0.5 + R*R*(angle-sin(angle))*0.5;
    }
    else if (up && right) {
        x3 = x2, y3 = sqrt(R * R - x3 * x3);
        y4 = y2, x4 = sqrt(R * R - y4 * y4);
        angle = fabs(acos((x3*x4+y3*y4)/(R*R)));
        return g*g - (y2-y3)*(x2-x4)*0.5 + R*R*(angle-sin(angle))*0.5;
    }
    else if ((!up) && right) {
        x3 = x1, y3 = sqrt(R * R - x3 * x3);
        x4 = x2, y4 = sqrt(R * R - x4 * x4);
        angle = fabs(acos((x3*x4+y3*y4)/(R*R)));
        return g*(y3-y1+y4-y1)*0.5 + R*R*(angle-sin(angle))*0.5;
    }
    else {
        y3 = y1, x3 = sqrt(R * R - y3 * y3);
        y4 = y2, x4 = sqrt(R * R - y4 * y4);
        angle = fabs(acos((x3*x4+y3*y4)/(R*R)));
        return g*(x3-x1+x4-x1)*0.5 + R*R*(angle-sin(angle))*0.5;
    }
}
double Hole(const double &R, const double &r, const double &g)
{
    double res = 0.0;
    double inc = g + 2*r;
    double sqrG, sqrR, sqrY, sqrYt;
    double xt, yt;
    sqrR = R * R, sqrG = g * g;
    for (double x = r; x < R; x += inc) {
        sqrY = sqrR - x * x - EXP;
        xt = x + g, sqrYt = sqrR - xt * xt + EXP;
        for (double y = r; y*y < sqrY; y += inc) {
            yt = y + g;
            if (yt * yt <= sqrYt) {
                res += sqrG;
            }
            else {
                res += Face(x, y, g, R);
            }
        }
    }
    return 4 * res;
}
void Process(const int &cas)
{
    double R, r, t, g, f;
    scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
    t = R - t - f;
    r += f, g -= 2*f;
    if (g <= EXP) {
        printf("Case #%d: %.6lf\n", cas, 1.0);
    }
    else {
        double tot = M_PI * R * R;
        double space = Hole(t, r, g);
        printf("Case #%d: %.6lf\n", cas, 1.0 - space / tot);
    }
}
int main()
{
    int cas;
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    scanf("%d", &cas);
    for (int t = 1; t <= cas; t++)
        Process(t);
    return 0;
}
