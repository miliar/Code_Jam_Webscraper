#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <time.h>
#include <cmath>
#include <cassert>
using namespace std;

typedef long long ll;

int main() {
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int tests; scanf("%d", &tests);
  for(int t = 1; t <= tests; t++) {
    printf("Case #%d: ", t);
    int n; scanf("%d", &n);
    int sum = 0, min_x = (int)1e7, xsum = 0;
    for(int j = 0; j < n; j++) {
      int d; scanf("%d", &d);
      sum += d;
      min_x = min(min_x, d);
      xsum ^= d;
    }
    if(xsum) puts("NO");
    else printf("%d\n", sum - min_x);
  }

}
