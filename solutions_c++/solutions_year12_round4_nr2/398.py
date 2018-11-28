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
typedef pair<int, int> pii;

const int MAXN = 1000;

bool   done[MAXN];
int    x[MAXN], y[MAXN];
int    r[MAXN];

int main() {
  int T; scanf("%d", &T);
  REP(tc, T) {
    vector<pii> R;
    int         N, W, L; 

    scanf("%d%d%d", &N, &W, &L);
    REP(i, N) {
      scanf("%d", &r[i]);
      R.push_back(make_pair(r[i], i));
    }

    sort(R.begin(), R.end(), greater<pii>());
    memset(done, 0, sizeof(done));

    FOREACH(it, R) {
      int lo = 0, hi = L;
      int p_x;

      while (lo < hi) {
        int p_y = (lo + hi) / 2;
        p_x = 0;

        REP(i, N) if (done[i]) {
          if (y[i] + r[i] + it->first > p_y) 
            p_x = max(p_x, x[i] + r[i] + it->first);
        }

        if (p_x <= W) hi = p_y; else lo = p_y+1;
      }

      p_x = 0; int p_y = lo;
      REP(i, N) if (done[i]) {
        if (y[i] + r[i] + it->first > p_y) 
          p_x = max(p_x, x[i] + r[i] + it->first);
      }

      assert(p_x <= W);
      assert(lo <=  L);

      done[it->second] = true;
      x[it->second]    = p_x;
      y[it->second]    = lo;
    }

    printf("Case #%d:", tc+1);
    REP(i, N) printf(" %d %d", x[i], y[i]); printf("\n"); fflush(stdout);
  }

  return EXIT_SUCCESS;
}
