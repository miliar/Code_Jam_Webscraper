#include <cstdio>
#include <complex>
#include <vector>
#include <set>

#define input "A-large.in"
#define output "A.out"
using namespace std;

FILE *fin = freopen(input, "r", stdin);
FILE *fout = freopen(output, "w", stdout);

const double EPS = 1e-8;
const double INF = 1e12;

typedef complex<double> P;
namespace std {
  bool operator < (const P& a, const P& b) {
    return real(a) != real(b) ? real(a) < real(b) : imag(a) < imag(b);
  }
}
double cross(const P& a, const P& b) {
  return imag(conj(a)*b);
}
double dot(const P& a, const P& b) {
  return real(conj(a)*b);
}

struct L : public vector<P> {
  L() {}
  L(const P &a, const P &b) {
    push_back(a); push_back(b);
  }
};

int ccw(P a, P b, P c) {
  b -= a; c -= a;
  if (cross(b, c) > 0)   return +1;       // counter clockwise
  if (cross(b, c) < 0)   return -1;       // clockwise
  if (dot(b, c) < 0)     return +2;       // c--a--b on line
  if (norm(b) < norm(c)) return -2;       // a--b--c on line
  return 0;
}

bool intersectSS(const L &s, const L &t) {
  return ccw(s[0],s[1],t[0])*ccw(s[0],s[1],t[1]) <= 0 &&
         ccw(t[0],t[1],s[0])*ccw(t[0],t[1],s[1]) <= 0;
}

P crosspoint(const L &l, const L &m) {
	double A = cross(l[1] - l[0], m[1] - m[0]);
	double B = cross(l[1] - l[0], l[1] - m[0]);
	if (abs(A) < EPS && abs(B) < EPS) return m[0]; // same line
//	if (abs(A) < EPS) assert(false); // !!!PRECONDITION NOT SATISFIED!!!
	return m[0] + B / A * (m[1] - m[0]);
}


int main()
{
	int cases, t;
	scanf("%d", &t);
	for (cases = 1; cases <= t; cases++) {
		int i, j, k, n, res = 0;
		int a, b;

		scanf("%d", &n);
		vector<L> seg;
		set<P> cp;
		for (i = 0; i < n; i++) {
			scanf("%d %d", &a, &b);
			L temp(P(0, a), P(1000, b));
			seg.push_back(temp);
		}

		for (j = 0; j < n; j++) {
			for (k = j + 1; k < n; k++) {
				if (intersectSS(seg[j], seg[k])) {
					P dot = crosspoint(seg[j], seg[k]);
					cp.insert(dot);
				}
			}
		}

		printf("Case #%d: %d\n", cases, cp.size());
	}

	return 0;
}