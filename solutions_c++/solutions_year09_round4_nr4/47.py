#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const double EPS = 1e-8;

struct Point {
	double x, y;
};

inline double xmult(const Point & p1, const Point & p2, const Point & p0) {
	return (p1.x - p0.x) * (p2.y - p0.y) - (p2.x - p0.x) * (p1.y - p0.y);
}

inline double dis(const Point & p1, const Point & p2) {
	return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}

double disptoline(const Point & p, const Point & l1, const Point & l2) {
	return fabs(xmult(p, l1, l2)) / dis(l1, l2);
}

Point intersection(const Point & u1, const Point & u2, const Point & v1, const Point & v2) {
	Point ret = u1;
	double t = ((u1.x - v1.x) * (v1.y - v2.y) - (u1.y - v1.y) * (v1.x - v2.x)) / ((u1.x - u2.x) * (v1.y - v2.y) - (u1.y - u2.y) * (v1.x - v2.x));
	ret.x += (u2.x - u1.x) * t;
	ret.y += (u2.y - u1.y) * t;
	return ret;
}

//判圆和圆相交, 包括相切
int intersectCircleCircle(const Point & c1, double r1, const Point & c2, double r2) {
	return dis(c1, c2) < r1 + r2 + EPS && dis(c1, c2) > fabs(r1 - r2) - EPS;
}

//计算直线与圆的交点, 保证直线与圆有交点
//计算线段与圆的交点可用这个函数后判点是否在线段上
void intersectionLineCircle(const Point & c, double r, const Point & l1, const Point & l2, Point & p1, Point & p2) {
	Point p = c;
	p.x += l1.y - l2.y;
	p.y += l2.x - l1.x;
	p = intersection(p, c, l1, l2);
	double t = sqrt(r * r - dis(p, c) * dis(p, c)) / dis(l1, l2);
	p1.x = p.x + (l2.x - l1.x) * t;
	p1.y = p.y + (l2.y - l1.y) * t;
	p2.x = p.x - (l2.x - l1.x) * t;
	p2.y = p.y - (l2.y - l1.y) * t;
}

//计算圆与圆的交点, 保证圆与圆有交点, 圆心不重合
void intersectionCircleCircle(const Point & c1, double r1, const Point & c2, double r2, Point & p1, Point & p2) {
	Point u, v;
	double t = (1 + (r1 * r1 - r2 * r2) / dis(c1, c2) / dis(c1, c2)) / 2;
	u.x = c1.x + (c2.x - c1.x) * t;
	u.y = c1.y + (c2.y - c1.y) * t;
	v.x = u.x + c1.y - c2.y;
	v.y = u.y - c1.x + c2.x;
	intersectionLineCircle(c1, r1, u, v, p1, p2);
}

const int MAXN = 128;
Point c[MAXN];
double r[MAXN];

bool good(int n, double rr) {
	Point p1, p2;
	vector<Point> cs;
	for (int i = 0; i < n; ++i) {
		cs.push_back(c[i]);
		for (int j = i + 1; j < n; ++j) {
			if (intersectCircleCircle(c[i], rr - r[i], c[j], rr - r[j])) {
				intersectionCircleCircle(c[i], rr - r[i], c[j], rr - r[j], p1, p2);
				cs.push_back(p1);
				cs.push_back(p2);
			}
		}
	}
	int m = cs.size();

	for (int i = 0; i < m; ++i) {
		for (int j = i + 1; j < m; ++j) {
			bool flag = true;
			for (int k = 0; flag && k < n; ++k) {
				if (dis(c[k], cs[i]) > rr - r[k] + 5e-7 && dis(c[k], cs[j]) > rr - r[k] + 5e-7) {
					flag = false;
				}
			}
			if (flag) {
				return true;
			}
		}
	}
	return false;
}

int main() {
	int re, n;
	double left, right, mid;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d", &n);
		left = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%lf%lf%lf", &c[i].x, &c[i].y, &r[i]);
			left = max(left, r[i]);
		}
		if (n == 1) {
			mid = r[0];
			goto ONE;
		}
		right = 1000;
		for (int i = 0; i < 50; ++i) {
			mid = (left + right) / 2;
			if (good(n, mid)) {
				right = mid;
			} else {
				left = mid;
			}
		}
		mid = (left + right) / 2;
ONE:
		printf("Case #%d: %.7lf\n", ri, mid);
		fflush(stdout);
	}

	return 0;
}

