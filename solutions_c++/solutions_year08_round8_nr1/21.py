#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>

#define eps 1e-12

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define sz(v)((v).size())

#define task_name "a"


using namespace std;

struct pnt 
{
  double x, y;
  pnt(double _x = 0, double _y = 0)
  {
    x = _x, y = _y;
  }
  void read()
  {
    cin >> x >> y;
  }
  double d()
  {
    return sqrt(x * x + y * y);
  }
  pnt& operator *= ( double t )
  {
    x *= t;
    y *= t;
    return *this;
  }

  void rot( double co, double si )
  {
    double a = x * co - y * si, b = x * si + y * co;
    x = a;
    y = b;
  }

};

pnt operator - ( pnt a, pnt b )
{
  return pnt(a.x - b.x, a.y - b.y);
}

double operator * ( pnt a, pnt b )
{
  return a.x * b.y - a.y * b.x;
}

bool ok( double a, double b, double c, double a1, double b1, double c1)
{
  return a < a1 - eps || a < a1 + eps && (
         b < b1 - eps || b < b1 + eps && (
         c < c1 - eps
  ));
}

void update( pnt &a, pnt &b, pnt &c )
{
  if ((b - a) * (c - a) < -eps)
    swap(b, c);
  
  pnt ra = a, rb = b, rc = c;
  for (int t = 0; t < 3; t++)
  {
    double ab = (a - b).d(), bc = (b - c).d(), ac = (c  - a).d();
    double rab = (ra - rb).d(), rbc = (rb - rc).d(), rac = (rc  - ra).d();
    if (!ok(rab, rbc, rac, ab, bc, ac))
      ra = a, rb = b, rc = c;
    pnt t = a;
    a = b;
    b = c;
    c = t;
  }
  a = ra;
  b = rb;
  c = rc;
}

int main( void )
{
  freopen(task_name ".in", "r", stdin);
  freopen(task_name ".out", "w", stdout);

  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);
    pnt a1, b1, c1,  a2, b2, c2;
    a1.read();
    b1.read();
    c1.read();
    a2.read();
    b2.read();
    c2.read();
    update(a1, b1, c1);
    update(a2, b2, c2);
    double k = (b1 - a1).d() / (b2 - a2).d();
    double a = 1, b = 0, c = 0, d = 1, r1 = 0, r2 = 0;
    double an = atan2((b1 - a1).y, (b1 - a1).x) -  atan2((b2 - a2).y, (b2 - a2).x);
    
    double co = cos(an), si = sin(an);
//    fprintf(stderr, "%.2lf\n", si);
    a = co, b = -si;
    c = si, d = co;
    a2.rot(co, si);
    b2.rot(co, si);
    c2.rot(co, si);

    a2 *= k;
    b2 *= k;
    a *= k, b *= k, c *= k, d *= k;
    
    r1 = (a1.x - a2.x);
    r2 = (a1.y - a2.y);
    a -= 1;
    d -= 1;
  //  fprintf(stderr, "x * %2lf y * %.2lf + %.2lf  = 0\n", a, b, r1);
//    fprintf(stderr, "x * %2lf y * %.2lf + %.2lf  = 0\n", c, d, r2);
    double x = b * r2 - r1 * d, y = r1 * c - a * r2, z = a * d - b * c;
    if (fabs(z) < eps)
      printf("No solution\n");
    else
      printf("%.20lf %.20lf\n", x / z, y / z);
  }

   
  
  return 0;
}