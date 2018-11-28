#include <iostream>
#include <cstdio>
#include <complex>
#include <cmath>
#include <cassert>

using namespace std;
typedef complex<double> Point;

const double PI = atan(1.) * 4.;

double solve(double Y, double R)
{
    if (R < Y) return -1.0;
    double d = R * R - Y * Y;
    if (d < 0.) d = 0.;
    return sqrt(d);
}

double hmarea(Point p1, Point p2, double R)
{
    double theta = arg(p2) - arg(p1);
    assert(theta >= 0.);

    return R * R * (theta - sin(theta)) / 2.;
}

template <typename T>
bool range(T x, T a, T y)
{
    return x <= a && a <= y;
}

double area(double x, double y, double len, double R, double f)
{
    len -= f + f;
    if (len < 0.0) return 0.0;
    x += f;
    y += f;

    double botx = solve(y, R);
    double topx = solve(y + len, R);
    double lefty = solve(x, R);
    double righty = solve(x + len, R);

    if (range(x, topx, x + len) && range(y, righty, y + len)) {
        double w1 = topx - x;
        double w2 = x + len - topx;
        double h1 = righty - y;
        return w1 * len + (len + h1) * w2 / 2.
            + hmarea(Point(x + len, righty), Point(topx, y + len), R);
    }

    if (range(x, botx, x + len) && range(y, lefty, y + len)) {
        double w1 = botx - x;
        double h1 = lefty - y;
        return w1 * h1 / 2. + hmarea(Point(botx, y), Point(x, lefty), R);
    }

    if (range(x, botx, x + len) && range(x, topx, x + len)) {
        double w1 = topx - x;
        double w2 = botx - topx;
        return (w1 + w1 + w2) * len / 2.
            + hmarea(Point(botx, y), Point(topx, y + len), R);
    }

    if (range(y, lefty, y + len) && range(y, righty, y + len)) {
        double h1 = righty - y;
        double h2 = lefty - righty;
        return (h1 + h1 + h2) * len / 2.
            + hmarea(Point(x + len, righty), Point(x, lefty), R);
    }

    if (x + len - 1e-6 <= topx)
        return len * len;

    return 0.;
}

int main()
{
    int cases;
    cin >> cases;

    for (int cs = 0; cs < cases; ++cs) {
        double f, R, t, r, g;
        cin >> f >> R >> t >> r >> g;

        double ir = R - t - f;
        if (ir < 0.) ir = 0.;

        double all = PI * R * R / 4.;
        double ar = 0.;
        for (double x = r; x <= R; x += g + r + r) {
            for (double y = r; y <= R; y += g + r + r) {
                double dar = area(x, y, g, ir, f);
                ar += dar;
            }
        }
        printf("Case #%d: %.6f\n", cs + 1, 1. - ar / all);
    }

    return 0;
}
