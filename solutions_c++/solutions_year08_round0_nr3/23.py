#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define VI vector<int>
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const real eps = 1e-14;
const real pi = 3.14159265358979323846264338328;

real f, R, t, r, g, ans, rr;

int inCircle(real x, real y)
{
   return SQR(x) + SQR(y) < SQR(rr);
}

real segment(real x1, real y1, real x2, real y2)
{
   real d = sqrt(SQR(x2-x1) + SQR(y2-y1));
   real cosa = 1-SQR(d)/2.0/SQR(rr);
   if (cosa > 1.0-eps) cosa = 1.0-eps;
   if (cosa < -1.0+eps) cosa = -1.0+eps;
   real alfa = acosl(cosa);
   real res = SQR(rr)*alfa/2.0 - sqrt(SQR(rr)-SQR(d)/4.0)*d/2.0;
   return res;
}

void solve(real x, real y)
{
   if (inCircle(x+g, y+g)) {ans += g*g; return;}
   int a = inCircle(x+g, y), b = inCircle(x, y+g);
   if (a && b) {
      real x1 = sqrt(SQR(rr) - SQR(y+g));
      real y1 = sqrt(SQR(rr) - SQR(x+g));
      ans += g*g - (x+g-x1)*(y+g-y1)/2.0;
      ans += segment(x1, y+g, x+g, y1);
   } else if (a && !b) {
      real y1 = sqrt(SQR(rr) - SQR(x));
      real y2 = sqrt(SQR(rr) - SQR(x+g));
      ans += g*(y1+y2-2.0*y)/2.0;
      ans += segment(x, y1, x+g, y2);
   } else if (!a && b) {
      real x1 = sqrt(SQR(rr) - SQR(y));
      real x2 = sqrt(SQR(rr) - SQR(y+g));
      ans += g*(x1+x2-2.0*x)/2.0;
      ans += segment(x1, y, x2, y+g);
   } else {
      real x1 = sqrt(SQR(rr) - SQR(y));
      real y1 = sqrt(SQR(rr) - SQR(x));
      ans += (x1-x)*(y1-y)/2.0;
      ans += segment(x, y1, x1, y);
   }
}

int main()                 
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      cin >> f >> R >> t >> r >> g;
      g -= 2*f; r += f; t += f; rr = R - t;
      if (g < 0.0 || t > R)
         ans = 1.0;
      else {
         ans = 0;
         real x = r, y = r;
         while (1) {
            if (!inCircle(x,y)) break;
            while (1) {
               if (!inCircle(x,y)) break;
               solve(x,y);
               x += g+2*r;
            }
            y += g+2*r; x = r;
         }
         ans = 1.0 - 4.0*ans/(pi*R*R);
      }
      cout << "Case #" << sc << ": " << fixed << setprecision(7) << ans << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}