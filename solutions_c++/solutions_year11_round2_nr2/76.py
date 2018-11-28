#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool okay(int D, vector<int> pos, double t) {
  int n = pos.size();
  if (n == 0) return true;
  double lastpos = pos[0] - t;
  for (int i=1; i<n; ++i) {
    double mypos = max(lastpos+D, pos[i]-t);
    if (mypos > pos[i]+t) {
      return false;
    }
    lastpos = mypos;
  }
  return true;
}

int main() {
  cin.sync_with_stdio(0);
  int CASES; cin >> CASES;

  for (int tt=1; tt<=CASES; ++tt) {
    int C, D; cin >> C >> D;
    vector<int> pos;
    for (int i=0; i<C; ++i) {
      int P, V; cin >> P >> V;
      while (V-- > 0) {
        pos.push_back(P);
      }
    }

    double lo = 0, hi = 10e12;
    for (int iter=0; iter<100; ++iter) {
      double mid = (lo + hi) / 2;
      if (okay(D, pos, mid)) {
        hi = mid;
      } else {
        lo = mid;
      }
    }

    printf("Case #%d: %.12f\n", tt, lo);
  }

  return 0;
}
