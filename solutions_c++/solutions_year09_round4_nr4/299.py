/*
 * Author: momodi
 * Created Time:  2009/9/26 23:52:31
 * File Name: c.cpp
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define out(x) fprintf(stderr, "%s: %I64d\n", #x, (long long)(x))
#define SZ(v) ((int)(v).size())
const int maxint=-1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
#define SQR(v) ((v) * (v))
const double eps = 1e-9;
const double pi = acos(-1.0);

int sgn(const double &a) {
    return (a > eps) - (a < -eps);
}

const int zx[] = {
    0, 1, 0, -1
};
const int zy[] = {
    1, 0, -1, 0
};

struct P {
    double x, y;
    P(const double &_x, const double &_y)
        :x(_x), y(_y) {}
    P() {}
    bool operator == (const P &a) const {
        return sgn(x - a.x) == 0 && sgn(y - a.y) == 0;
    }
    P operator + (const P &a) const {
        return P(x + a.x, y + a.y);
    }
    P operator - (const P &a) const {
        return P(x - a.x, y - a.y);
    }
    P operator * (const double &a) const {
        return P(x * a, y * a);
    }
    P operator / (const double &a) const {
        return P(x / a, y / a);
    }
    P trunc(double a) const {
        a /= sqrt(SQR(x) + SQR(y));
        return P(x * a, y * a);
    }
    P turn_left() const {
        return P(-y, x);
    }
    P turn_right() const {
        return P(y, -x);
    }
    const P& input() {
        scanf("%lf %lf", &x, &y);
        return *this;
    }
    const P& output() const {
        printf("P: %.12lf %.12lf\n", x, y);
        return *this;
    }
};

double dist2(const P &a, const P &b) {
    return SQR(a.x - b.x) + SQR(a.y - b.y);
}
double dist(const P &a, const P &b) {
    return sqrt(SQR(a.x - b.x) + SQR(a.y - b.y));
}
double cross(const P &a, const P &b, const P &c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}
double dmul(const P &a, const P &b, const P &c) {
    return (b.x - a.x) * (c.x - a.x) + (b.y - a.y) * (c.y - a.y);
}

struct C {
    P mid;
    double r;
    C(const P &_mid, const double &_r)
        :mid(_mid), r(_r) {}
    C() {}
    bool operator == (const C &a) const {
        return mid == a.mid && sgn(r - a.r) == 0;
    }
    bool in(const C &a) const {
        return sgn(r + dist(mid, a.mid) - a.r) < 0;
    }
    const C &input() {
        mid.input();
        scanf("%lf", &r);
        return *this;
    }
    const C &output() const {
        printf("P: %.12lf %.12lf R: %.12lf\n", mid.x, mid.y, r);
    }
};
C c[100];
int n;
#define move(v) (1ll << (v))
bool find(C a, C b, P &tmp, double mid) {
    double d = dist(a.mid, b.mid);
    if (sgn(d + a.r + b.r - mid * 2) == 0) {
        tmp = (a.mid + (a.mid - b.mid).trunc(a.r) + b.mid + (b.mid - a.mid).trunc(b.r)) / 2;
        return true;
    } else if (sgn(d + a.r + b.r - mid * 2) > 0) {
        return false;
    }
    double p = mid - a.r;
    double q = mid - b.r;
    double z = SQR(p) - SQR(q);
    double x = (d + z / d) / 2;
    double y = d - x;
    tmp = (a.mid * y + b.mid * x) / d + (a.mid - b.mid).turn_left().trunc(sqrt(SQR(p) - SQR(x)));
    return true;
}

bool ok(double mid) {
    for (int i = 0; i < n; ++i) {
        if (sgn(c[i].r - mid) > 0) {
            return false;
        }
    }
    vector<long long> ans;
    for (int i = 0; i < n; ++i) {
        ans.push_back(move(i));
        for (int j = 0; j < n; ++j) {
            if (i == j) {
                continue;
            }
            P tmp(0, 0);
            if (find(c[i], c[j], tmp, mid)) {
                long long cc = 0;
                for (int k = 0; k < n; ++k) {
                    if (sgn(dist(tmp, c[k].mid) + c[k].r - mid) <= 0) {
                        cc |= move(k);
                    }
                }
//                tmp.output();
//                out(cc);
                ans.push_back(cc);
            }
        }
    }
    for (int i = 0; i < SZ(ans); ++i) {
        for (int j = i; j < SZ(ans); ++j) {
            if ((ans[i] | ans[j]) == move(n) - 1) {
                return true;
            }
        }
    }
    return false;
}

double solve() {
    double s = 0, t = 1e5;
    while (t - s > 1e-7) {
        double mid = (s + t) / 2;
//        printf("%lf\n", mid);
        if (ok(mid)) {
            t = mid;
        } else {
            s = mid;
        }
//        break;
    }
    return (s + t) / 2;
}

int main() {
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            c[i].input();
        }
        printf("%.7lf\n", solve());
    }
    return 0;
}

