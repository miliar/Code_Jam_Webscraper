#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
//typedef long long ll;

typedef long double dbl;

//inline ll sqr(ll x) { return x * x; }

void test_case()
{
  int n;
  if (scanf("%d", &n) != 1) {
    exit(0);
  }

  vector<int> x(n + 1), L(n + 1);
  for (int i = 0; i < n; ++i)
    scanf("%d%d", &x[i], &L[i]);

  scanf("%d", &x[n]);
  L[n++] = 0;

  vector<int> dp(n, -1);
  dp[0] = x[0];

  for (int i = 0; i < n - 1; ++i)
  {
    if (dp[i] <= 0)
      continue;

    for (int j = i + 1; j < n; ++j)
    {
      int dx = x[j] - x[i];
      if (dx > dp[i])
        break;

      int dy = min(dx, L[j]);
      if (dp[j] < dy)
        dp[j] = dy;
    }

//    for (int j = 0; j < n; ++j)
//      fprintf(stderr, "%d ", dp[j]);
//    fprintf(stderr, "\n");
  }

  printf("%s\n", dp[n - 1] >= 0 ? "YES" : "NO");
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T = 0;
  scanf ("%d", &T);
  for (int ti = 1; ti <= T; ++ti) {
    printf ("Case #%d: ", ti);
    test_case();
  }
  return 0;
}
