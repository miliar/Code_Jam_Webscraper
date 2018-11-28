#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <map>
using namespace std;

#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
#define FOR(i,c) for (__typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)

const double PI = acos(-1.0);

double piece(double x1, double x2, double y1, double u) {
  if (x1*x1 + y1*y1 > u*u) return 0.0;
  assert(u > y1);
  double x3 = sqrt(u*u - y1*y1);
  assert(x1 <= x3);
  x2 = min(x2, x3);
  //printf("x1: %f\nx2: %f\ny1: %f\nr: %f\n\n", x1, x2, y1, r);

  double t1 = acos(x1 / u);
  double t2 = acos(x2 / u);
  double circ = (t1-sin(2*t1)/2 - t2+sin(2*t2)/2)*u*u/2.0;
  return max(circ - (x2-x1)*y1, 0.0);
}


class Racket {
public:
  void input() {
    scanf("%lf %lf %lf %lf %lf\n", &f_, &R_, &t_, &r_, &g_);
    //printf("f: %f\nR: %f\nt: %f\nr: %f\ng: %f\n:", f_,R_,t_,r_,g_);
  }
  double calc() {
    double sect = sector_gap();
    double A = PI*R_*R_;
    //printf("    %.2f  sect: %.2f / %.2f\n", 4.0*sect/A, sect, A/4.0);
    double ret = 1.0 - (4.0 * sect) / A;
    return max(ret, 0.0);
  }
private:
  double sector_gap() {
    double gr = g_ - 2*f_;
    if (gr <= 0) return 0.0;
    double perfect_gap = gr*gr;
    double STEP = g_ + 2*r_;
    double E = R_ - t_ - f_;
    double ret = 0.0;
    for (double b = r_+f_; b < E; b += STEP) {
      double t = b + gr;
      long long npgap = 0;

      if (t < E) {
        double x = sqrt(E*E - t*t);
        if (x >= r_ + g_) {
          npgap = 1 + static_cast<int>((x-r_-g_+f_) / STEP);
          ret += npgap * perfect_gap;
        }
      }


      for (long long i = npgap; ; ++i) {
        double x1 = r_+f_ + i*STEP;
        if (x1*x1 + b*b > E*E) break;
        ret += piece(x1, x1+gr, b, E);
        ret -= piece(x1, x1+gr, b+gr, E);
      }

    }
    return ret;
  }

  double f_, R_, t_, r_, g_;
};

int main() {
  int n;
  scanf("%d\n", &n);
  for (int t = 1; t <= n; ++t) {
    Racket r;
    r.input();
    double p = r.calc();
    printf("Case #%d: %.6f\n", t, p);
  }
}
