#include<iostream>
#include<cmath>
#include<cassert>
using namespace std;

#define DX 1e-3
#define pi acos(-1.0)

double dx;

double R, g, r, 
  r2, //r+r
  g2r, //g+2*r
  R2; // R*R

double len(double x) {
  double x2 = x+r;
  x2 = fmod(x2, (g2r)) - r2;
  if (x2 <= 0) return 0;

  double y = sqrt(R2 - x*x);
  double ret = g * floor( (y+r) / (g2r) );
  double resi = fmod(y+r, (g+2*r)) - r2;
  if (resi > 0) ret += resi;
  return ret;
}

int main() {
  int cases, q;
  double f, t, whole, ans, x;
  
  cin >> cases;
  for (q = 1; q <= cases; q++) {
    cin >> f >> R >> t >> r >> g;
    whole = pi * R * R / 4;

    R -= (t+f);
    r += f;
    g -= 2*f;
    
    if (g > 0 && R > 0) {
      ans = 0;
      
      r2 = 2*r;
      g2r = g+2*r;
      R2 = R*R;
      #define test 1e7
      //printf("dx1 %.6f dx2 %.6f\n", DX, R/test);
      dx = min(DX, R/test);
      if (dx == 0) dx = max(DX, R/test);
      //printf("dx %.6f\n", dx);
      for (x = dx/2; x < R; x += dx) {
	ans += len(x) * dx;
      }
      ans = 1-(ans/whole);
    }
    else {
      ans = 1;
    }
    printf("Case #%d: %.6f\n", q, ans);
  }
  return 0;
}
