#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>
#include <numeric>

using namespace std;

const int N = 1000;

double x[N], y[N], z[N];
double vx[N], vy[N], vz[N];

double sqr(double arg) {
  return arg * arg;
}

int main() {
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);

  int test_cases;
  cin >> test_cases;
  for (int test = 0; test < test_cases; test++) {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
      cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
    }
     double sumx = accumulate(x, x + n, 0, plus<double>());
    double sumy = accumulate(y, y + n, 0, plus<double>());
    double sumz = accumulate(z, z + n, 0, plus<double>());
    double sumvx = accumulate(vx, vx + n, 0, plus<double>());
    double sumvy = accumulate(vy, vy + n, 0, plus<double>());
    double sumvz = accumulate(vz, vz + n, 0, plus<double>());
    double A = sqr(sumvx) + sqr(sumvy) + sqr(sumvz);
    double B = 2 * (sumx * sumvx + sumy * sumvy + sumz * sumvz);
    double t = max(0.0, -(B / A / 2));
    
    double fx = 0;
    for (int i = 0; i < n; i++) {
      fx += (x[i] + t * vx[i]);
    }
    double fy = 0;
    for (int i = 0; i < n; i++) {
      fy += (y[i] + t * vy[i]);
    }
    double fz = 0;
    for (int i = 0; i < n; i++) {
      fz += (z[i] + t * vz[i]);
    }
    fx /= n;
    fy /= n;
    fz /= n;
    
    double d = sqrt(sqr(fx) + sqr(fy) + sqr(fz));

    printf("Case #%i: %.9lf %.9lf\n", test + 1, d, t);
  }

  return 0;
}