#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

const double EPS = 1e-7;
struct Point {
    double x, y;
}c1, c2;
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
      double t = ((u1.x - v1.x) * (v1.y - v2.y) - (u1.y - v1.y) * (v1.x - v2.x)) / ((
u1.x - u2.x) * (v1.y - v2.y) - (u1.y - u2.y) * (v1.x - v2.x));
      ret.x += (u2.x - u1.x) * t;
      ret.y += (u2.y - u1.y) * t;
      return ret;
}
//判直线和圆相交, 包括相切
int intersectLineCircle(const Point & c, double r, const Point & l1, const Point &
l2) {
      return disptoline(c, l1, l2) < r + EPS;
}
//判线段和圆相交, 包括端点和相切
int intersectSegCircle(const Point & c, double r, const Point & l1, const Point & l2) {
      double t1 = dis(c, l1) - r, t2 = dis(c, l2) - r;
      Point t = c;
      if (t1 < EPS || t2 < EPS) {
          return t1 > -EPS || t2 > -EPS;
      }
      t.x += l1.y - l2.y;
      t.y += l2.x - l1.x;
      return xmult(l1, c, t) * xmult(l2, c, t) < EPS && disptoline(c, l1, l2) - r < EPS;
}
//判圆和圆相交, 包括相切
bool intersectCircleCircle(const Point & c1, double r1, const Point & c2, double r2)
  {
      return dis(c1, c2) < r1 + r2 + EPS && dis(c1, c2) > fabs(r1 - r2) - EPS;
}
//计算圆上到点 p 最近点, 如 p 与圆心重合, 返回 p 本身
Point dotToCircle(const Point & c, double r, const Point & p) {
      Point u, v;
      if (dis(p, c)<EPS) {
          return p;
     }
     u.x = c.x + r * fabs(c.x - p.x) / dis(c, p);
     u.y = c.y + r * fabs(c.y - p.y) / dis(c, p) * ((c.x - p.x) * (c.y - p.y) < 0 ?
-1 : 1);
     v.x = c.x - r * fabs(c.x - p.x) / dis(c, p);
     v.y = c.y - r * fabs(c.y - p.y) / dis(c, p) * ((c.x - p.x) * (c.y - p.y) < 0 ?
-1 : 1);
     return dis(u, p) < dis(v, p) ? u : v;
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
void intersectionCircleCircle(const Point & c1, double r1, const Point & c2, double
 r2, Point & p1, Point & p2) {
     Point u, v;
     double t = (1 + (r1 * r1 - r2 * r2) / dis(c1, c2) / dis(c1, c2)) / 2;
     u.x = c1.x + (c2.x - c1.x) * t;
     u.y = c1.y + (c2.y - c1.y) * t;
     v.x = u.x + c1.y - c2.y;
     v.y = u.y - c1.x + c2.x;
     intersectionLineCircle(c1, r1, u, v, p1, p2);
}

const int MAXN = 41;

int x[MAXN], y[MAXN], r[MAXN], n;

vector<int> v;
bool used[MAXN], tmp[MAXN];

bool allcover(Point c1, double R) {
	for (int i = 0; i < n; i++) {
		Point c;
		c.x = x[i], c.y = y[i];
		if (!used[i] && dis(c, c1) + r[i] > R + EPS) return false;
	}
	return true;
}

bool cover(double R) {

//	printf("RR = %.2lf, n = %d\n", R, (int)v.size());

	int n = (int)v.size();
	if (n == 0) return true;
	if (n == 1) {
		return r[v[0]] < R + EPS;
	}
	
	if (n == 2) {
		Point p1, p2;
		p1.x = x[v[0]], p1.y = y[v[0]];
		p2.x = x[v[1]], p2.y = y[v[1]];
		return (dis(p1, p2) + r[v[0]] + r[v[1]]) / 2 < R + EPS;
	}

	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++) {
			Point c1, c2;
			c1.x = x[v[i]], c1.y = y[v[i]];
			c2.x = x[v[j]], c2.y = y[v[j]];
			if (R < r[v[i]] || R < r[v[j]]) continue;
			Point p1, p2;
			if (intersectCircleCircle(c1, R - r[v[i]], c2, R - r[v[j]])) {
				intersectionCircleCircle(c1, R - r[v[i]], c2, R - r[v[j]], p1, p2);
				if (allcover(p1, R)) return true;
				if (allcover(p2, R)) return true;
			}
		
		}
	return false;

}

bool cover(Point c1, double R) {
	memset(used, false, sizeof(used));
	for (int i = 0; i < n; i++) {
		Point c;
		c.x = x[i], c.y = y[i];
		if (dis(c, c1) + r[i] < R + EPS) used[i] = true;
	}
	v.clear();
	for (int i = 0; i < n; i++)
		if (!used[i]) v.push_back(i);
	if (cover(R)) return true;
	return false;
}

bool ok(double R) {

//	printf("R = %.2lf\n", r);

	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++) {
			c1.x = x[i], c1.y = y[i];
			c2.x = x[j], c2.y = y[j];
			if (R < r[i] || R < r[j]) continue;
			Point p1, p2;
			if (intersectCircleCircle(c1, R - r[i], c2, R - r[j])) {
				intersectionCircleCircle(c1, R - r[i], c2, R - r[j], p1, p2);
				if (cover(p1, R)) return true;
				if (cover(p2, R)) return true;
			}
		}
	return false;
}

void solve() {

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d", &x[i], &y[i], &r[i]);	
	}

	if (n == 1) {
		printf("%.6lf\n", (double)r[0]);
		return;
	}
	if (n == 2) {
		printf("%.6lf\n", (double)max(r[0], r[1]));
		return;
	}

	double INF = 1000;
	double left = 0, right = INF, ans = INF;
	while (right - left > EPS) {
		double x = (left + right) / 2;
		if (ok(x)) {
			right = x;
			ans = min(ans, x);
		}
		else {
			left = x;
		}
	}
	printf("%.7lf\n", ans);
}

int main() {

	int test;
	scanf("%d", &test);
	for (int i = 1; i<= test; i++) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}

