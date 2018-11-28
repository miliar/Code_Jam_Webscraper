#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <stdio.h>
#include <set>
#include <assert.h>
using namespace std;
int v[1001];
int main() {
  int nocases;
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i)
      cin >> v[i];
    int xo = 0;
    for (int i = 0; i < n; ++i)
      xo ^= v[i];
    if (xo) {
      printf("Case #%d: NO\n", rr);
      continue;
    }
    int best = -1;
    for (int m = 1; m+1 < 1<<n; ++m) {
      int x = 0, xx = 0, y = 0;
      for (int i = 0; i < n; ++i) 
	if (m&(1<<i))
	  x ^= v[i], y += v[i];
	else
	  xx ^= v[i];
      if (x == xx)
	best = max(best, y);
    }
    if (best == -1)
      printf("Case #%d: NO\n", rr);
    else
      printf("Case #%d: %d\n", rr, best);
  }
  return 0;
}
