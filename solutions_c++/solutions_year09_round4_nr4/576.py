#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <utility>
#include <iostream>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <string>

#define rep(i, n) for (int i = 0; i < n; i++)

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define TRACE(x...) 
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

using namespace std;

const int INF = 0x3f3f3f3f, NEGINF = 0xc0c0c0c0, NULO = -1;
const double EPS = 1e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

struct point {
	double x, y;
	point(double x = 0, double y = 0): x(x), y(y) {}

	point operator +(point q) { return point(x + q.x, y + q.y); }
	point operator -(point q) { return point(x - q.x, y - q.y); }
	point operator *(double t) { return point(x * t, y * t); }
	point operator /(double t) { return point(x / t, y / t); }
	double operator *(point q) { return x * q.x + y * q.y; }
	double operator %(point q) { return x * q.y - y * q.x; }

	int cmp(point q) const {
		if (int t = ::cmp(x, q.x)) return t;
		return ::cmp(y, q.y);
	}
	bool operator ==(point q) const { return cmp(q) == 0; }
	bool operator !=(point q) const { return cmp(q) != 0; }
	bool operator <(point q) const { return cmp(q) < 0; }

	friend ostream& operator <<(ostream& o, point p) {
		return o << "(" << p.x << ", " << p.y << ")";
	}

	static point pivot;
};

point point::pivot;

double abs(point p) { return hypot(p.x, p.y); }
double arg(point p) { return atan2(p.y, p.x); }

typedef vector<point> polygon;

inline int ccw(point p, point q, point r) {
	return cmp((p - r) % (q - r));
}

inline double angle(point p, point q, point r) {
	point u = p - q, v = r - q;
	return atan2(u % v, u * v);
}

double seg_distance(point p, point q, point r) {
	point A = r - q, B = r - p, C = q - p;
	double a = A * A, b = B * B, c = C * C;
	if (cmp(b, a + c) >= 0) return sqrt(a);
	else if (cmp(a, b + c) >= 0) return sqrt(b);
	else return fabs(A % B) / sqrt(c);
}

double circs[50][3];

int main() {
	int C;
	scanf("%d", &C);

	rep(c,C) {
		int N;
		scanf("%d", &N);
		
		rep(i,N) {
			scanf("%lf %lf %lf", &circs[i][0], &circs[i][1], &circs[i][2]);
		}
		
		double res = INFINITY;

		if (N == 1) res = circs[0][2];
		else if (N == 2) res = max(circs[0][2], circs[1][2]);
		else {
			point c1;
			point c2;

			c1 = point(circs[0][0], circs[0][1]);
			c2 = point(circs[1][0], circs[1][1]);
			res = min(res, max((abs(c1-c2) + circs[0][2] + circs[1][2])/2., circs[2][2]));
			
			c1 = point(circs[1][0], circs[1][1]);
			c2 = point(circs[2][0], circs[2][1]);
			res = min(res, max((abs(c1-c2) + circs[1][2] + circs[2][2])/2., circs[0][2]));
			
			c1 = point(circs[0][0], circs[0][1]);
			c2 = point(circs[2][0], circs[2][1]);
			res = min(res, max((abs(c1-c2) + circs[0][2] + circs[2][2])/2., circs[1][2]));

		}

		printf("Case #%d: %lf\n", c+1, res);
	}
}


