#include <cmath>
#include <complex>
#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,v) FOR(i,(int)v.size())
#define BEND(v) v.begin(),v.end()
#define dump(x) cerr << #x << " = " << (x) << endl;
typedef complex<double> cpx;
#define X real()
#define Y imag()

const double eps = 1e-8;
double f,R,t,r,g,iR;
int cas = 0;
cpx getpos(int x, int y) {
  cpx p;
  p.X = r + x*(g+2*r);
  p.Y = r + y*(g+2*r);
  return p;
}
bool inside(cpx p) {
  return abs(p)+eps < iR;
}
cpx bsearch(cpx lo, cpx hi) {
  FOR(k,111) {
    cpx mid = 0.5*(lo+hi);
    if (inside(mid)) lo = mid;
    else hi = mid;
  }
  return lo;
}
double evalint(double x) {
  return 0.5*x*sqrt(iR*iR-x*x)
       + 0.5*iR*iR*atan2(x,sqrt(iR*iR-x*x));
}
void doit() {
  scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);

  r += f;
  g -= 2*f;
  t += f;
  iR = max(0.0, R-t);

  double A = M_PI*R*R;
  double a = 0;

  FOR(x,1024) FOR(y,1024) {
    cpx ll = getpos(x,y);
    cpx ul = getpos(x,y)+cpx(0,g);
    cpx lr = getpos(x,y)+cpx(g,0);
    cpx ur = ll+cpx(g,g);

    if (!inside(ll)) continue;

    double me;
    if (inside(ur)) {
      me = g*g;
    } else {
      double b = ll.X;
      double c = lr.X;

      if (inside(ul)) b = bsearch(ul,ur).X;
      if (!inside(lr)) c = bsearch(ll,lr).X;

      assert(ll.X <= b && b <= c && c <= lr.X);
/*
      dump(ll.X);
      dump(b);
      dump(c);
      dump(lr.X);
      dump(abs(cpx(b,ul.Y)));
      dump(abs(cpx(c,ll.Y)));
      dump(iR);*/
      double cslice = evalint(c) - evalint(b);
/*
      dump(cslice);
      dump(ll.Y*(c-b));*/
      me =
	(b-ll.X)*g
	+ cslice - ll.Y*(c-b);
    }
    //dump(x);dump(y);dump(me);
    a += me;
  }
  //dump(evalint(iR) - evalint(0));

  double ans = (A-4*a) / A;
  printf("Case #%d: %.6lf\n",++cas,ans);
}

int main() {
  int N;
  scanf("%d",&N);
  FOR(i,N) doit();
}
