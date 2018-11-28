#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>

#define eps 1e-12


using namespace std;

double getI( double x1, double x2, double R )
{

  x1 >?= -R + eps;
  x2 <?= R - eps;
  if (x1 + eps > x2)
    return 0;
  double y1 = sqrt(R * R - x1 * x1), y2 = sqrt(R * R - x2 * x2);
  return (atan2(y1, x1) - atan2(y2, x2)) * R * R  / 2 - fabs(y1 * x2 - y2 * x1) / 2
         + (y1 + y2) * (x2 - x1) / 2;
}

double get( double x1, double x2, double y, double R )
{
  if (y < eps)
    return 0;
  if (y > R - eps)
    return getI(x1, x2, R);

  double l = -sqrt(R * R - y * y), r = -l;
  double res = 0;
  if (x2 > r)
    res += getI(max(r, x1), x2, R);
  l >?= x1;
  r <?= x2;
  if (l + eps < r)
    res += (r - l) * y;
  return res;
}

double inter( double x1, double x2, double y1, double y2, double R )
{
  return get(x1, x2, y2, R) - get(x1, x2, y1, R);
}

int main( void )
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++)
  {
    double f, R, t, r, g, allS;
    scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);


    allS = M_PI * R * R;
    R -= t;
    R -= f;
    g -= 2 * f;
    r += f;

    double res = 0;

    if (g > eps)
    {
      double side = g + 2 * r;
      double y = 0;
      while (y < R)
      {
        
        double len = 0;
        if (y + side + eps < R)
          len = sqrt(R * R - (y + side) * (y + side));
        int cnt = (int)(len / side - eps);

        res += cnt * g * g;

        double x = cnt * side;
        
        while (x * x + y * y < R * R)
        {
          double x1 = x + r, x2 = x1 + g, y1 = y + r, y2 = y1 + g;
          res += inter(x1, x2, y1, y2, R);
          x += side;
        }
        y += side;
      }
    }

    printf("Case #%d: %.20lf\n", tt, (allS - 4 * res) / allS);
  }
       
  return 0;
}
