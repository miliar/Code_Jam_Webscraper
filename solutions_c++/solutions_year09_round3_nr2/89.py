
#include <cmath>
#include <iostream>
#include <cstdio>

using namespace std;

int Solve()
{
  int nN;

  cin >> nN;

  double sx = 0, svx = 0, sy = 0, svy = 0, sz = 0, svz = 0;

  for (int i = 0; i < nN; i++)
    {
      double x, y, z, vx, vy, vz;
      cin >> x >> y >> z >> vx >> vy >> vz;

      sx += x; 
      sy += y;
      sz += z;

      svx += vx;
      svy += vy;
      svz += vz;
    }

  //printf("\n%f %f %f %f %f %f\n", sx, sy, sz, svx, svy, svz);

  double sv = (svx * svx + svy * svy + svz * svz);
  double t;

  if (sv != 0.0)
    t = -(sx * svx + sy * svy + sz * svz) / sv;
  else
    t = 0;

  if (t < 0)
    t = 0;

  double rx = (sx + svx * t);
  double ry = (sy + svy * t);
  double rz = (sz + svz * t);

  double dd = sqrt(rx * rx + ry * ry + rz * rz) / double(nN);

  printf("%.7f %.7f\n", dd, t);

  return 0;
}

int main()
{
  freopen("o.txt", "w", stdout);

  int nTC;
  cin >> nTC;
  for (int nC = 1; nC <= nTC; nC++)
    {
      printf("Case #%d: ", nC);
      Solve();
    }

  return 0;
}
