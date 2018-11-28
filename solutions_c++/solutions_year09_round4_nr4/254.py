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

double sq(double x) {
  return x*x;
}

void lin_solve(double a, double b, double c, double d, double e, double f,
	       double &x, double &y) {
  x = (b*f - c*e) / (a*e - b*d);
  y = (a*f - c*d) / (a*e - b*d);
}

void circ_center(double x1, double y1, double r1,
		 double x2, double y2, double r2,
		 double x3, double y3, double r3,
		 double &x, double &y, double &r) {

  double xr, yr, x0, y0;
  lin_solve(2*(x1-x2), 2*(y1-y2), 2*(r1-r2),
	    2*(x1-x3), 2*(y1-y3), 2*(r1-r3),
	    xr, yr);
  lin_solve(2*(x1-x2), 2*(y1-y2), sq(x1)-sq(x2)+sq(y1)-sq(y2)-sq(r1)+sq(r2),
	    2*(x1-x3), 2*(y1-y3), sq(x1)-sq(x3)+sq(y1)-sq(y3)-sq(r1)+sq(r3),
	    x0, y0);
  
  double A, B, C;
  A = sq(xr) + sq(yr) - 1;
  B = 2*xr*(x0-x1) + 2*yr*(y0-y1) + 2*r1;
  C = sq(x0-x1) + sq(y0-y1) - sq(r1);

  if (A > 0)
    r = (-B + sqrt(sq(B) - 4*A*C)) / (2*A);
  else
    r = (-B - sqrt(sq(B) - 4*A*C)) / (2*A);
  x = xr*r + x0;
  y = yr*r + y0;
  
  cout << x << " " << y << " " << r << endl;
  cout << sqrt(sq(x-x1) + sq(y-y1)) + r1 << endl;
  cout << sqrt(sq(x-x2) + sq(y-y2)) + r2 << endl;
  cout << sqrt(sq(x-x3) + sq(y-y3)) + r3 << endl;
  
}

int main(void)
{
  int C; cin >> C;
  for (int c = 1; c <= C; c++) {
    int N; cin >> N;
    vector <double> x(N), y(N), r(N);
    double maxr = 0;
    for (int i = 0; i < N; i++) {
      cin >> x[i] >> y[i] >> r[i];
      maxr >?= r[i];
    }

    double ans = 1e9;
    if (N <= 2) ans = maxr;
    else {
      for (int i = 0; i < N; i++)
	for (int j = i+1; j < N; j++) {
	  double r3 = r[0]+r[1]+r[2]-r[i]-r[j];
	  ans = min(ans, max((hypot(x[i]-x[j], y[i]-y[j]) + r[i] + r[j]) / 2,
			     r3));
	}
    }

    /*
    for (int i = 0; i < N; i++)
      for (int j = i+1; j < N; j++)
	hypot(x[i]+x[j], y[i]+y[j]) + r[i] + r[j];

    double xc, yc, rc;
    circ_center(0, 0, 1,
		10, 0, 1,
		0, 20, 3,
		xc, yc, rc);
    
    */

    printf("Case #%d: %.6f\n", c, ans);
  }
}
