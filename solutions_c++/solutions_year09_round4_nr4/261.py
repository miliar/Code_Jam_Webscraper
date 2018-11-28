/**********************************************************************
Author: Xay
Created Time:  2009-9-27 1:00:52
File Name: d.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;

typedef long long lint;
const int maxint = 0x7FFFFFFF;
const int maxn = 40 + 10;
const double eps = 1e-9;

struct Point {
    double x, y;
    Point() {}
    Point(double _x, double _y): x(_x), y(_y) {}
    Point turn(const double &m) const {
        return Point(x * cos(m) - y * sin(m), x * sin(m) + y * cos(m));
    }
    Point operator + (const Point &a) const {
        return Point(x + a.x, y + a.y);
    }
    Point operator - (const Point &a) const {
        return Point(x - a.x, y - a.y);
    }
    Point operator * (const double &m) const {
        return Point(x * m, y * m);
    }
    Point operator / (const double &m) const {
        return Point(x / m, y / m);
    }
    double dist() const {
        return x * x + y * y;
    }
    double lenth() const {
        return sqrt(dist());
    }
    Point set(const double &m) const {
        return (*this) * (m / lenth());
    }
    void input() {
        scanf("%lf%lf", &x, &y);
    }
};

int n, len;
Point pt[maxn], cen[maxn * maxn];
double r[maxn];
lint sta[maxn * maxn];

int sgn(double x) {
    return (x > eps) - (x < -eps);
}
void cross(int x1, int x2, double R) {
    double r1 = R - r[x1], r2 = R - r[x2];
    if (sgn((pt[x1] - pt[x2]).lenth() - r1 - r2) > 0) return;
    if (sgn((pt[x1] - pt[x2]).lenth() - r1 - r2) == 0) cen[len++] = pt[x1] + (pt[x2] - pt[x1]).set(r1);
    double angle = acos((r1 * r1 + (pt[x2] - pt[x1]).dist() - r2 * r2) / (2 * (pt[x2] - pt[x1]).lenth() * r1));
    cen[len++] = pt[x1] + (pt[x2] - pt[x1]).turn(angle).set(r1);
    cen[len++] = pt[x1] + (pt[x2] - pt[x1]).turn(-angle).set(r1);
}
bool ok(double R) {
    len = 0;
    for (int i = 0; i < n; ++i) {
        cen[len++] = pt[i];
        for (int j = 0; j < i; ++j) {
            cross(i, j, R);
        }
    }
    for (int i = 0; i < len; ++i) {
        sta[i] = 0;
        for (int j = 0; j < n; ++j) {
            if (sgn((cen[i] - pt[j]).lenth() + r[j] - R) <= 0) {
                sta[i] |= (1LL<<j);
            }
        }
        for (int j = 0; j <= i; ++j) {
            if ((sta[i] | sta[j]) == (1LL<<n) - 1) return true;
        }
    }
    return false;
}
int main()
{
    freopen("d.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        double low = 0, high = 10000;
        for (int i = 0; i < n; ++i) {
            pt[i].input();
            scanf("%lf", &r[i]);
            low = max(low, r[i]);
        }
        double ans = -1;
        while (high - low > 1e-8) {
            double mid = (low + high) * 0.5;
            if (ok(mid)) {
                high = mid;
                ans = mid;
            } else {
                low = mid;
            }
        }
        printf("Case #%d: %.8lf\n", ++ca, ans);
    }
    return 0;
}

