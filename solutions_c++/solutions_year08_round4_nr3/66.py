#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <numeric>
#include "MyLib.h"

using namespace std;
int col = 27;

double best;

int n;
int x[1001], y[1001], z[1001], p[1001];
double eps = 1e-8;

double Abs(double x)
{
  if (x > 0)
    return x;
  else
    return -x;
}

double getans(double ax, double ay, double az)
{
  double bbest, ans;
  int i;
  bbest = 0;

//  cout << ax << ' ' << ay << ' ' << az << endl;

  for (i = 0; i < n; i++)
  {
    ans = Abs(x[i] - ax) + Abs(y[i] - ay) + Abs(z[i] - az);
    ans /= p[i];

    if (ans > best)
      return ans;

    if (ans > bbest)
      bbest = ans;
  }

  return bbest;
}

int main()
{
  long long i, j, ans, t_count, test, tmp, round;
  double u, stepx, stepy, stepz, lx, ly, lz, rx, ry, rz, ax, ay, az, bx, by, bz, savebest;

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> t_count;
  for (test = 0; test < t_count; test++)
  {
    cout << "Case #" << test + 1 << ": ";

    lx = ly = lz = rx = ry = rz = 0;

    cin >> n;
    Cin
    {
      cin >> x[i] >> y[i] >> z[i] >> p[i];
      if (x[i] > rx) 
        rx = x[i];
      if (x[i] < lx)
        lx = x[i];

      if (y[i] > ry) 
        ry = y[i];
      if (y[i] < ly)
        ly = y[i];

      if (z[i] > rz) 
        rz = z[i];
      if (z[i] < lz)
        lz = z[i];
    }

//    cout << rx << ' ' << lx << endl;
    rx += 1;
    lx -= 1;
    ry += 1;
    ly -= 1;
    rz += 1;
    lz -= 1;

    savebest = 0;


    for (round = 0; round < 10; round++)
    {
     best = 10000000;
      
      stepx = (rx - lx) / col;
      stepy = (ry - ly) / col;
      stepz = (rz - lz) / col;

//      cout << "*** " << stepx << ' ' << stepy << ' ' << stepz << endl;

      for (ax = lx; ax <= rx; ax += stepx)
      for (ay = ly; ay <= ry; ay += stepy)
      for (az = lz; az <= rz; az += stepz)
      {
        u = getans(ax, ay, az);

        if (u < best)
        {
          best = u;
          bx = ax;
          by = ay;
          bz = az;
        }

      }

      lx = bx - stepx;
      rx = bx + stepx;

      ly = by - stepy;
      ry = by + stepy;

      lz = bz - stepz;
      rz = bz + stepz;

//      cout << round << endl;

      if (Abs(savebest - best) < eps)
        break;

       savebest = best;

//       if (best < eps)
//         break;
    }

    printf("%.6lf", best);

    cout << endl;
  }

  return 0;
}