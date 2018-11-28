#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define DEBUG(format, args...) { fprintf(stderr, format, ## args); fflush(stderr); }
#define PRINT(format, args...) { fprintf(stdout, format, ## args); DEBUG(format, ## args); }

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

const int MOD=10007;

bool rk[107][107];
int dp[107][107];

int main() {
  int i, x, y, X, Y, R, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d %d", &X, &Y, &R);
    memset(rk, 0, sizeof rk);
    for (i=0; i<R; i++) {
      scanf("%d %d", &x, &y);
      rk[x-1][y-1]=1;
    }
    memset(dp, 0, sizeof dp);
    dp[0][0]=1;
    for (x=0; x<X; x++)
      for (y=(x==0); y<Y; y++)
        if (!rk[x][y]) {
          if (x>=2 && y>=1)
            dp[x][y]+=dp[x-2][y-1];
          if (y>=2 && x>=1)
            dp[x][y]+=dp[x-1][y-2];
          while (dp[x][y]>=MOD)
            dp[x][y]-=MOD;
        }
    PRINT("Case #%d: %d\n", t, dp[X-1][Y-1]);
  }
  return 0;
}
