#include <cassert>
#include <cmath>
#include <cctype>
#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <functional>
#include <numeric>
#include <limits>
#include <boost/bind.hpp>

using namespace std;
typedef vector<int> vi_t;
typedef vector<string> vs_t;
typedef long long i64_t;

struct ff
{
  int x, y, z, vx, vy, vz;
};

struct Position
{
  double x, y, z;
  Position() : x(0), y(0), z(0) {}
};

int main()
{
  int N; cin >> N; cin.ignore();

  for (int n = 1; n <= N; ++n)
  {
    int nff;
    cin >> nff;
    vector<ff> ffs(nff);
    for (int i = 0; i < nff; ++i)
    {
      cin >> ffs[i].x >> ffs[i].y >> ffs[i].z >> ffs[i].vx >> ffs[i].vy >>
        ffs[i].vz;
    }
    Position M0; 
    M0.x = accumulate(ffs.begin(), ffs.end(), 0,
      boost::bind(plus<int>(), _1, boost::bind(&ff::x, _2))
      ) / double(nff);
    M0.y = accumulate(ffs.begin(), ffs.end(), 0,
      boost::bind(plus<int>(), _1, boost::bind(&ff::y, _2))
      ) / double(nff);
    M0.z = accumulate(ffs.begin(), ffs.end(), 0,
      boost::bind(plus<int>(), _1, boost::bind(&ff::z, _2))
      ) / double(nff);

    Position Vel;
    Vel.x = accumulate(ffs.begin(), ffs.end(), 0,
      boost::bind(plus<int>(), _1, boost::bind(&ff::vx, _2))
      ) / double(nff);
    Vel.y = accumulate(ffs.begin(), ffs.end(), 0,
      boost::bind(plus<int>(), _1, boost::bind(&ff::vy, _2))
      ) / double(nff);
    Vel.z = accumulate(ffs.begin(), ffs.end(), 0,
      boost::bind(plus<int>(), _1, boost::bind(&ff::vz, _2))
      ) / double(nff);

    
    double p1 = (Vel.x * M0.x + Vel.y * M0.y + Vel.z*M0.z);
    double dmin, tmin = 0;
    if (p1 > numeric_limits<double>::epsilon())
    {
      dmin = sqrt(M0.x*M0.x + M0.y * M0.y + M0.z * M0.z);
    }
    else
    {
      double Velm = sqrt(Vel.x * Vel.x + Vel.y * Vel.y + Vel.z * Vel.z);
      p1 = -p1;
      double t = p1;
      if (abs(Velm) <= 0.0000000001)
      {
        dmin = sqrt(M0.x*M0.x + M0.y * M0.y + M0.z * M0.z);
      }
      else
      {
        t /= Velm;
        p1 /= Velm;
        double M0m = M0.x * M0.x + M0.y* M0.y + M0.z*M0.z; 
        dmin = M0m - p1 * p1;
        if (dmin >= 0.00000000001)
        {
          dmin = sqrt(dmin);
        }
        else
        {
          dmin = 0;
        }
        Position M1;
        M1.x = M0.x + Vel.x * t ;
        M1.y = M0.y + Vel.y * t;
        M1.z = M0.z + Vel.z * t;
        double dist = sqrt(Vel.x * t * Vel.x * t + Vel.y * t * Vel.y * t +
          Vel.z * t * Vel.z * t);
       tmin = dist / Velm / Velm;
      }
    }
    cout << "Case #" << n << ": " << fixed << setprecision(8)<< dmin << ' ' << tmin << endl;
  }
  return 0;
}
