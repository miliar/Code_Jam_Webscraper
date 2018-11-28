#include <algorithm>
#include <functional>
#include <iterator>
#include <numeric>
#include <limits>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cassert>
using namespace std;

#define REP(i, n)      for (int (i) = 0, __n = (int)(n); (i) < __n; ++(i))
#define REPS(i, s, n)  for (int (i) = (s), __n = (int)(n); (i) < __n; ++(i))
#define REPD(i, n)     for (int (i) = (n); (i) >= 0; --(i))
#define FOREACH(i, x)  for (typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define SIZE(x)        (int)((x).size())

const int MAXN = 10010;

int d[MAXN], l[MAXN];
int best[MAXN];
int N;

int main() {
  int T; scanf("%d", &T);
  REP(tc, T) {
    scanf("%d", &N);
    REP(i, N) scanf("%d%d", &d[i], &l[i]);
    scanf("%d", &d[N]); l[N] = numeric_limits<int>::max() / 2;

    memset(best, -1, sizeof(best));
    best[0] = 0;

    REP(i, N) if (best[i] != -1) {
      int L = d[i] - best[i];
      REPS(j, i+1, N+1) {
        if (d[j] - d[i] > L) break;

        int D = max(d[i], d[j] - l[j]);
        if (best[j] == -1 || D < best[j]) best[j] = D;
      }
    }

    printf("Case #%d: %s\n", tc+1, best[N] != -1 ? "YES" : "NO"); fflush(stdout);
  }

  return EXIT_SUCCESS;
}
