/*
 * Author: momodi
 * Created Time:  2010/6/5 23:26:57
 * File Name: d.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
#define SQR(v) ((v) * (v))
const long double eps = 1e-8;
const long double pi = acos(-1.0);
int NEXT(int i, int n) {
    return i % n;
}

int sgn(const long double &a) {
    return (a > eps) - (a < -eps);
}

const int zx[] = {
    0, 1, 0, -1
};
const int zy[] = {
    1, 0, -1, 0
};

struct P {
    long double x, y;
    P(const long double &_x, const long double &_y)
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
    P operator * (const long double &a) const {
        return P(x * a, y * a);
    }
    P operator / (const long double &a) const {
        return P(x / a, y / a);
    }
    P trunc(long double a) const {
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
        cin >> x >> y;
        return *this;
    }
    const P& output() const {
        printf("P: %.12lf %.12lf\n", x, y);
        return *this;
    }
};

long double dist2(const P &a, const P &b) {
    return SQR(a.x - b.x) + SQR(a.y - b.y);
}
long double dist(const P &a, const P &b) {
    return sqrt(SQR(a.x - b.x) + SQR(a.y - b.y));
}
long double cross(const P &a, const P &b, const P &c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}
long double dmul(const P &a, const P &b, const P &c) {
    return (b.x - a.x) * (c.x - a.x) + (b.y - a.y) * (c.y - a.y);
}

struct C {
    P mid;
    long double r;
    C(const P &_mid, const long double &_r)
        :mid(_mid), r(_r) {}
    C() {}
    bool operator == (const C &a) const {
        return mid == a.mid && sgn(r - a.r) == 0;
    }
    bool operator != (const C &a) const {
        if (mid == a.mid && sgn(r - a.r) == 0) {
            return false;
        }
        return true;
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

long double cal_angle(const C &c, const P &a, const P &b) {
    long double k = dmul(c.mid, a, b) / SQR(c.r);
    get_min(k, (long double)1.0);
    get_max(k, (long double)-1.0);
    return acos(k);
}

long double cal_area(const C &c, const P &a, const P &b) {
    return SQR(c.r) * cal_angle(c, a, b) / 2 - cross(c.mid, a, b) / 2;
}

struct cmp {
    P mid;
    cmp(const P &_mid)
        :mid(_mid) {}
    bool operator () (const P &a, const P &b) {
        return atan2(a.y - mid.y, a.x - mid.x) < atan2(b.y - mid.y, b.x - mid.x);
    }
};

bool circles_intersection(const C &a, const C &b, P &c1, P &c2) {
    long double dd = dist(a.mid, b.mid);
    if (sgn(dd - (a.r + b.r)) >= 0) {
        return false;
    }
    long double l = (dd + (SQR(a.r) - SQR(b.r)) / dd) / 2;
    long double h = sqrt(SQR(a.r) - SQR(l));
    c1 = a.mid + (b.mid - a.mid).trunc(l) + (b.mid - a.mid).turn_left().trunc(h);
    c2 = a.mid + (b.mid - a.mid).trunc(l) + (b.mid - a.mid).turn_right().trunc(h);
    return true;
}

bool cover(const C &c, const P &a, const P &b, const vector<C> &cir) {
    P p = c.mid + ((a + b) / 2 - c.mid).trunc(c.r);
    for (vector<C>::const_iterator it = cir.begin(); it != cir.end(); ++it) {
        if (c != *it && sgn(dist2(p, it->mid) - SQR(it->r)) >= 0) {
            return false;
        }
    }
    return true;
}

long double cal_area(const vector<C> &in) {
    vector<C> cir;
    for (int i = 0; i < SZ(in); ++i) {
        if (sgn(in[i].r == 0)) {
            continue;
        }
        bool flag = false;
        for (int j = i + 1; j < SZ(in); ++j) {
            if (in[i] == in[j]) {
                flag = true;
                break;
            }
        }
        if (flag) {
            continue;
        }
        for (int j = 0; j < SZ(in); ++j) {
            if (i != j && in[i].in(in[j])) {
                flag = true;
                break;
            }
        }
        if (flag) {
            continue;
        }
        cir.push_back(in[i]);
    }
    vector<vector<P> > point_on_circle(SZ(cir));
    for (int i = 0; i < SZ(cir); ++i) {
        for (int z = 0; z < 4; ++z) {
            point_on_circle[i].push_back(cir[i].mid + P(zx[z], zy[z]).trunc(cir[i].r));
        }
    }
    for (int i = 0; i < SZ(cir); ++i) {
        for (int j = i + 1; j < SZ(cir); ++j) {
            P a, b;
            if (circles_intersection(cir[i], cir[j], a, b)) {
                point_on_circle[i].push_back(a);
                point_on_circle[i].push_back(b);
                point_on_circle[j].push_back(a);
                point_on_circle[j].push_back(b);
            }
        }
    }
    for (int i = 0; i < SZ(cir); ++i) {
        sort(point_on_circle[i].begin(), point_on_circle[i].end(), cmp(cir[i].mid));
        point_on_circle[i].erase(unique(point_on_circle[i].begin(), point_on_circle[i].end()), point_on_circle[i].end());
    }
    long double ans = 0;
    for (int i = 0; i < SZ(cir); ++i) {
        for (int j = 0; j < SZ(point_on_circle[i]); ++j) {
            const P &a = point_on_circle[i][j];
            const P &b = point_on_circle[i][NEXT(j + 1, SZ(point_on_circle[i]))];
            if (cover(cir[i], a, b, cir)) {
                ans += cross(P(0, 0), a, b) / 2;
                ans += cal_area(cir[i], a, b);
            }
        }
    }
    return ans;
}
long double mabs(long double a) {
    return a;
}

int main() {
    freopen("d.out", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        int n, m;
        scanf("%d %d", &n, &m);
        vector<C> c(n);
        for (int i = 0; i < n; ++i) {
            c[i].mid.input();
        }
        for (int i = 0; i < m; ++i) {
            P now;
            now.input();
            for (int j = 0; j < n; ++j) {
                c[j].r = dist(now, c[j].mid);
            }
            printf("%.7f ", (double)cal_area(c));
        }
        puts("");
    }
    return 0;
}

