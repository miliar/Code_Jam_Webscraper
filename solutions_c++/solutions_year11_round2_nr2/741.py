#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

typedef long long llint;
const double EPS = 1e-9;

vector< int > P;

int main(void)
{
  int T; scanf("%d", &T);

  for (int t = 1; t <= T; ++t) 
  {
    int C;
    double D;
    scanf("%d %lf", &C, &D);

    P.clear();
    for (int i = 0; i < C; ++i) {
      int p, v; 
      scanf("%d %d", &p, &v);
      for (int j = 0; j < v; ++j)
        P.push_back(p);
    }

    double lo = 0;
    double hi = 1e15;

    while (hi - lo > EPS) {
      double mid = (lo + hi) / 2;

      double last = -1e15;
      int fail = 0;
      for (int i = 0; i < P.size(); ++i) {
        if (last + D > P[i] + mid) {
          fail = 1;
          break;
        }
        if (last + D < P[i]) 
          last = max(last + D, P[i] - mid);
        else 
          last = last + D;
      }

      if (fail) 
        lo = mid; 
      else hi = mid;
    }

    printf("Case #%d: %.7lf\n", t, lo);
  }

  return 0;
}
