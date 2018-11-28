#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <queue>
#include <complex>
using namespace std;
#define PI 3.14159265358979323846264338327950288
#define Eps 1E-8
int T;
int N;
complex <double> cent[45];
long long covered[45][45][45];
double radii[45][45][45];
double rad[45];
inline double min(double a, double b) {
   return (a < b ? a : b);
}
inline double max(double a, double b) {
   return (a > b ? a : b);
}
int calcint(complex <double> cen1, double r1, complex <double> cen2, double r2, complex <double> s1, complex <double> s2) {
   s1 = 1E20;
   s2 = 1E20;
   if (abs(cen1 - cen2) > r1 + r2)
      return 0;
   double l = abs(cen1 - cen2);
   double ang = (r1 * r1 + l * l - r2 * r2) / (2 * r1 * l);
#define I (sqrt(-1))
   s1 = cen1 + r1 * (cen2 - cen1) / l * (ang + I * sqrt(1 - ang * ang));
   s2 = cen1 + r1 * (cen2 - cen1) / l * (ang - I * sqrt(1 - ang * ang));
   return 0;
}
int calc(int a, int b, int c, complex <double> &cen, double &res) {
   if (a == b && b == c) {
      cen = cent[a];
      res = rad[a];
      return 0;
   }
   if (a == b || b == c) {
      double l = abs(cent[a] - cent[c]);
      double p1 = l - rad[a] + rad[c];
      double p2 = l - rad[c] + rad[a];
      cen = (cent[a] * p2 + cent[b] * p1) / (p1 + p2);
      res = (l + rad[a] + rad[c]) / 2;
      return 0;
   }
   double f, r, m;
   f = max(rad[a], max(rad[b], rad[c]));
   r = 1E20;
   while (f + Eps < r) {
      m = (f + r) / 2;
      complex <double> s1, s2;
      calcint(cent[a], m - rad[a], cent[b], m - rad[b], s1, s2);
      if (abs(s1 - cent[c]) < m - rad[c] || abs(s2 - cent[c]) < m - rad[c])
	 r = m;
      else
	 f = m;
   }
   complex <double> tmp1, tmp2;
   calcint(cent[a], f - rad[a], cent[b], f - rad[b], tmp1, tmp2);
   if (abs(tmp1 - cent[c]) <= m - rad[c] + Eps)
      cen = tmp1;
   else
      cen = tmp2;
   res = f;
   return 0;
}
int main() {
   int i, j, Case = 1, k, l, m, n;
   scanf("%d", &T);
   while (T --) {
      scanf("%d", &N);
      for (i = 0; i < N; i ++)
	 scanf("%lf%lf%lf", &cent[i].real(), &cent[i].imag(), &rad[i]);
      if (N == 1) {
	 printf("Case #%d: %.10lf\n", Case ++, rad[0]);
	 continue;
      }
      for (i = 0; i < N; i ++)
	 for (j = i; j < N; j ++)
	    for (k = j; k < N; k ++) {
	       complex <double> center;
	       calc(i, j, k, center, radii[i][j][k]);
	       covered[i][j][k] = 0;
	       for (l = 0; l < N; l ++)
		  if (abs(center - cent[l]) <= radii[i][j][k] - rad[l] + Eps)
		     covered[i][j][k] += (1LL << l);
	    }
      double ans = 1E20;
      for (i = 0; i < N; i ++)
	 for (j = i; j < N; j ++)
	    for (k = j; k < N; k ++) {
	       long long left = ((1LL << N) - 1) ^ covered[i][j][k];
	       double cntr = radii[i][j][k];
	       if (cntr >= ans - Eps)
		  continue;
	       for (l = 0; l < N; l ++)
		  if (left & (1LL << l))
		     for (m = l; m < N; m ++)
			if (left & (1LL << m))
			   for (n = m; n < N; n ++)
			      if ((covered[l][m][n] & left) == left)
				 ans = min(ans, max(cntr, radii[l][m][n]));
	    }
      printf("Case #%d: %.10lf\n", Case ++, ans);
   }
   return 0;
}

