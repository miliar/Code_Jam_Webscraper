#include <algorithm>
#include <cmath>
#include <cstdio>
#include <map>
#include <string>
#include <vector>

using namespace std;

typedef long double dbl;

#define pb push_back
#define eps 1e-11
double eps2 = 1e-3;

dbl ans, R, R_2, r, f, g, t;

dbl sqr( dbl x )
{
  return x * x;
}

bool ok( dbl x1, dbl y1 )
{
  return sqr(x1) + sqr(y1) <= R_2;
}

dbl area( dbl x1, dbl y1, dbl x2, dbl y2, int d = 0 )
{
  if (x2 - x1 < eps2 && y2 - y1 < eps2)
    return ok(0.5 * (x1 + x2), 0.5 * (y1 + y2)) ? (x2 - x1) * (y2 - y1) : 0.0;
  bool o1 = ok(x1, y1);
  bool o2 = ok(x1, y2);
  bool o3 = ok(x2, y1);
  bool o4 = ok(x2, y2);
  if (o1 && o2 && o3 && o4)
    return (x2 - x1) * (y2 - y1);
  if (!o1 && !o2 && !o3 && !o4)
    return 0.0;
//   fprintf(stderr, "area(%.3Lf,%.3Lf,%.3Lf,%.3Lf,%d), R = %.10Lf\n", x1, y1, x2, y2, d, sqrt(sqr(0.5 * (x1 + x2)) + sqr(0.5 * (y1 + y2))));
/*  if (d & 1 == 0)
    return area(x1, y1, 0.5 * (x1 + x2), y2, d + 1) + area(0.5 * (x1 + x2), y1, x2, y2, d + 1);
  else
    return area(x1, y1, x2, 0.5 * (y1 + y2), d + 1) + area(x1, 0.5 * (y1 + y2), x2, y2, d + 1);*/
  return area(x1, y1, 0.5 * (x1 + x2), 0.5 * (y1 + y2), d + 1) +
         area(x1, 0.5 * (y1 + y2), 0.5 * (x1 + x2), y2, d + 1) +
         area(0.5 * (x1 + x2), y1, x2, 0.5 * (y1 + y2), d + 1) +
         area(0.5 * (x1 + x2), 0.5 * (y1 + y2), x2, y2, d + 1);
}

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int test = 1; test <= tn; test++)
  {
    fprintf(stderr, "test = %d\n", test);
    scanf("%Lf%Lf%Lf%Lf%Lf", &f, &R, &t, &r, &g);
    g -= 2 * f;
    t += f;
    r += f;
    if (g <= eps || R - t <= eps)
      ans = 0.0;
    else
    {
      dbl total = M_PI * R * R;
      dbl good = 0.0;
      R = R - t;
      eps2 = R * 1e-5;
      R_2 = R * R;
      int n = (int)(R / (g + 2 * r)) + 2;
//       fprintf(stderr, "n = %d\n", n);
      for (int i = -n; i < n; i++)
      {
//         fprintf(stderr, "i=%d\n", i);
        for (int j = -n; j < n; j++)
        {
          dbl x1 = r + i * (g + 2 * r);
          dbl x2 = r + i * (g + 2 * r) + g;
          dbl y1 = r + j * (g + 2 * r);
          dbl y2 = r + j * (g + 2 * r) + g;
          good += area(x1, y1, x2, y2);
        }
      }
      ans = good / total;
    }
    printf("Case #%d: %.20Lf\n", test, abs(1.0 - ans));
  }
  return 0;
}
