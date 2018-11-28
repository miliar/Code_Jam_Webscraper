#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <vector>
#include <cstdint>
#include <cstdio>
#include <map>
#include <cmath>

using namespace std;

namespace {
inline pair<double, double> dist(int mx, int my, int mz, int mvx, int mvy, int mvz, int denom) {
  double x = static_cast<double>(mx)/denom;
  double y = static_cast<double>(my)/denom;
  double z = static_cast<double>(mz)/denom;
  double vx = static_cast<double>(mvx)/denom;
  double vy = static_cast<double>(mvy)/denom;
  double vz = static_cast<double>(mvz)/denom;
  
  //double td = (vx-x)*(vx-x) + (vy-y)*(vy-y) + (vz-z)*(vz-z);
  double t;
  t = 0.0f;
  if (mvx != 0 || mvy != 0 || mvz != 0) {
    double td = vx*vx+vy*vy+vz*vz;
    t = -(x*vx + y*vy + z*vz) / td;
    
    t = max(0.0, t);
  }
  
  double d;
  double xd = x+vx*t;
  double yd = y+vy*t;
  double zd = z+vz*t;
  d = sqrt(xd*xd+yd*yd+zd*zd);
  return make_pair(t, d);
}
}

int main(int argc, char *argv[]) {
  int ntrials = 0;
  scanf("%d\n", &ntrials);
  for (int i = 1; i <= ntrials; ++i) {
    int ncases = 0;
    scanf("%d\n", &ncases);
    int mx = 0, my = 0, mz = 0;
    int mvx = 0, mvy = 0, mvz = 0;
    for (int j = 0; j < ncases; ++j) {
      int x, y, z, vx, vy, vz;
      scanf("%d %d %d %d %d %d\n", &x, &y, &z, &vx, &vy, &vz);
      mx += x; my += y; mz += z;
      mvx += vx; mvy += vy; mvz += vz;
    }
    pair<double, double> d = dist(mx, my, mz, mvx, mvy, mvz, ncases);
    cout << "Case #" << i << ": "
         << fixed << setprecision(8)
         << d.second << " " <<  d.first << '\n';
  }
  return 0;
}

