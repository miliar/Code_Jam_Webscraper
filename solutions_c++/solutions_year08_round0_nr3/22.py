#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

// (x, y) is lower right corner
long double area(long double X, long double y, long double s, long double &t)
{
  if (X*X + y*y <= 1) { // hits on further, vertical side
    t = acosl(X); double yhit = sqrtl(1 - X*X);
    return 0.5 * (X * (yhit-y) - s * y);
  }
  else { // hits on nearer, horizontal side
    t = asinl(y); double xhit = sqrtl(1 - y*y);
    //cout << xhit << " on " << X-s << " to " << X << endl;
    return -0.5 * (xhit-(X-s)) * y;
  }
}

long double box(long double x, long double y, long double s)
{
  long double X = x+s, Y = y+s;
  if (X*X + Y*Y <= 1) return s*s;
  long double theta1, area1, theta2, area2;
  area1 = area(X, y, s, theta1);
  area2 = area(Y, x, s, theta2);
  //cout << x << " " << y << ": " << theta1 << ", " << theta2 << "; " << area1 << ", " << area2 << ", " << M_PI/2 - (theta1 + theta2) + area1 + area2 << endl;
  return (M_PI/2 - (theta1 + theta2)) / 2 + area1 + area2;
}

int main(void)
{
  int N;
  cin >> N;
  for (int c = 1; c <= N; c++) {
    long double f, R, t, r, g;
    cin >> f >> R >> t >> r >> g;
    long double Rin = R-t-f, gf = g-2*f;
    long double ans = 0;
    if (Rin <= 0 || gf <= 0)
      ans = 1;
    else {
      f /= Rin; R /= Rin; t /= Rin; r /= Rin; g /= Rin; gf /= Rin;
      //cout << gf << endl;
      long double d = 2*r + g;
      for (long double x = r+f; x < 1; x += d)
	for (long double y = r+f; x*x + y*y < 1; y += d)
	  ans += box(x, y, gf);
      ans = 1 - ans / R / R / (M_PI/4);
    }
    printf("Case #%d: %Lf\n", c, ans);
  }
}
