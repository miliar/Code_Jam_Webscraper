#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>

using namespace std;

double X, Y;
struct Point {
    double x, y;

    Point() {}
    Point(double x, double y) {
        this->x = min(X, max(0.0, x));
        this->y = min(Y, max(0.0, y));
    }

    void clear() {
        x = y = 0;
    }

    Point operator+(const Point &o) const {
        return Point(x + o.x, y + o.y);
    }

    Point operator-(const Point &o) const {
        return Point(x - o.x, y - o.y);
    }

    Point operator*(double a) const {
        return Point(x * a, y * a);
    }
};

const double inv = 1.0 / 65535.0;

double nextRand() {
    return (rand() & 65535) * inv;
}

int n;
Point pts[1024];
Point delta[1024];
double R[1024];

int main()
{
    srand(time(0));
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%lf%lf", &n, &X, &Y);
        for (int i = 0; i < n; i++)
            scanf("%lf", R+i);
        int times = 1000;
        while (true) {
            for (int i = 0; i < n; i++) {
                pts[i].x = nextRand() * X;
                pts[i].y = nextRand() * Y;
            }
            bool okay = false;
            for (int it = 0; it < times; ++it) {
                bool found = false;
                for (int i = 0; i < n; i++)
                    for (int j = 0; j < i; j++) {
                        double dis = hypot(pts[i].x - pts[j].x, pts[i].y - pts[j].y);
                        if (dis < R[i] + R[j] + 0.1) {
                            found = true;
                            Point delta = (pts[i] - pts[j]) * 0.51;
                            pts[i] = pts[i] + delta;
                            pts[j] = pts[j] - delta;
                        }
                    }
                if (!found) {
                    okay = true;
                    break;
                }
            }
            if (okay) {
                break;
            }
        }
        printf("Case #%d: ", ++ cas);
        for (int i = 0; i < n; i++)
            printf(" %.10lf %.10lf", pts[i].x, pts[i].y);
        puts("");
    }
}
