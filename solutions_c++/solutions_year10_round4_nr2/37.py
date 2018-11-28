#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

#define maxn 10000

int dp[maxn][20], a[maxn];
int p;

int get (int v, int x) {
  if (dp[v][x] != -1) {
    return dp[v][x];
  }
  int &res = dp[v][x] = 1000000000;
  if (v >= (1 << p)) {
    if (x <= a[v]) {
      res = 0;
    }
    return res;
  }

  res = min(res, min(a[v] + get(v * 2, x) + get(v * 2 + 1, x), get(v * 2, x + 1) + get(v * 2 + 1, x + 1)));
  return res;
}

int main (void) {
  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++) {
    printf("Case #%d: ", tt);

    cin >> p;
    for (int i = p; i >= 0; i--) {
      for (int j = 0; j < (1 << i); j++) {
        cin >> a[(1 << i) + j];
        memset(dp[(1 << i) + j], -1, sizeof(dp[0]));
      }
     
    }
    cout << get(1, 0) << endl;
  }

  return 0;
} 