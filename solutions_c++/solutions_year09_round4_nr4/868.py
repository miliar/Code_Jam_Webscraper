#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cfloat>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <string>

using namespace std;

#define loop(a, b) for(a = 0; a < b; ++a)
#define iter(a, b, c) for(a = b; a < c; ++a)

#define all(v) (v).begin(), (v).end()
#define _inline(f...) f() __attribute__((always_inline)); f
const double EPS = 1e-10;

_inline(int cmp)(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

struct P {
	double x, y, r;
	P(double x = 0, double y = 0): x(x), y(y) {}
	P operator +(P q) { return P(x + q.x, y + q.y); }
	P operator -(P q) { return P(x - q.x, y - q.y); }
	P operator *(double t) { return P(x * t, y * t); }
	P operator /(double t) { return P(x / t, y / t); }
	double operator *(P q) { return x * q.x + y * q.y; }
	double operator %(P q) { return x * q.y - y * q.x; }
	int cmp(P q) const {
		if (int t = ::cmp(x, q.x)) return t;
		return ::cmp(y, q.y);
	}
	bool operator ==(P q) const { return cmp(q) == 0; }
	bool operator !=(P q) const { return cmp(q) != 0; }
	bool operator < (P q) const { return cmp(q) < 0; }
	static P pivot;
};

typedef pair<P, double> circle;

double abs(P p) { return hypot(p.x, p.y); }

bool in_circle(circle C, P p){
	return cmp(abs(p - C.first), C.second) <= 0;
}
P circumcenter(P p, P q, P r) {
	P a = p - r, b = q - r, c = P(a * (p + r) / 2, b * (q + r) / 2);
	return P(c % P(a.y, b.y), P(a.x, b.x) % c) / (a % b);
}
circle spanning_circle(vector<P>& T) {
	int n = T.size();
	if (n == 0) {
//		puts("YY");
		return circle(P(), 0);
	}
	if (n == 1) {
//		puts("XX");
		return circle(P(), T[0].r);
	}
	random_shuffle(all(T));
	circle C(P(), -INFINITY);
	for (int i = 0; i < n; i++) if (!in_circle(C, T[i])) {
		C = circle(T[i], 0);
		for (int j = 0; j < i; j++) if (!in_circle(C, T[j])) {
			C = circle((T[i] + T[j]) / 2, abs(T[i] - T[j]) / 2);
			for (int k = 0; k < j; k++) if (!in_circle(C, T[k])) {
				P o = circumcenter(T[i], T[j], T[k]);
				C = circle(o, abs(o - T[k]));
			}
		}
	}
	return C;
}

P c[1000], pa[1000], pb[1000];

double dist(int a, int b) {
	double dx = c[a].x - c[b].x, dy = c[a].y - c[b].y;
	return dx*dx + dy*dy + c[a].r + c[b].r;
}

int main(){
	int ds, n, i, j, k, npa, npb, tc = 1;
	double ans;
	P pt;
	vector<P> p;
	scanf("%d", &ds);
	while(ds--) {
		ans = DBL_MAX;
		scanf("%d", &n);
		loop(i, n)
			scanf("%lf%lf%lf", &c[i].x, &c[i].y, &c[i].r);
/*		if (n == 1) {
			printf("Case #%d: %lf\n", tc++, c[0].r);
			continue;
		}*/
		loop(i, 1<<n) {
			npa = npb = 0;

/*			loop(j, n)
				printf("%d", (i & 1<<j));
			puts("");
*/
			loop(j, n) {
				iter(k, j+1, n) {
					if ((i & 1<<j) and (i & 1<<k)) {
						pt = c[j]-c[k];
						pa[npa] = c[j];
						pa[npa].x += pt.x/hypot(pt.x, pt.y)*c[j].r;
						pa[npa].y += pt.y/hypot(pt.x, pt.y)*c[j].r;
						npa++;

						pt = c[k]-c[j];
						pa[npa] = c[k];
						pa[npa].x += pt.x/hypot(pt.x, pt.y)*c[k].r;
						pa[npa].y += pt.y/hypot(pt.x, pt.y)*c[k].r;
						npa++;
					} else if (!(i & 1<<j) and !(i & 1<<k)) {
						pt = c[j]-c[k];
						pb[npb] = c[j];
						pb[npb].x += pt.x/hypot(pt.x, pt.y)*c[j].r;
						pb[npb].y += pt.y/hypot(pt.x, pt.y)*c[j].r;
						npb++;

						pt = c[k]-c[j];
						pb[npb] = c[k];
						pb[npb].x += pt.x/hypot(pt.x, pt.y)*c[k].r;
						pb[npb].y += pt.y/hypot(pt.x, pt.y)*c[k].r;
						npb++;
					}
				}
			}

			p.clear();
			loop(k, npa)
				p.push_back(pa[k]);
			if (npa == 0)
				loop(k, n)
					if (i & 1<<k)
						p.push_back(c[k]);
			circle ca = spanning_circle(p);

			p.clear();
			loop(k, npb)
				p.push_back(pb[k]);
			if (npb == 0)
				loop(k, n)
					if (!(i & 1<<k))
						p.push_back(c[k]);
			circle cb = spanning_circle(p);

			ans = min(ans, max(ca.second, cb.second));
		}
		printf("Case #%d: %lf\n", tc++, ans);
	}
	return 0;
}
