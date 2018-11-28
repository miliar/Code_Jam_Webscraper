#include <iostream>
#include <math.h>

using namespace std;

double eps = 1e-12;
double pi = 3.1415926535897932;

double Abs(double x)
{
  if (x > 0)
    return x;
  else
    return -x;
}

int inside(double r, double x, double y)
{
  if (x * x + y * y < r * r - eps)
    return 1;
  else
    return 0;
}

double find_deg(double r, int type, double x)
{
//  cout << "??? " << r << ' ' << x << ' ' << type << ' ' << x / r << endl;
  if (x >= r)
    x = r;

//  cout << "+++ " << acos(x / r) << ' ' << asin(x / r) << endl;

  if (type == 0)
    return acos(x / r);
  else
    return asin(x / r);
}

double get_sq(double r, double a, double b)
{
  double x1, y1, x2, y2;

  x1 = r * cos(a);
  y1 = r * sin(a);
  x2 = r * cos(b);
  y2 = r * sin(b);

  return (r * r * Abs(b - a) - r * r * sin(Abs(b - a)) + Abs((x2 - x1) * (y2 - y1))) / 2;
}
                            
double sq(double r, double xx, double yy, double a)
{
  double x[4], y[4], aa, bb, bonus = 0, seg;
  int use[4], i;

  x[0] = x[1] = xx - a / 2;
  x[2] = x[3] = xx + a / 2;

  y[0] = y[3] = yy - a / 2;
  y[1] = y[2] = yy + a / 2;

  for (i = 0; i < 4; i++)
    use[i] = inside(r, x[i], y[i]);

  if (use[0] == 0)
    return 0;

  if (use[2] == 1)
    return a * a;

/*  for (i = 0; i < 4; i++)
    cout << use[i] << ' ';
  cout << endl;*/

  if (use[1] == 0 && use[3] == 0)
  {
    aa = find_deg(r, 0, x[0]);
    bb = find_deg(r, 1, y[0]);
    bonus = 0;
  }

  if (use[1] == 1 && use[3] == 0)
  {
    aa = find_deg(r, 1, y[1]);
    bb = find_deg(r, 1, y[0]);
    bonus = a * (r * cos(aa) - x[0]);
  }

  if (use[1] == 0 && use[3] == 1)
  {
    aa = find_deg(r, 0, x[0]);
    bb = find_deg(r, 0, x[3]);
    bonus = a * (r * sin(bb) - y[0]);
  }

  if (use[1] == 1 && use[3] == 1)
  {
    aa = find_deg(r, 1, y[1]);
    bb = find_deg(r, 0, x[3]);
    bonus = a * (r * cos(aa) - x[0]) + a * (r * sin(bb) - y[0]) - (r * cos(aa) - x[0]) * (r * sin(bb) - y[0]);
  }

  seg = get_sq(r, aa, bb);
//  cout << "A = " << a << " a = " << aa << "  b = " << bb << " r = " << r << "  x3 = " << x[0] << "  y0 = " << y[0] << endl;
//  cout << "seg = " << seg << ' ' << "bonus = " << bonus << endl;

  return seg + bonus;
}

int main()
{
  int i, j, n;
  double x, y, a, r0, f, R, t, r, g, s0, s, d;

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> n;

//  cin >> x >> y >> a >> r;
//  cout << sq(r, x, y, a);

  for (i = 0; i < n; i++)
  {
//    cout << "Test " << i << endl;

    cin >> f >> R >> t >> r >> g;

    s0 = R * R * pi / 4;
    s = 0;

    R = R - t - f;
    r += f;
    g -= 2 * f;

    if (r >= R - eps || g <= eps)
    {
  //    cout << "1.000000" << endl;
      s = 0;
      printf("Case #%d: %.6lf\n", i + 1, 1 - s / s0);
      continue;
    }

    d = 2 * r + g;  

//    cout << R << ' ' << r << ' ' << g << endl;

    x = 0;
    while (x < R + 2 * d)
    {
      y = 0;
      while (y < R + 2 * d)
      {
        s += sq(R, x + d / 2, y + d / 2, g);
//        cout << "R = " << R << " g = " << g << endl;
//        cout << "x = " << x + d / 2 << "  y = " << y + d / 2 << "  sq = " << sq(R, x + d / 2, y + d / 2, g) << endl;
        y += d;
      }
      x += d;
    }
    
    printf("Case #%d: %.6lf\n", i + 1, 1 - s / s0);
  }

  return 0;
}