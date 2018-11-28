#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;
 
#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
 
const double EPS = 1E-10;
const double INF = 1E10;
 
struct _tag_orig { double f, R, t, r, g; } orig;

double Rout, Rin, r, g;

inline double sqr(double x) { return x * x; }

double f(double x1, double y1) {
  double x2 = x1 + g;
  double y2 = y1 + g;
  double xb1 = (y2 > Rin - EPS ? -INF : sqrt(sqr(Rin) - sqr(y2)));
  double xb2 = sqrt(sqr(Rin) - sqr(y1));
  
  double res = 0.0;
  if (xb1 > x1 + EPS) {
    if (xb1 > x2 - EPS) {
      // 正方形のみの場合
      return g * g;
    }

    // 長方形部分
    //puts("also rect");
    res += (xb1 - x1) * (y2 - y1);
  }

  // 以下は円により切り取られた部分
  x1 = max(x1, xb1);
  x2 = min(x2, xb2);

  double yb2 = sqrt(sqr(Rin) - sqr(x1));
  y2 = min(y2, yb2);

  double ybottom = y1;
  y1 = sqrt(sqr(Rin) - sqr(x2 - EPS));
  
  double th = atan2(y2, x1) - atan2(y1, x2);
  res += (th / 2.0) * sqr(Rin)
    + 0.5 * x2 * y1
    - 0.5 * x1 * y2
    - (x2 - x1) * ybottom;

  return res;
}

int main() {
  int N;
  cin >> N;
  rep (c, N) {
    cin >> orig.f >> orig.R >> orig.t >> orig.r >> orig.g;
    
    // ハエの分の変換
    Rout = orig.R;
    Rin = orig.R - orig.t - orig.f;
    r = orig.r + orig.f;
    g = orig.g - 2.0 * orig.f;

    if (g < EPS) {
      printf("Case #%d: %.10lf\n", c + 1, 1.0);
      continue;
    }

    double s = 0.0;

    // xについてまず走査
    double x = r;
    while (sqr(x) + sqr(r) < sqr(Rin) - EPS) {
      //printf("x: %lf, s: %lf\n", x, s);
      // 面積やって
      double y = r;
      while (sqr(x) + sqr(y) < sqr(Rin) - EPS) {
        s += f(x, y);
        y += g + 2.0 * r;
      }
      
      // x動かす
      x += g + 2.0 * r;
      
      //break;
    }
  done:

    double ans = 1.0 - (4.0 * s / (M_PI * sqr(Rout)));
    printf("Case #%d: %.10lf\n", c + 1, ans);
  }
}
