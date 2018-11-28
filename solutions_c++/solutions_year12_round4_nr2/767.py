#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define SQR(x) ((x) * (x))
const int maxint = -1u>>1;
const int maxn = 1000 + 5;
const double eps = 1e-8;
int sgn(double x) {
    return (x > eps) - (x < -eps);
}

struct P {
    double x, y;
    P(double _x = 0, double _y = 0): x(_x), y(_y) {}
    P operator + (const P &a) const {
        return P(x + a.x, y + a.y);
    }
    P operator - (const P &a) const {
        return P(x - a.x, y - a.y);
    }
    P operator * (const double &m) const {
        return P(x * m, y * m);
    }
    P operator / (const double &m) const {
        return P(x / m, y / m);
    }
    P set(const double &m) const {
        double len = get_length();
        return P(x * m / len, y * m / len);
    }
    double get_dist(const P &a) const {
        return sqrt(SQR(x - a.x) + SQR(y - a.y));
    }
    double get_length() const {
        return sqrt(SQR(x) + SQR(y));
    }
    void random(int w, int l) {
        x = ((rand() << 15) | rand()) % w;
        y = ((rand() << 15) | rand()) % l;
    }
    void output() const {
        printf("%lf %lf\n", x, y);
    }
};

int n, w, l;
double r[maxn];
P pt[maxn];

bool ok(int x, const P &p) {
    for (int i = 0; i < x; ++i) {
        if (sgn(p.x - pt[i].x) == 0 && sgn(p.y - pt[i].y) == 0) return false;
    }
    return true;
}

int main() {
    freopen("b.out", "w", stdout);
    srand(19900709);
    int ca = 0, t;
    scanf("%d", &t);
    while (scanf("%d", &n) == 1) {
        printf("Case #%d:", ++ca);
        scanf("%d%d", &w, &l);
        for (int i = 0; i < n; ++i) {
            scanf("%lf", &r[i]);
        }
        while (true) {
            bool flag = true;
            for (int i = 0; i < n; ++i) {
                pt[i].random(w, l);
            }
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < i; ++j) {
                    double d = pt[i].get_dist(pt[j]);
                    if (sgn(r[i] + r[j] - d) > 0) {
                        flag = false;
                        goto OUT;
                    }
                }
            }
OUT:;
            if (flag) break;
        }
        for (int i = 0; i < n; ++i) {
            printf(" %.12lf %.12lf", pt[i].x, pt[i].y);
        }
        printf("\n");
    }
    return 0;
}

