#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <vector>

#define EPS 1e-09

using namespace std;

const double PI = acos(-1.0);

struct Point {
    double x, y;

    Point () {
        this->x = x;
        this->y = y;
    }

    Point (double x, double y) {
        this->x = x;
        this->y = y;
    }
};

double dist(Point a, Point b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

double cross(Point p1, Point p2, Point p3) {
    assert((p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y) >= 0);
    return (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y);
}

double intersect(double R, double x1, double x2, double y1, double y2) {
    if (x1 * x1 + y1 * y1 >= R * R) {
        return 0;
    }

    if (x2 * x2 + y2 * y2 <= R * R) {
        return (x2 - x1) * (y2 - y1);
    }

    Point a, b;
    vector <Point> p;
    p.push_back(Point(x1, y1));
    if (x2 * x2 + y1 * y1 >= R * R) {
        double tx = sqrt(R * R - y1 * y1);
        a = Point(tx, y1);
        p.push_back(a);
    }
    else {
        double ty = sqrt(R * R - x2 * x2);
        a = Point(x2, ty);
        p.push_back(Point(x2, y1));
        p.push_back(a);
    }
    if (x1 * x1 + y2 * y2 >= R * R) {
        double ty = sqrt(R * R - x1 * x1);
        b = Point(x1, ty);
        p.push_back(b);
    }
    else {
        double tx = sqrt(R * R - y2 * y2);
        b = Point(tx, y2);
        p.push_back(b);
        p.push_back(Point(x1, y2));
    }

    double area = 0;
    for (unsigned i = 1; i + 1 < p.size(); i++) {
        area += cross(p[0], p[i], p[i + 1]) / 2;
    }

    double angle = asin(dist(a, b) / (2 * R));

    return area + angle * R * R - cross(Point(0, 0), a, b) / 2;
}

double calcMissArea(double R, double S, double W) {
    double gridSize = S + 2 * W;
    double x = 0;
    double y = floor(R / gridSize) * gridSize;
    double result = 0;
    while (y >= -EPS) {
        //assert(x * x + y * y <= R * R);
        //assert((x + gridSize) * (x + gridSize) + (y + gridSize) * (y + gridSize) >= R * R);
        result += intersect(R, x + W, x + W + S, y + W, y + W + S);

        double distNext = (x + gridSize) * (x + gridSize) + y * y;
        if (distNext <= R * R) {
            x += gridSize;
            result += y * gridSize * S * S / (gridSize * gridSize);
        }
        else {
            y -= gridSize;
        }
    }
    return 4 * result;
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        double f, R, t, r, g;
        scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
        fprintf(stderr, "TEST: %d\n", test);
        f = min(g / 2, f);
        double miss = calcMissArea(R - t - f, g - 2 * f, r + f);
        double total = PI * R * R;
        printf("Case #%d: %lf\n", test + 1, 1 - miss / total);
    }
    return 0;
}
