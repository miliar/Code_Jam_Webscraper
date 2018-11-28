#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <utility>
#include <string>
#include <vector>
#include <queue>
#include <map>
using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << endl)

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)
#define rep(i, n) foreach(i, 0, n)

#define MSET(c, v) memset(c, v, sizeof(c))

const int INF = 0x3f3f3f3f; const int NEGINF = 0xC0C0C0C0;
const int NULO = -1;
double EPS = 1.e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
struct point {
	double x,y;
	point(double x = 0, double y = 0): x(x), y(y) {}
	point operator +(point q) { return point(x + q.x, y + q.y); }
	point operator -(point q) { return point(x - q.x, y - q.y); }
	point operator *(double t) { return point(t*x, t*y); }
	point operator /(double t) { return point(x/t, y/t); }
	double operator *(point q) { return x*q.x + y*q.y; }
	double operator %(point q) { return x*q.y - y*q.x; }
	int cmp(point q) const {
		if (int t = ::cmp(x, q.x)) return t;
		return ::cmp(y, q.y);
	}
	bool operator==(point q) const { return cmp(q) == 0; }
	bool operator!=(point q) const { return cmp(q) != 0; }
	bool operator <(point q) const { return cmp(q) < 0; }
	static point pivot;
};

point point::pivot;

double abs(point p) { return hypot(p.x, p.y); }
double arg(point p) { return atan2(p.y, p.x); }

typedef vector<point> polygon;

inline int ccw(point p, point q, point r) {
	return cmp((p-r)%(q-r));
}

inline double angle(point p, point q, point r) {
	point u = p - q, v = r - q;
	return atan2(u%v, u*v);
}

bool between(point p, point q, point r) {
	return ccw(p, q, r) == 0 && cmp((p-q)*(r-q)) <= 0;
}

bool seg_intersect(point p, point q, point r, point s) {
	point A = q-p, B = s-r, C = r-p, D = s-q;
	int a = cmp(A%C) + 2*cmp(A%D);
	int b = cmp(B%C) + 2*cmp(B%D);
	if (a == 3 || a == -3 || b == 3 || b == -3) return false;
	if (a || b || p == r || p == s || q == r || q == s) return true;
	int t = (p < r) + (p < s) + (q < r) + (q < s);
	return t != 0 && t != 4;
}

double seg_distance(point p, point q, point r) {
	point A = r-q, B = r-p, C = q-p;
	double a = A*A, b = B*B, c = C*C;
	if (cmp(b, a+c) >= 0) return sqrt(a);
	else if (cmp(a, b+c) >= 0) return sqrt(b);
	else return fabs(A%B)/sqrt(c);
}

int in_poly(point p, polygon& T) {
	double a = 0; int N = T.size();
	for (int i = 0; i < N; i++) {
		if (between(T[i], p, T[(i+1)%N])) return -1;
		a += angle(T[i], p, T[(i+1)%N]);
	}
	return cmp(a) != 0;
}

bool radial_lt(point p, point q) {
	point P = p - point::pivot, Q = q - point::pivot;
	double R = P%Q;
	if (cmp(R)) return R > 0;
	return cmp(P*P, Q*Q) < 0;
}

polygon convex_hull(vector<point>& T) {
	int j = 0, k, n = T.size(); polygon U(n);

	point::pivot = *min_element(all(T));
	sort(all(T), radial_lt);
	for (k = n-2; k >= 0 && ccw(T[0], T[n-1], T[k]) == 0; k--);
	reverse((k+1) + all(T));
	for (int i = 0; i < n; i++) {
		while (j > 1 && ccw(U[j-1], U[j-2], T[i]) >= 0) j--;
		U[j++] = T[i];
	}
	U.erase(j + all(U));
	return U;
}

double poly_area(polygon& T) {
	double s = 0; int n = T.size();
	for (int i = 0; i < n; i++)
		s += T[i] % T[(i+1)%n];
	return s/2;
}

point line_intersect(point p, point q, point r, point s) {
	point a = q-p, b = s-r, c = point(p%q, r%s);
	return point(point(a.x, b.x)%c, point(a.y, b.y)%c)/(a%b);
}

typedef pair<point, double> circle;

bool in_circle(circle C, point p) {
	return cmp(abs(p-C.first), C.second) <= 0;
}

point circumcenter(point p, point q, point r) {
	point a = p-r, b = q-r, c = point(a*(p+r)/2, b*(q+r)/2);
	return point(c%point(a.y, b.y), point(a.x, b.x) %c) / (a % b);
}

circle spanning_circle(vector<point>& T) {
	int n = T.size();
	random_shuffle(all(T));
	circle C(point(), -INFINITY);
	rep(i, n) if (!in_circle(C, T[i])) {
		C = circle(T[i], 0);
		rep(j, i) if (!in_circle(C, T[j])) {
			C = circle((T[i] + T[j])/2, abs(T[i]-T[j])/2);
			rep(k, j) if (!in_circle(C, T[k])) {
				point o = circumcenter(T[i], T[j], T[k]);
				C = circle(o, abs(o-T[k]));
			}
		}
	}
	return C;
}

polygon poly_intersect(polygon& P, polygon& Q) {
	int m = Q.size(), n = P.size();
	int a = 0, b = 0, aa = 0, ba = 0, inflag = 0;
	polygon R;
	while ((aa < n || ba < m) && aa < 2*n && ba < 2*m) {
		point p1 = P[a], p2 = P[(a+1)%n], q1 = Q[b], q2 = Q[(b+1)%m];
		point A = p2 - p1, B = q2 - q1;
		int cross = cmp(A%B), ha = ccw(p2, q2, p1), hb = ccw(q2, p2, q1);
		if (cross == 0 && ccw(p1, q1, p2) == 0 && cmp(A*B) < 0) {
			if (between(p1, q1, p2)) R.push_back(q1);
			if (between(p1, q2, p2)) R.push_back(q2);
			if (between(q1, p1, q2)) R.push_back(p1);
			if (between(q1, p2, q2)) R.push_back(p2);
			if (R.size() < 2) return polygon();
			inflag = 1; break;
		} else if (cross != 0 && seg_intersect(p1, p2, q1, q2)) {
			if (inflag == 0) aa = ba = 0;
			R.push_back(line_intersect(p1, p2, q1, q2));
			inflag = (hb > 0) ? 1 : -1;
		}
		if (cross == 0 && hb < 0 && ha < 0) return R;
		bool t = cross == 0 && hb == 0 && ha == 0;
		if (t? (inflag == 1) : (cross >= 0) ? (ha <= 0) : (hb > 0)) {
			if (inflag == -1) R.push_back(q2);
			ba++; b++; b %= m;
		} else {
			if (inflag == 1) R.push_back(p2);
			aa++; a++; a %= n;
		}
	}
	if (inflag == 0) {
		if (in_poly(P[0], Q)) return P;
		if (in_poly(Q[0], P)) return Q;
	}
	R.erase(unique(all(R)), R.end());
	if (R.size() > 1 && R.front() == R.back()) R.pop_back();
	return R;
}
circle P[5010];
point Q;

int main() {
	TRACE(setbuf(stdout, NULL));
	int _42;
	scanf("%d", &_42);
	rep(_41, _42) {
		printf("Case #%d:", _41+1);
		int N, M;
		scanf("%d %d", &N, &M);
		rep(i, N) scanf("%lf %lf", &P[i].first.x, &P[i].first.y);
		rep(i, M) {
			scanf("%lf %lf", &Q.x, &Q.y);
			P[0].second = abs(P[0].first - Q);
			P[1].second = abs(P[1].first - Q);
			if (cmp(abs(P[0].first - P[1].first), P[0].second + P[1].second) >= 0) {
				printf(" 0.0000000");
				continue;
			}
			double theta = fabs(2.*angle(P[1].first, P[0].first, Q));
			double ans = 0.5*P[0].second*P[0].second*(theta - sin(theta));
			theta = fabs(2.*angle(P[0].first, P[1].first, Q));
			ans += 0.5*P[1].second*P[1].second*(theta - sin(theta));
			printf(" %.7lf", ans);
		}
		printf("\n");
	}
	return 0;
}

