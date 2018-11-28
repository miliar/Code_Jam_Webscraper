#include <algorithm>
#include <string>
#include <vector>
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

const int infinity = 100000000;

int cost[1 << 12], f[11][1 << 12];
int canmiss[1 << 12], n, startl;

int calc(int missed, int v) {
  if (f[missed][v] >= 0) return f[missed][v];

  int ret = infinity;
  if (v > startl) {
    if (canmiss[v - startl] >= missed) ret = 0;
  } else {
    ret = min(cost[v] + calc(missed, 2 * v) + calc(missed, 2 * v + 1),
              calc(missed + 1, 2 * v) + calc(missed + 1, 2 * v + 1));
  }
  return f[missed][v] = min(ret, infinity);
}

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    scanf("%i", &n);

    startl = (1 << n) - 1;

    for (int i = 1; i <= (1 << n); ++i)
      scanf("%i", &canmiss[i]);

    for (int j = n; j >= 1; --j)
      for (int i = 1; i <= (1 << (j - 1)); ++i)
        scanf("%i", &cost[i + (1 << (j - 1)) - 1]);
    memset(f, -1, sizeof(f));
    printf("Case #%i: %i\n", numcase, calc(0, 1));
  }
  return 0;
}
