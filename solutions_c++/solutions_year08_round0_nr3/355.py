#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

#define FOR(i,n) for (int i=0;i<n;i++)
#define FORI(i,s) FOR(i,(signed)s.size())
#define ld long double

ld area(ld x1, ld y1, ld x2, ld y2, ld r) {
 if (hypot(x2,y2) < r && hypot(x1,y2) < r
  && hypot(x1,y1) < r && hypot(x2,y1) < r)
  return (x2-x1)*(y2-y1);
 if (hypot(x2,y2) > r && hypot(x1,y2) > r
  && hypot(x1,y1) > r && hypot(x2,y1) > r)
  return 0;
 ld ans = 0;
 if (hypot(x1,y1) < r && hypot(x2,y1) > r) {
  ld lb=x1, ub=x2;
  FOR(zz,40) {
   ld c = (lb+ub)/2;
   if (hypot(c,y1) < r) lb=c; else ub=c;
  }
  x2 = lb;
 }
 if (hypot(x1,y2) < r && hypot(x2,y2) > r) {
  ld lb=x1, ub=x2;
  FOR(zz,40) {
   ld c = (lb+ub)/2;
   if (hypot(c,y2) < r) lb=c; else ub=c;
  }
  ans += (lb-x1) * (y2-y1);
  x1 = lb;
 }
 //printf("  %Lf %Lf %Lf %Lf %Lf\n", x1, y1, x2, y2, r);

#define N 200
#define F(x) (sqrt(r*r-(x)*(x)) - y1)
 if (fabsl(x2-x1) < 1e-8) return 0;
 ld x = x1, step = (x2-x1)/N;
 ld f = 0;
 FOR(i,N) {
  f += step * (F(x) + 4*F(x+step/2) + F(x+step))/6;
  x+=step;
 }
 //printf("  %Lf %Lf\n", f, ans);
 return f+ans;
}

void doit() {
 ld f,R,t,r,g;
 scanf("%Lf%Lf%Lf%Lf%Lf", &f, &R, &t, &r, &g);
 r+=f; g-=f+f; t+=f;
 if (g<0) g=0;
 ld area1=0, area2 = M_PI*R*R;
 FOR(i,1000) FOR(j,1000) {
  ld x1 = i*(g+r+r)+r, y1 = j*(g+r+r)+r;
  area1 += area(x1, y1, x1+g, y1+g, R-t);
 }
 printf("%.20Lf\n", 1-4*area1/area2);
}

int main() {
 int cases;
 scanf("%i", &cases);
 FOR(i,cases) {
  printf("Case #%i: ", i+1);
  doit();
 }
}
