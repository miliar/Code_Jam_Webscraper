#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

#define all(v) (v).begin(), (v).end()

inline int cmp(double x, double y=0, double tol=1e-10) {
	return (x <= y+tol) ? (x+tol < y) ? -1 : 0 : 1;
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
	bool operator < (point q) const { return cmp(q) <  0; }
	
	friend ostream& operator <<(ostream& o, point p) {
		return o << "(" << p.x << ", " << p.y << ")";
	}
};

double abs(point p) { return hypot(p.x, p.y); }

////////////////////////////////////////////////////////////////////////////////
// Encontra o menor círculo que contém todos os pontos dados.
//

typedef pair<point, double> circle;

bool in_circle(circle C, point p){
	return cmp(abs(p - C.first), C.second) <= 0;
}

point circumcenter(point p, point q, point r) {
	point a = p - r, b = q - r, c = point(a * (p + r) / 2, b * (q + r) / 2);
	return point(c % point(a.y, b.y), point(a.x, b.x) % c) / (a % b);
}

circle spanning_circle(vector<point>& T) {
	int n = T.size();
	random_shuffle(all(T));
	circle C(point(), -INFINITY);
	for (int i = 0; i < n; i++) if (!in_circle(C, T[i])) {
		C = circle(T[i], 0);
		for (int j = 0; j < i; j++) if (!in_circle(C, T[j])) {
			C = circle((T[i] + T[j]) / 2, abs(T[i] - T[j]) / 2);
			for (int k = 0; k < j; k++) if (!in_circle(C, T[k])) {
				point o = circumcenter(T[i], T[j], T[k]);
				C = circle(o, abs(o - T[k]));
			}
		}
	}
	return C;
}





circle flor[5];

int main() {
	int T;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		int N;
		scanf(" %d", &N);
		for (int i=0; i < N; i++) {
			int x, y, r;
			scanf(" %d %d %d", &x, &y, &r);
			flor[i] = circle(point(x,y), r);
		}

		double ans = -1.0;
		if (N == 1) ans = flor[0].second;
		else if (N == 2) ans = max(flor[0].second, flor[1].second);
		else { // N == 3
			ans = 0x3f3f3f3f;
			for (int i=0; i < 3; i++) {
				point seg = flor[(i+1)%3].first - flor[(i+2)%3].first;
				double d = abs(seg) + flor[(i+1)%3].second + flor[(i+2)%3].second;
				double tmp = max(flor[i].second, d/2.0);
				ans = min(ans, tmp);
			}
		}
		printf("Case #%d: %.8lf\n", _42, ans);
	}

	return 0;
}
