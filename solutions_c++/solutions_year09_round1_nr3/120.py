#include <algorithm>
#include <string>
#include <vector>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;
using namespace __gnu_cxx;

typedef long long ll;
const int infinity = 1000000000;

const int maxn = 40, maxp = 2000;
double ncr[maxn + 1][maxn + 1], 
       pr[maxn + 1][maxn + 1],
       f[maxn + 1];

double comb(int i, int j) {
  if (j >= 0 && j <= i) return ncr[i][j];
  else return 0;
}

int main() {
  for (int i = 0; i <= maxn; ++i)
    ncr[i][0] = ncr[i][i] = 1;
  for (int i = 1; i <= maxn; ++i)
    for (int j = 1; j < i; ++j)
      ncr[i][j] = ncr[i - 1][j] + ncr[i - 1][j - 1];

  int cases;
  scanf("%i\n", &cases);
  for (int caseno = 1; caseno <= cases; ++caseno) {
    printf("Case #%i: ", caseno);
    int c, n;
    scanf("%i%i", &c, &n);
    if (c <= n) { puts("1"); continue; }

    fill(&pr[0][0], &pr[c + 1][0], 0);
    double packs = ncr[c][n];
    for (int t = 0; t <= c; ++t)
      for (int k = 0; k <= t; ++k) {
        int numnew = t - k, numold = n - numnew;
        if (numnew >= 0 && numold >= 0)
          pr[k][t] = comb(k, numold) * comb(c - k, numnew) / packs;
      }
    pr[c][c] = 0;

    double ret = 0;
    fill(&f[0], &f[c + 1], 0);
    f[0] = 1;
    for (int rounds = 1; rounds <= maxp; ++rounds) {
      for (int i = c; i >= 0; --i) {
        f[i] *= pr[i][i];
        for (int j = 0; j < i; ++j)
          f[i] += f[j] * pr[j][i];
      }

      ret += f[c] * rounds;
    }
    printf("%lf\n", ret);
    fflush(stdout);
  }
  return 0;
}
