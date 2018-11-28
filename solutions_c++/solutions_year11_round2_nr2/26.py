#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <queue>
#include <cctype>
using namespace std;

typedef long double Real;

const Real o = 1e-7;
const Real pi = acos(-1.0);

const int max_n = 256;

int n, T, I;
Real d;
int v[max_n], p[max_n];
Real minp1[max_n], maxp1[max_n];
Real ans;

void input() {
  cin >> n >> d;
  for (int i = 0; i < n; ++i) {
    cin >> p[i] >> v[i];
  }
}

bool ok(Real t) {
  for (int i = 0; i < n; i++) {
    minp1[i] = p[i] - t;
    if (i > 0)
      minp1[i] = max(minp1[i], maxp1[i - 1] + d);
    if (minp1[i] > p[i] + t + o)
      return false;
    maxp1[i] = minp1[i] + (v[i] - 1) * d;
    if (maxp1[i] > p[i] + t + o)
      return false;
  }
  return true;
}

void solve() {
  Real low = 0, high = 1e+100;
  /*
  for (int i = 0; i < n; i++)
    high += v[i];
  high *= d;
  */
  while (high - low > o) {
    Real mid = (low + high) / 2;
    if (ok(mid))
      high = mid;
    else
      low = mid;
  }
  ans = (low + high) / 2;
}

void output() {
  printf("Case #%d: %.10Lf\n", I + 1, ans);
  fprintf(stderr, "Case #%d: %.10Lf\n", I + 1, ans);
}

int main() {
  cin >> T;
  for (I = 0; I < T; ++I) {
    input();
    solve();
    output();
  }
	return 0;
}

