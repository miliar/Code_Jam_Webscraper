#include <iostream>
#include <string.h>
#include <map>
#include <cstdlib>
#include <cmath>
using namespace std ;
char mline[1000] ;
double xp[1000], yp[1000], rp[1000] ;
void error(const char *s) {
  cerr << s ;
  exit(10) ;
}
struct enc {
  enc() { bm = 0 ; r = 0.0 ; }
  enc(long long _bm, double _r) {
    bm = _bm ;
    r = _r ;
  }
  long long bm ;
  double r ;
} ;
int N ;
map<long long, enc> circs ;
double mat[2][4] ;
double d2(double d1, double d2) {
  return hypot(d1, d2) ;
}
double d(int p1, int p2) {
   return hypot(xp[p1]-xp[p2], yp[p1]-yp[p2]) ;
}
void equ(int i, int j, int d) {
   mat[d][0] = 2 * (xp[j]-xp[i]) ;
   mat[d][1] = 2 * (yp[j]-yp[i]) ;
   mat[d][2] = 2 * (j - i) ;
   mat[d][3] = -(xp[i]*xp[i]-xp[j]*xp[j]+yp[i]*yp[i]-yp[j]*yp[j]-i*i+j*j) ;
}
double det2(int i, int j) {
   return mat[0][i] * mat[1][j] - mat[1][i] * mat[0][j] ;
}
double tcx, tcy ;
double threecirc(int i, int j, int k, double dij, double djk, double dki) {
// cout << "Threecirc for " << i << " " << j << " " << k << endl ;
   double tq = dij ;
   double cx = ((tq/2-i)*xp[j]+(tq/2-j)*xp[i])/(tq-i-j) ;
   double cy = ((tq/2-i)*yp[j]+(tq/2-j)*yp[i])/(tq-i-j) ;
   if (sqrt((xp[k]-cx)*(xp[k]-cx)+(yp[k]-cy)*(yp[k]-cy)) + k <=
       tq / 2) {
      tcx = cx ;
      tcy = cy ;
// cout << "Inside enclosing circle " << endl ;
      return tq ;
   }
   equ(i, j, 0) ;
   equ(j, k, 1) ;
   double det = det2(0, 1) ;
   double xr = det2(2, 1) / det ;
   double xc = det2(3, 1) / det ;
   double yr = det2(0, 2) / det ;
   double yc = det2(0, 3) / det ;
   double a = xr * xr + yr * yr - 1 ;
   double b = 2 * ((xc - xp[i]) * xr + (yc - yp[i]) * yr + i) ;
   double c = (xc - xp[i]) * (xc - xp[i]) + (yc - yp[i]) * (yc - yp[i]) - i * i ;
   double d = b * b - 4 * a * c ;
   if (d < 0) {
 cout << "Negative d " << endl ;
 cout << i << " " << xp[i] << " " << yp[i] << " " << i << endl ;
 cout << j << " " << xp[j] << " " << yp[j] << " " << j << endl ;
 cout << k << " " << xp[k] << " " << yp[k] << " " << k << endl ;
 cout << "mat[0] " << mat[0][0] << " " << mat[0][1] << " " << mat[0][2] << " " << mat[0][3] << endl ;
 cout << "mat[1] " << mat[1][0] << " " << mat[1][1] << " " << mat[1][2] << " " << mat[1][3] << endl ;
 cout << "coef " << det << " " << xr << " " << xc << " " << yr << " " << yc << endl ;
      return tq ;
   }
   double s1 = (- b - sqrt(d)) / (2 * a) ;
   double s2 = (- b + sqrt(d)) / (2 * a) ;
//   cout << "Got " << s1 << " " << s2 << endl ;
   if (s1 < 0)
      s1 = 1e20 ;
   if (s2 < 0)
      s2 = 1e20 ;
   if (s2 < s1)
      s1 = s2 ;
   if (s1 > 1e10)
      error("! broken?") ;
   tcx = s1 * xr + xc ;
   tcy = s1 * yr + yc ;
   if (2 * s1 > tq)
      return 2 * s1 ;
   return tq ;
}
double threecirc(int i, int j, int k) {
   if (i == j || i == k || j == k)
      return 0 ;
   double dij = d(i, j) + i + j ;
   double djk = d(j, k) + j + k ;
   double dki = d(k, i) + k + i ;
   if (dij > djk) {
      if (dij > dki) {
         return threecirc(i, j, k, dij, djk, dki) ;
      } else {
         return threecirc(k, i, j, dki, dij, djk) ;
      }
   } else if (djk > dki) {
      return threecirc(j, k, i, djk, dki, dij) ;
   } else {
      return threecirc(k, i, j, dki, dij, djk) ;
   }
}
double eps = 1e-8 ;
void checkcirc(double x, double y, double r, long long cbm) {
  long long bm = 0LL ;
  for (int i=0; i<N; i++) {
    double dc = d2(x-xp[i], y-yp[i]) ;
    if (dc + rp[i] <= r * (1+eps)) {
      bm |= 1LL << i ;
    }
  }
  if (cbm & ~bm)
    error("Failed to enclose defining circles") ;
  if (circs.find(bm) == circs.end())
    circs[bm] = enc(bm, r) ;
}
void consider(int i) {
  checkcirc(xp[i], yp[i], rp[i], 1LL<<i) ;
}
void consider(int i, int j) {
  double dd = d2(xp[i]-xp[j], yp[i]-yp[j]) + rp[i] + rp[j] ;
  double r = dd / 2.0 ;
  double cx = ((r - rp[i]) * xp[j] + (r - rp[j]) * xp[i]) / (dd - rp[i] - rp[j]) ;
  double cy = ((r - rp[i]) * yp[j] + (r - rp[j]) * yp[i]) / (dd - rp[i] - rp[j]) ;
  checkcirc(cx, cy, r, ((1LL<<i)|(1LL<<j))) ;
}
void consider(int i, int j, int k) {
  double r = threecirc(i, j, k) ;
  double cx = tcx ;
  double cy = tcy ;
  checkcirc(cx, cy, r, ((1LL<<i)|(1LL<<j)|(1LL<<k))) ;
}
int main(int argc, char *argv[]) {
  fgets(mline, 1000, stdin) ;
  int T = atol(mline) ;
  for (int c=1; c<=T; c++) {
    fgets(mline, 1000, stdin) ;
    N = atol(mline) ;
    for (int i=0; i<N; i++) {
      fgets(mline, 1000, stdin) ;
      int x, y, r ;
      if (sscanf(mline, "%d %d %d", &x, &y, &r) != 3) {
	cerr << "Fail" << endl ;
	exit(10) ;
      }
      xp[i] = x ;
      yp[i] = y ;
      rp[i] = r ;
    }
    circs.clear() ;
    for (int i=0; i<N; i++)
      consider(i) ;
    for (int i=0; i<N; i++)
      for (int j=0; j<i; j++)
	consider(i, j) ;
    for (int i=0; i<N; i++)
      for (int j=0; j<i; j++)
	for (int k=0; k<j; k++)
	  consider(i, j, k) ;
    double r = 1e10 ;
    long long all = (1LL << N) - 1 ;
    for (map<long long, enc>::iterator i1 = circs.begin(); i1 != circs.end(); i1++) {
      enc &e = i1->second ;
      if (e.r >= r)
	continue ;
      for (map<long long, enc>::iterator i2 = circs.begin(); i2 != circs.end(); i2++) {
	enc &e2 = i2->second ;
	if (e2.r < r && (e2.bm | e.bm) == all)
	  r = max(e.r, e2.r) ;
      }
    }
    cout << "Case #" << c << ": " << r << endl ;
  }
}
