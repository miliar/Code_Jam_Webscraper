#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

const double eps = 1e-9;

#define uint unsigned int

#define FOR(i, n) for (int i = 0; i < (n); i++)
#define FORU(i, n) for (uint i = 0; i < (n); i++)
#define FORR(i, n) for (int i = (n)-1; i >= 0; i--)
#define FORRU(i, n) for (uint i = (n)-1; i >= 0; i--)
#define FOREACH(it, v) for (__typeof__(v.begin()) it = (v).begin(); it != (v).end(); ++it)

struct Point {       //Punkt mit double-Koordinaten
    double x, y;
    Point(double x=0, double y=0) : x(x), y(y) {}
};

//Darstellung einer Gerade in der Form Ax + By = C
struct Line {
    double A, B, C;
    Line(double a=1, double b=1, double c=0) : A(a), B(b), C(c) {}
};

//Liefert die Gerade durch die zwei verschiedenen Punkte p0 und p1
Line getLine(Point p0, Point p1) {
    double a = p1.y - p0.y, b = p0.x - p1.x;
    return Line(a, b, a * p0.x + b * p0.y);
}

bool intersectLineLine(Line a, Line b, Point *s) {
    double det = a.A * b.B - b.A * a.B;
    if (abs(det) < eps) return false;
    s->x = (a.C * b.B - b.C * a.B) / det;
    s->y = (a.A * b.C - b.A * a.C) / det;
    return true;
}

Line lines[1100];

int main() {
    int cases;
    cin >> cases;

    FOR(tcase, cases) {
        int n;

        cin >> n;

        FOR(i, n) {
            Point a, b;
            cin >> a.y >> b.y;
            a.x = 0;
            b.x = 10000;

            lines[i] = getLine(a, b);
        }

        int sect = 0;
        FOR(i, n) {
            FOR(j, n) {
                if (i == j) continue;
                Point x;
                if (intersectLineLine(lines[i], lines[j], &x)
                        && x.x >= 0 && x.x <= 10000) {
                    sect++;
                }
            }
        }

        printf("Case #%d: %d\n", tcase+1, sect/2);
    }

    return 0;
}
