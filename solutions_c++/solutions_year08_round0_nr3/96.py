// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

double f,R,t,r,g;

inline bool out(double x, double y) { return x*x + y*y >= R*R; }

inline double bsearchx(double x1, double x2, double y) { 
  for (int i=0; i<60; i++) {
    double x3 = (x1+x2)/2;
    if (out(x3,y)) x2=x3; else x1=x3;
  }
  return (x1+x2)/2;
}

inline double primitive(double x) {
  double res = 0.5*( R*R*atan( x / sqrt(R*R-x*x) ) + x * sqrt(R*R-x*x) );
  return res;
}

inline double integrate(double x1, double x2) { return primitive(x2) - primitive(x1); }

double solve(double x1, double y1, double x2, double y2) {
  double res=0;
  if (out(x1,y2)) {
    double x3 = x2;
    if (out(x2,y1)) x3 = bsearchx(x1,x2,y1);
    res=integrate(x1,x3) - (x3-x1)*y1;
  } else {
    double x3 = bsearchx(x1,x2,y2);
    double x4 = x2;
    if (out(x2,y1)) x4 = bsearchx(x3,x2,y1);
    res=(x3-x1)*(y2-y1) + integrate(x3,x4) - (x4-x3)*y1;
  }
  return res;
}

int main() {
  int N;
  cin >> N;
  for (int n=1; n<=N; n++) {
    cin >> f >> R >> t >> r >> g;
    double area = M_PI * R * R;
    r += f; g -= 2*f;
    R -= t; R -= f;
    if (g <= 1e-8) { printf("Case #%d: %.10f\n",n,1.); continue; }
    double free_area = 0;
    for (int i=0; ; i++) {
      if (out(r+i*(g+2*r),r)) break;
      for (int j=0; ; j++) {
        if (out(r+i*(g+2*r),r+j*(g+2*r))) break;
        if (!out(r+i*(g+2*r)+g,r+j*(g+2*r)+g)) { free_area += g*g; continue; }
        free_area += solve(r+i*(g+2*r),r+j*(g+2*r),r+i*(g+2*r)+g,r+j*(g+2*r)+g);
      }
    }
    printf("Case #%d: %.10f\n",n,1. - (4.*free_area / area)); 
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
