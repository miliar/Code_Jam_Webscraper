#include <iostream>
#include <fstream>
#include <cmath>
std::ifstream fin("input.txt");

int N;
double f, R, t, r, g;

double overlap(double x1, double y1, double x2, double y2, double r) {
    double p1, p2, d1, d2, area = 0;
    if (x1*x1 + y1*y1 >= r*r) return 0;
    if (x2*x2 + y2*y2 < r*r) return (x2-x1)*(y2-y1);
    bool cisin = (x1*x1 + y2*y2 < r*r);

    if (x2*x2 + y1*y1 < r*r) {
        if (cisin) { // 3 inside :(
            p1 = sqrt(r*r-y2*y2); // p1x
            p2 = sqrt(r*r-x2*x2); // p2y
            d1 = atan2(y2, p1);
            d2 = atan2(p2, x2);
            area += r*r*fabs(d1-d2)/2;
            area += .5*y2*p1;
            area += .5*x2*p2;
            area -= (x2-x1)*y1;
            area -= x1*y2;
            return area;
        }
        p1 = sqrt(r*r-x1*x1); // p1y
        p2 = sqrt(r*r-x2*x2); // p2y
        d1 = atan2(p1, x1);
        d2 = atan2(p2, x2);
        area += r*r*fabs(d1-d2)/2;
        area += .5*x2*p2;
        area -= .5*p1*x1;
        area -= (x2-x1)*y1;
        return area;
    }
    if (cisin) {
        p1 = sqrt(r*r-y2*y2); // p1x
        p2 = sqrt(r*r-y1*y1); // p2x
        d1 = atan2(y2, p1);
        d2 = atan2(y1, p2);
        area += r*r*fabs(d1-d2)/2;
        area += .5*y2*p1;
        area -= .5*p2*y1;
        area -= (y2-y1)*x1;
        return area;
    }
    p1 = sqrt(r*r-x1*x1); // p1y
    p2 = sqrt(r*r-y1*y1); // p2x
    d1 = atan2(p1, x1);
    d2 = atan2(y1, p2);
    area += r*r*fabs(d1-d2)/2;
    area += y1*x1;
    area -= .5*p2*y1;
    area -= .5*p1*x1;
    return area;
}

int main() {
    fin >> N;
    for (int i=1; i<=N; i++) {
        fin >> f >> R >> t >> r >> g;
        double step = g + 2*r,
               missa = 0;
        if (f < g-f)
            for (double x=r; x < R; x += step)
            for (double y=r; y < R; y += step)
                missa += overlap(x+f, y+f, x+g-f, y+g-f, R-t-f);
        printf("Case #%i: %.6f\n", i, 1 - 4*missa / (M_PI*R*R));
    }
}

