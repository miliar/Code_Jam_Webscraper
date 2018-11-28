
//Written by Alex Hamed Ahmadi - alex@hamedahmadi.com
//Compiler used: g++ (GCC) 3.4.5 (mingw-vista special r3)

#include <algorithm>
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
#include <cmath>
#include <complex>

using namespace std;

#define FOR(i,n) for (int i=0;i<(n);i++)
#define FORIT(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define P(x) cerr<<#x<<" = "<<x<<endl;
#define pb push_back

const int maxn=50;

typedef complex <double> Point;

struct Circle {
  double x, y;
  double r;
  double r1;
  Point c;
} c[maxn];
int n;

double eps=1e-8;
vector <Point> ap;

inline bool is0(double x) {
  return -eps<x && x<eps;
}
inline bool eq(double x, double y) {
  return is0(x-y);
}

bool same(const Circle &a, const Circle &b) {
  return eq(a.x, b.x) && eq(a.y, b.y) && eq(a.r, b.r);
}

bool intersect(const Circle &a, const Circle &b) {
  double dis = abs(a.c-b.c);
  if (dis+a.r+eps<b.r || dis+b.r+eps<a.r) return 0;
  if (a.r+b.r+eps<dis) return 0;
  return 1;
}

void findcross(Circle &a, Circle &b) {
  Point base=a.c;
  Point ac=a.c, bc=b.c;
  a.c-=base; b.c-=base;
  Point rot=b.c;
  double c=abs(rot);
  double x=(a.r*a.r+c*c-b.r*b.r)/(2*c);
  double y1=sqrt(a.r*a.r-x*x);
  if(a.r*a.r-x*x<0) y1 = 0;
  double y2=-y1;
  
  rot/=c;

  Point p(x, y1);
  p*=rot;
  p+=base;

  ap.push_back(p);  //p here is intersection
  
  if (!eq(y1, y2)) {
    p=Point(x,y2);
    p*=rot;
    p+=base;
    ap.push_back(p); //again, p is intersection
  }

  a.c=ac; b.c=bc;
}

bool test(Point a, Point b, double R) {
  FOR (i,n) {
    if (abs(c[i].c-a)>R-c[i].r1+eps && abs(c[i].c-b)>R-c[i].r1+eps) return false;
  }
  return true;
}

bool good(double R) {
  FOR (i,n) {
    if (R<c[i].r1) return 0;
    c[i].r=R-c[i].r1;
  }

  ap.clear();

  FOR (i,n) {
    FOR (j,n) {
      if (same(c[i], c[j])) {
	ap.push_back(c[i].c);
      } else {
	if (intersect(c[i], c[j])) {
	  findcross(c[i], c[j]);
	}
      }
    }
  }

  FORIT(it, ap) {
    FORIT(jt, ap) {
      if (test(*it, *jt, R)) return 1;
    }
  }
  return 0;
}

int main() {

  int nt;
  cin>>nt;
  for (int T=1;T<=nt;T++) {
    cin>>n;
    FOR (i,n) {
      cin>>c[i].x>>c[i].y>>c[i].r1;
      c[i].c=Point(c[i].x, c[i].y);
    }
    double lo=1;
    double hi=100000;
      
    while (hi-lo>1e-8) {
      double m=(lo+hi)/2.0;
      if (good(m)) hi=m;
      else lo=m;
    }

    double ans=(lo+hi)/2.0;
    //cout<<"Case #"<<T<<": ";
    printf("Case #%d: %.7f\n",T,ans);
  }

  return 0;
}
