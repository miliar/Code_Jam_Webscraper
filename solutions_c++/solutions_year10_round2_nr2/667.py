#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define For(i, x) for (int i=0; i<(int)(x); i++)

typedef vector<int> vi;

void calc(int n, int k, int b, int t, vi& xs, vi& ves) {
  vi can(n);
  int cnt = 0;
  For(i, n) {
    double d = b - xs[i];
    if (d/ves[i] <= t) {
      cnt++;
      can[i] = true;
    }
  }
  if (cnt < k) {
    puts("IMPOSSIBLE");
    return;
  }

  int ss = 0;
  while (k > 0) {
    if (can.back()) {
      k--;
      can.pop_back();
      continue;
    }

    if (can.size() == 1) {
      puts("IMPOSSIBLE");
      return;
    }

    bool b = false;
    for (int i = can.size()-1; i > 0; i--) {
      if (can[i-1] && can[i] == 0) {
        swap(can[i-1], can[i]);
        ss++;
        b = true;
        break;
      }
    }

    if (!b) {
      puts("IMPOSSIBLE");
      return;
    }
  }

  printf("%d\n", ss);
}

int main() {
  int ncases;
  scanf("%d", &ncases);
  For(cc, ncases) {
    int n, k, b, t;
    scanf("%d %d %d %d", &n, &k, &b, &t);

    vi xs(n), ves(n);
    For(i, n) scanf("%d", &xs[i]);
    For(i, n) scanf("%d", &ves[i]);

    printf("Case #%d: ", cc+1);
    calc(n, k, b, t, xs, ves);
  }
}
