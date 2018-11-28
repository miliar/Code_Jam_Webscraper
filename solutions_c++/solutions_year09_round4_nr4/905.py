
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;
int cmp(double x, double y = 0, double tol = EPS) {
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
  bool operator < (point q) const { return cmp(q) <  0; }
  
  static point pivot;
};

double abs(point p) { return hypot(p.x, p.y); }
double arg(point p) { return atan2(p.y, p.x); }

typedef pair<point, double> circle;
/*
bool in_circle(circle C, circle D){
  return cmp(abs(D.first - C.first), C.second - D.second) <= 0;
}
point circumcenter(point p, point q, point r) {
  point a = p - r, b = q - r, c = point(a * (p + r) / 2, b * (q + r) / 2);
  return point(c % point(a.y, b.y), point(a.x, b.x) % c) / (a % b);
}
circle spanning_circle(vector<circle>& T) {
  int n = T.size();
  random_shuffle(T.begin(), T.end());
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
*/
circle plants[16];

int main(void)
{
	int nc, ca;
	int i, j;
	int n;
	double res;

	scanf("%d", &nc);
	for(ca=1; ca<=nc; ca++)
	{
		printf("Case #%d: ", ca);

		scanf("%d", &n);
		for(i=0; i<n; i++) scanf("%lf %lf %lf", &plants[i].first.x, &plants[i].first.y, &plants[i].second);

		if(n == 1) res = 2*plants[0].second;
		if(n == 2) res = 2*max(plants[0].second, plants[1].second);
		if(n == 3)
		{
			res = 99999999;

			double val;

			val = plants[0].second + plants[1].second + abs(plants[0].first - plants[1].first);
			val = max(val, 2*plants[2].second);
			res = min(res, val);

			val = plants[0].second + plants[2].second + abs(plants[0].first - plants[2].first);
			val = max(val, 2*plants[1].second);
			res = min(res, val);

			val = plants[1].second + plants[2].second + abs(plants[1].first - plants[2].first);
			val = max(val, 2*plants[0].second);
			res = min(res, val);
		}

		printf("%.6f\n", res/2);
	}

	return 0;
}
