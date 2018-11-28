#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cmath>
#include <set>
#include <memory.h>

using namespace std;

#define eps 1e-9
#define mp make_pair
#define pb push_back

typedef long double dbl;

#define maxn 1010

int T;
int x, s, r, t, n;

int b[maxn], e[maxn], w[maxn];

set <int> xset;
int xs[maxn];
int nx;

int st, fi;
dbl d[maxn];

int rev[maxn];

int main() {
  scanf("%d", &T);
  for (int qn = 1; qn <= T; qn++) {
    scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
    e[0] = 0;
    for (int i = 1; i <= n; i++) {
      scanf("%d%d%d", &b[i], &e[i], &w[i]);
    }

    dbl res = 0;

    dbl rest = t;
    b[n + 1] = x;
    for (int i = 1; i <= n + 1; i++) {
      dbl cur = (b[i] - e[i - 1]) * 1.0 / r;
      if (rest < cur) {
        res += rest + (b[i] - rest * r - e[i - 1]) * 1.0 / s;
        rest = 0;
      } else {
        rest -= cur;
        res += cur;
      }
    }

    memset(d, 0, sizeof(d));
    for (int it = 0; it < n; it++) {
      int mini = -1;
      for (int i = 1; i <= n; i++) {
        if (!d[i] && (mini == -1 || w[i] < w[mini])) {
          mini = i;
        }
      }

      int i = mini;
      d[i] = 1;
      dbl cur = (e[i] - b[i]) * 1.0 / (r + w[i]);
      if (rest < cur) {
        res += rest + (e[i] - rest * (r + w[i]) - b[i]) * 1.0 / (s + w[i]);
        rest = 0;
      } else {
        rest -= cur;
        res += cur;
      }
    }

    printf("Case #%d: %.10lf\n", qn, (double)res);
  }

  return 0;
}