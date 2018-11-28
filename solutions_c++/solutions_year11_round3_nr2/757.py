#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

typedef long long llint;

const int MAXN = 1100;
const int MAXC = 1100;

llint L, B, N, C, a[MAXC];
llint dp[MAXN][MAXN];

llint min(llint A, llint B) {
  if (A < B) return A;
  return B;
}

llint max(llint A, llint B) {
  if (A > B) return A;
  return B;
}

int main(void)
{
  int T; scanf("%d", &T);

  for (int t = 1; t <= T; ++t) 
  {                                         
    scanf("%lld %lld %lld %lld", &L, &B, &N, &C);
    for (int i = 0; i < C; ++i) 
      scanf("%lld", &a[i]);

    for (int i = 0; i <= L; ++i)
      dp[0][i] = 0;

    for (int i = 1; i <= N; ++i)
      for (int j = 0; j <= min(L, i); ++j) {
        dp[i][j] = 1LL << 40;
        if (j <= i - 1) 
          dp[i][j] = dp[i - 1][j] + 2 * a[(i - 1) % C];
        if (j >= 1) {
          llint slowly = max(B - dp[i - 1][j - 1], 0LL) / 2;
          if (slowly <= a[(i - 1) % C])
            dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 2 * slowly + (a[(i - 1) % C] - slowly));
        }
      }

    llint ret = 1LL << 40;
    for (int i = 0; i <= min(L, N); ++i)
      ret = min(ret, dp[N][i]);
    printf("Case #%d: %lld\n", t, ret);
  }

  return 0;
}
