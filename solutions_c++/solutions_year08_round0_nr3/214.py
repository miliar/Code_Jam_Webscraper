#include <iostream>
#include <cmath>

using namespace std;

const double eps = 1e-11;
const double pi = 3.1415926535897932384626433832795;

double f, R, t, r, g, ans, fs, fr, si, nr, x, y;
int i, j, ntc, ttc;

inline double sqr(double x) { return x*x; }
inline double in_(double x, double y) { return (nr-hypot(x, y)>eps); }

double seg(double x1, double y1, double x2, double y2)
{
    return 0.5*(sqr(nr)*acos((2.0*sqr(nr)-sqr(x1-x2)-sqr(y1-y2))/2.0/sqr(nr))-abs(x1*y2-x2*y1));
}

double calc(double xl, double yl)
{
   if (!in_(xl, yl)) return 0.0; else {
      double xu=xl+si, yu=yl+si;
       bool i2=in_(xl, yu), i3=in_(xu, yu), i4=in_(xu, yl);
      if (i2 && i4 && i3) return sqr(si); else
      if (i2 && i4) {
         double sx=sqrt(sqr(nr)-sqr(yu)), ty=sqrt(sqr(nr)-sqr(xu));
           return sqr(si)+seg(sx, yu, xu, ty)-0.5*(xu-sx)*(yu-ty);
      } else
      if (i2) {
         double sx=sqrt(sqr(nr)-sqr(yu)), tx=sqrt(sqr(nr)-sqr(yl));
           return seg(sx, yu, tx, yl)+0.5*si*(tx+sx-2*xl);
      } else
      if (i4) {
         double sy=sqrt(sqr(nr)-sqr(xl)), ty=sqrt(sqr(nr)-sqr(xu));
           return seg(xl, sy, xu, ty)+0.5*si*(sy+ty-2*yl);
     } else {
         double tx=sqrt(sqr(nr)-sqr(yl)), sy=sqrt(sqr(nr)-sqr(xl));
           return seg(tx, yl, xl, sy)+0.5*(sy-yl)*(tx-xl);
      }
   }
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
     scanf("%d", &ntc);
   for(ttc=1; ttc<=ntc; ttc++) {
      scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
     if (g/2.0-f<eps || R-t-f<eps) ans=1.0; else {
          fs=pi*sqr(R);
          fr=0.0;
          si=g-2.0*f;
          nr=R-t-f;  i=0;
        for(i=0; r+double(i)*(2.0*r+g)+f<nr; i++)
          for(j=0; r+double(j)*(2.0*r+g)+f<nr; j++)
            fr+=calc(r+double(i)*(2.0*r+g)+f, r+double(j)*(2.0*r+g)+f);
             ans=(fs-4.0*fr)/fs;
     }
       printf("Case #%d: %.6lf\n", ttc, ans);
   }
       return 0;
}
