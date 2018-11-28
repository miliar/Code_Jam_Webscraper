#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;
typedef long long ll;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define DEC(i, s) for (int i = (s); i >= 0; i--)

#define SIZE(v) (int)((v).size())
#define MEMSET(v, h) memset((v), h, sizeof(v))
#define FIND(m, w) ((m).find(w) != (m).end())

#include <complex>
#include <vector>

typedef complex<double> Point;
typedef vector<Point> Polygon;

//static const double EPS = 1e-8;
static const double INF = 1e+10;

#define CURR(P, i) (P[i])
#define NEXT(P, i) (P[(i + 1) % P.size()])

struct Line : public vector<Point> {
  Line() {;}
  Line(Point a, Point b) { push_back(a); push_back(b); }
};

struct Circle {
  Point p;
  double r;
  Circle() {;}
  Circle(Point p, double r) : p(p), r(r) {;}
};

namespace std {
  bool operator<(const Point &lhs, const Point &rhs) {
    return lhs.real() == rhs.real() ? lhs.imag() < rhs.imag() : lhs.real() < rhs.real();
  }
}

inline double cross(const Point &a, const Point &b) {
  return imag(conj(a) * b);
}

inline double dot(const Point &a, const Point &b) {
  return real(conj(a) * b);
}

inline int ccw(Point a, Point b, Point c) {
  b -= a;
  c -= a;
  if (cross(b, c) > 0) { return 1; }
  if (cross(b, c) < 0) { return -1; }
  if (dot(b, c) < 0) { return 2; }
  if (norm(b) < norm(c)) { return -2; }
  return 0;
}

double CircleCircleArea(double r1, double r2, double d) {
  //if (r1 < r2) { swap(r1, r2); }
  //cout << r2 << " " << r2 << " " << d << endl;
  //if (r1 - r2 - d > -EPS || r2 < EPS) {
    //return r1 * r1 * PI;
  //}
  //double S = r1 * r1 * PI + r2 * r2 * PI;
  //if (r1 + r2 - d < EPS) { return S; }
  double t1 = acos((d * d + r1 * r1 - r2 * r2) / (2 * d * r1));
  double t2 = acos((d * d + r2 * r2 - r1 * r1) / (2 * d * r2));
  double sq = (r1 * r1 * sin(t1 * 2) + r2 * r2 * sin(t2 * 2)) / 2.0;
  double s = r1 * r1 * t1 
    + r2 * r2 * t2
    - sq;
  //cout << r1 << " " << r2 << " " << d << " " << S << " " << s << endl;
  //assert(s >= -EPS);
  //assert(s == s);
  return s;
}

Point pole[6000];
Point bucket[2000];

int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    test_case++;
    printf("Case #%d:", test_case);
    int n, m;
    scanf("%d %d", &n, &m);
    REP(i, n) {
      double x, y;
      scanf("%lf %lf", &x, &y);
      pole[i] = Point(x, y);
    }
    REP(i, m) {
      double x, y;
      scanf("%lf %lf", &x, &y);
      bucket[i] = Point(x, y);
    }
    REP(i, m) {
      double r1 = abs(pole[0] - bucket[i]);
      double r2 = abs(pole[1] - bucket[i]);
      double d = abs(pole[0] - pole[1]);
      printf(" %.7lf", CircleCircleArea(r1, r2, d));
    }
    puts("");
  }
}
