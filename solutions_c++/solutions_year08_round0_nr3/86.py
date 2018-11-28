#include <cstdio>
#include <map>
#include <string>
#include <set>
#include <cmath>

using namespace std;

typedef pair<int, int> pii;

const double eps = 1e-10;
const double pi = 2.0*acos(0.0);

double sqr(double x) { return x*x; }

double f, R, t, r, g;
double xa, ya, xb, yb;

double h(double x) {
  if (x > R-f) return 0;
  double y = sqrt(sqr(R-f) - sqr(x));
  if (y < ya) return 0;
  return min(yb, y) - ya;
}

double area(double x1, double x2, double f1, double f2, double A) {
  double xM = (x1+x2)/2, fM = h(xM);
  double A1 = (f1+fM)*(xM-x1)/2, A2 = (fM+f2)*(x2-xM)/2;
  if (fabs(A1+A2-A) < eps*(A1+A2+eps)) return A1+A2;
  return area(x1, xM, f1, fM, A1) + area(xM, x2, fM, f2, A2);
}

double area(double x1, double x2) {
  double f1 = h(x1), f2 = h(x2);
  return area(x1, x2, f1, f2, (f1+f2)*(x2-x1)/2);
}

void solve(int P) {

  scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
  double missA = 0, totA = pi*sqr(R);
  R -= t;

  if (2*f < g && f < R) {
    for (int x = 0; r + x*(2*r+g)+f < R; ++x) {
      for (int y = x; y*(2*r+g) < R; ++y) {
	xa = r + x*(2*r+g) + f;
	xb = xa + g - 2*f;
	ya = r + y*(2*r+g) + f;
	yb = ya + g - 2*f;
	if (sqr(xa) + sqr(ya) > sqr(R)) break;
	//	if (x > y) { swap(xa, ya); swap(xb, yb); }
	double con = area(xa, xb);
	missA += con;
	if (x != y) missA += con;
      }
    }
  }

  printf("Case #%d: %.8lf\n", P, 1-4*missA/totA);
  fprintf(stderr, "Case #%d: %.8lf\n", P, 1-4*missA/totA);
}

int main(void) {
  int N;
  scanf("%d", &N);
  for (int i = 1; i <= N; ++i) solve(i);
  return 0;
}
