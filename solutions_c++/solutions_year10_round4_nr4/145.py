#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
using namespace std;

const double eps = 1e-8;
const double pi = acos(-1.0);

const int dx[4] = {
    1, 0, -1, 0
};

const int dy[4] = {
    0, -1, 0, 1
};

int dcmp(double x) {
    return (x > +eps) - (x < -eps);
}

struct point {
    double x, y;
    point() {}
    point(double _x, double _y) : x(_x), y(_y) {}
    point operator + (const point& p) const {
        return point(x + p.x, y + p.y);
    }
    point operator - (const point& p) const {
        return point(x - p.x, y - p.y);
    }
    point operator * (double p) const {
        return point(x * p, y * p);
    }
    point operator / (double p) const {
        return point(x / p, y / p);
    }
    point trun_left() const {
        return point(-y, x);
    }
    point trun_right() const {
        return point(y, -x);
    }
    point rotate(double a) const {
        return point(x * cos(a) - y * sin(a), x * sin(a) + y * cos(a));
    }
    point trunc(double len) const {
        return *this * len / sqrt(x * x + y * y);
    }
    bool operator < (const point& p) const {
        return dcmp(x - p.x) < 0 || (dcmp(x - p.x) == 0 && dcmp(y - p.y) < 0);
    }
    bool operator ==(const point& p) const {
        return dcmp(x - p.x) == 0 && dcmp(y - p.y) == 0;
    }
    bool operator !=(const point& p) const {
        return dcmp(x - p.x) != 0 || dcmp(y - p.y) != 0;
    }
};

double xmul(const point& a, const point& b) {
    return a.x * b.y - a.y * b.x;
}

double xmul(const point& a, const point& b, const point& c) {
    return xmul(b - a, c - a);
}

double dmul(const point& a, const point& b) {
    return a.x * b.x + a.y * b.y;
}

double dmul(const point& a, const point& b, const point& c) {
    return dmul(b - a, c - a);
}

double dist(const point& a, const point& b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

struct Circle {
    double x, y, r;
    Circle() {}
    Circle(double _x, double _y, double _r) : x(_x), y(_y), r(_r) {}
    bool operator ==(const Circle& c) const {
        return dcmp(x - c.x) == 0 && dcmp(y - c.y) == 0 && dcmp(r - c.r) == 0;
    }
};

struct hu_node {
    point a, b;
    int i;
    hu_node() {}
    hu_node(const point& _a, const point& _b, int _i) {
        a = _a, b = _b;
        i = _i;
    }
};

struct cmp {
    point c;
    cmp() {}
    cmp(const point& c) : c(c) {}
    bool operator () (const point& a, const point& b) {
        return dcmp(atan2(a.y - c.y, a.x - c.x) - atan2(b.y - c.y, b.x - c.x)) < 0;
    }
};

bool circle_intersection(const Circle& s, const Circle& t, point& a, point& b) {
    point cs = point(s.x, s.y), ct = point(t.x, t.y);
    double dd = dist(cs, ct);
    if (dcmp(dd - (s.r + t.r)) > 0) {
        return false;
    }
    if (dcmp(dd - fabs(s.r - t.r)) < 0) {
        return false;
    }
    double x1 = (dd * dd + s.r * s.r - t.r * t.r) / dd / 2;
    double y1 = sqrt(s.r * s.r - x1 * x1);
    point mid = cs + (ct - cs).trunc(x1);
    a = mid + ((ct - cs).trun_right()).trunc(y1);
    b = mid + ((ct - cs).trun_left()).trunc(y1);
    if (dcmp(xmul(cs, a, b)) < 0) { // 保证a->b在圆s上逆时针方向
        swap(a, b);
    }
    return true;
}

bool in_hu(const point& p, const point& a, const point& b, const point& c) {
	return dcmp(dmul(p, a, b)) <= 0;
}

deque<point> hu_intersection(const point& a, const point& b, const Circle& s, const Circle& t) {
    point x, y;
    deque<point> it;
    if (circle_intersection(s, t, x, y)) {
        if (in_hu(x, a, b, point(s.x, s.y))) it.push_back(x);
        if (in_hu(y, a, b, point(t.x, t.y))) it.push_back(y);
    }
    return it;
}

double hu_area(const point& a, const point& b, double r) {
    double d = dist(a, b);
    double alpha = 2 * asin(d / r / 2);
    return (alpha - sin(alpha)) * r * r / 2;
}

bool in_circle(const point& p, const Circle& c) {
    return dcmp(dist(p, point(c.x, c.y)) - c.r) < 0;
}

bool check_hu(const point& a, const point& b, const Circle& p, const Circle& t) {
    point c = point(p.x, p.y);
    point mid = c + (b - a).trun_right().trunc(p.r);
    return in_circle(mid, t);
}

vector<double> calc_area(const vector<Circle>& in) {
    vector<double> ans(in.size(), 0);
    if (in.size() == 0) {
        return ans;
    }
    vector<hu_node> hu;//弧是逆时针保存
    for (int i = 0; i < in.size(); ++i) {
        bool ok = true;
        for (int j = 0; ok && j < i; ++j) {
            if (in[j] == in[i]) {
                ok = false;
            }
        }
        if (!ok && i > 0) {
            ans[i] = ans[i - 1];
            continue;
        }
        vector<point> on_circle;
        for (int j = 0; j < 4; ++j) {
            on_circle.push_back(point(in[i].x, in[i].y) + point(dx[j], dy[j]) * in[i].r);
        }
        vector<hu_node> tmp;
        for (int j = 0; j < hu.size(); ++j) {
            deque<point> it = hu_intersection(hu[j].a, hu[j].b, in[hu[j].i], in[i]);
            for (int k = 0; k < it.size(); ++k) {
                on_circle.push_back(it[k]);
            }
            it.push_front(hu[j].a), it.push_back(hu[j].b);
            for (int k = 0; k < it.size() - 1; ++k) {
                if (check_hu(it[k], it[k + 1], in[hu[j].i], in[i])) {
                    if (it[k] != it[k + 1]) {
                        tmp.push_back(hu_node(it[k], it[k + 1], hu[j].i));
                    }
                }
            }
        }
        hu = tmp;
        point c = point(in[i].x, in[i].y);
        sort(on_circle.begin(), on_circle.end(), cmp(c));
        on_circle.erase(unique(on_circle.begin(), on_circle.end()), on_circle.end());
        for (int j = 0; j < on_circle.size(); ++j) {
            int next = (j + 1) % on_circle.size();
            point a = on_circle[j], b = on_circle[next];
            bool flag = true;
            for (int k = 0; flag && k < i; ++k) {
                if (check_hu(a, b, in[i], in[k]) == false) {
                    flag = false;
                }
            }
            if (flag) {
                hu.push_back(hu_node(a, b, i));
            }
        }
        if (hu.size() == 0) {
            break;
        }
        ans[i] = 0;
        for (int j = 0; j < hu.size(); ++j) {
            ans[i] += hu_area(hu[j].a, hu[j].b, in[hu[j].i].r);
            ans[i] += xmul(hu[j].a, hu[j].b) / 2.0;
        }
    }
    return ans;
}

int main() {
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    int tt = 0, ca = 1;
    scanf("%d", &tt);
    while (tt--) {
        //fprintf(stderr, "%d\n", tt);
        int n, m;
        scanf("%d %d", &n, &m);
        vector<point> pt(n), dt(m);
        for (int i = 0; i < n; ++i) {
            scanf("%lf %lf", &pt[i].x, &pt[i].y);
        }
        for (int i = 0; i < m; ++i) {
            scanf("%lf %lf", &dt[i].x, &dt[i].y);
        }
        vector<double> ans;
        for (int i = 0; i < m; ++i) {
            vector<Circle> in;
            for (int j = 0; j < n; ++j) {
                double rr = dist(pt[j], dt[i]);
                in.push_back(Circle(pt[j].x, pt[j].y, rr));
            }
            vector<double> res = calc_area(in);
            //for (int j = 0; j < res.size(); ++j) {
                //printf("%lf ", res[j]);
            //}
            //printf("\n");
            ans.push_back(res[n - 1]);
        }
        printf("Case #%d:", ca++);
        for (int i = 0; i < ans.size(); ++i) {
            printf(" %.10lf", ans[i]);
        }
        printf("\n");
    }
    return 0;
}

