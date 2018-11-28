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

#define MAXN 1100

double dp[MAXN];

int main() {
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int tests; scanf("%d", &tests);
  for(int t = 1; t <= tests; t++) {
    printf("Case #%d: ", t);
    int n; scanf("%d", &n);
    int cnt = 0;
    for(int i = 0; i < n; i++) {
      int d; scanf("%d", &d);
      if(d != i + 1) cnt++;
    }
    printf("%.8lf\n", cnt + 0.);
  }

}
