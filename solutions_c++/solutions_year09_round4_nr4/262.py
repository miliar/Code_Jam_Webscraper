#include <cstdio>
#include <string.h>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const double EPS = 1E-6;
const int MAXN = 40;

int x[MAXN], y[MAXN], r[MAXN];
double rr[MAXN];
const int MAXP = MAXN * MAXN * 2 + MAXN;
long long gan[MAXP];
int points;
int n;

void readdata() {
  scanf("%d\n", &n);
  for (int i = 0; i < n; ++i)
    scanf("%d %d %d\n", x+i, y+i, r+i);
}

inline double sqr(double u) { return u*u; };

void gangangan(double xx, double yy) {
  long long tmp;
  fprintf(stderr, "%d: (%f, %f)\n", points, xx, yy);

  tmp = 0;
  for (int i = 0; i < n; ++i)
    tmp = tmp * 2 + (int)(bool)(sqr(xx - x[i]) + sqr(yy - y[i]) < sqr(rr[i]) + EPS);
  gan[points++] = tmp;
}

bool check(double u) {
  int i, j, k;
  double d, e, bx, by, hx, hy;

  for (i = 0; i < n; ++i) {
    rr[i] = u - r[i];
    if (rr[i] < 0) return false;
  }

  points = 0;
  for (i = 0; i < n; ++i) {
    gangangan(x[i], y[i]);
    for (j = i + 1; j < n; ++j) {
      if (sqrt(sqr(x[i] - x[j]) + sqr(y[i] - y[j])) > rr[i] + rr[j] + EPS)
	continue;

      d = sqrt(sqr(x[i] - x[j]) + sqr(y[i] - y[j]));
      e = ( sqr(rr[i]) - sqr(rr[j]) ) / d + d;
      e /= 2;

      if (e - rr[i] > EPS) 
	continue;
      
      bx = x[j] * e + x[i] * (d - e);
      by = y[j] * e + y[i] * (d - e);
      bx /= d; by /= d;

      hx = y[i] - y[j];
      hy = x[j] - x[i];

      e = sqrt(sqr(rr[i]) - sqr(e));
      hx = hx * e / d;
      hy = hy * e / d;

      gangangan(bx + hx, by + hy);
      gangangan(bx - hx, by - hy);
    }
  }

  for (i = 0; i < points; ++i)
    fprintf(stderr, "%d: %lld\n", i, gan[i]);

  long long all = 0;
  for (i = 0; i < n; ++i)
    all = all * 2 + 1;

  for (i = 0; i < points; ++i)
    for (j = i; j < points; ++j)
      if (((gan[i] | gan[j]) & all) == all)
	return true;
  return false;
}

double solve() {
  double l = 0, r = 2200, m;

  while (r - l > EPS) {
    m = (r + l) / 2;

    fprintf(stderr, "\nchecking %f\n", m);
    if (check(m))
      r = m;
    else 
      l = m;
  }

  return m;
}

int main() {
  int t;
  scanf("%d\n", &t);
  for (int i = 1; i <= t; ++i) {
    readdata();
    printf("Case #%d: %.6f\n", i, solve());
  }

  return 0;
}
