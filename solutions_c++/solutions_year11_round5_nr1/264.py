#include <math.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <complex>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

#define X real()
#define Y imag()

const int MAXN = 100;

typedef complex<double> Point;

double xl[MAXN], yl[MAXN], xu[MAXN], yu[MAXN];
int l, u, g;

inline int sgn(double x) {
  if (abs(x) < 1e-9) return 0;
  return x < 0 ? - 1 : 1;
}

inline double cross(Point a, Point b) {
  return a.X * b.Y - a.Y * b.X;
}

double solve(double x) {
  double result = 0.0;
  Point p1, p2;
  for (int i = 1; i < l; ++i) {
    if (sgn(xl[i] - x) < 0) {
      result += cross(Point(xl[i], yl[i]), Point(xl[i - 1], yl[i - 1]));
    } else {
      double y = (yl[i] - yl[i - 1]) * (x - xl[i - 1]) / (xl[i] - xl[i - 1]) + yl[i - 1];
      p1 = Point(x, y);
      result += cross(p1, Point(xl[i - 1], yl[i - 1]));
      break;
    }
  }
  for (int i = 1; i < u; ++i) {
    if (sgn(xu[i] - x) < 0) {
      result += cross(Point(xu[i - 1], yu[i - 1]), Point(xu[i], yu[i]));
    } else {
      double y = (yu[i] - yu[i - 1]) * (x - xu[i - 1]) / (xu[i] - xu[i - 1]) + yu[i - 1];
      p2 = Point(x, y);
      result += cross(Point(xu[i - 1], yu[i - 1]), p2);
      break;
    }
  }
  result += cross(Point(xl[0], yl[0]), Point(xu[0], yu[0]));
  result += cross(p2, p1);
  return abs(result / 2.0);
}

int main() {
  int T, W;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    printf("Case #%d:\n", tt);
    scanf("%d%d%d%d", &W, &l, &u, &g);
    for (int i = 0; i < l; ++i) {
      scanf("%lf%lf", xl + i, yl + i);
    }
    for (int i = 0; i < u; ++i) {
      scanf("%lf%lf", xu + i, yu + i);
    }
    double sum = solve(W);
    for (int i = 1; i < g; ++i) {
      double minv = 0, maxv = W, mid;
      while (maxv - minv > 1e-9) {
        mid = (minv + maxv) / 2.0;
        double val = solve(mid);
        if (val < sum / g * i) minv = mid;
        else maxv = mid;
      }
      printf("%lf\n", minv);
    }
  }
  return 0;
}
