using namespace std;

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

#define PB push_back
#define SZ size()
#define REP(var, hi) for (int var=0; var<(hi); var++)
#define REPD(var, hi) for (int var=((hi)-1); var>=0; var--)
#define FOR(var, lo, hi) for (int var=(lo); var<(hi); var++)
#define FORD(var, lo, hi) for (int var=((hi)-1); var>=(lo); var--)

typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <string> VS;

double piece (double x, double y, double r) {

  return x*y - 0.5*x*sqrt(r*r-x*x) - 0.5*y*sqrt(r*r-y*y)
    + 0.25*M_PI*r*r - 0.5*r*r*atan(x/sqrt(r*r-x*x)) - 0.5*r*r*atan(y/sqrt(r*r-y*y));
}

double calc (double x1, double y1, double x2, double y2, double r) {

  if (y1>x1) {
    swap(x1,y1);
    swap(x2,y2);
  }

  if (x1*x1 + y1*y1 >= r*r) return 0;

  if (x1*x1 + y2*y2 >= r*r) return piece(x1,y1,r);
  
  if (x2*x2 + y1*y1 >= r*r) {
    double x = sqrt(r*r-y2*y2);
    return (x-x1)*(y2-y1) + piece(x,y1,r);
  }

  if (x2*x2 + y2*y2 >= r*r) {
    double x = sqrt(r*r-y2*y2);
    double y = sqrt(r*r-x2*x2);
    return (x-x1)*(y-y1) + (x-x1)*(y2-y) + (x2-x)*(y-y1) + piece(x,y,r);
  }
  
  return (x2-x1)*(y2-y1);
}

int main () {

  int runs;
  scanf ("%i",&runs);

  for (int run=1; run<=runs; run++) {

    double f, R, t, r, g;
    scanf ("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);

    if (g <= 2*f) {
      printf ("Case #%i: 1.000000\n",run);
      continue;
    }

    double A0 = M_PI*R*R/4;
    
    R -= t+f;
    r += f;
    g -= 2*f;

    double A=0;

    for (double x=r; x<=R; x+=g+2*r)
      for (double y=r; y<=R; y+=g+2*r)
	A += calc(x,y,x+g,y+g,R);

    printf ("Case #%i: %.6lf\n", run, (A0-A)/A0);
  }
  
  return 0;
}
