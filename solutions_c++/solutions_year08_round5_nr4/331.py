#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <assert.h>
#define MOD 10007
#define MAXH 100
#define MAXW 100
using namespace std;
int H, W;
char ok[MAXH][MAXW];
int dp[MAXH][MAXW];
int go(int x, int y) {
  if (x+1==H && y+1==W)
    return 1;
  if (x>=H || y>=W || !ok[x][y])
    return 0;
  int &ret = dp[x][y];
  if (ret != -1)
    return ret;
  return ret = (go(x+1,y+2) + go(x+2,y+1)) % MOD;
}
int main() {
  int no_cases;
  cin >> no_cases;
  for (int rr = 1; rr <= no_cases; ++rr) {
    int R;
    cin >> H >> W >> R;
    memset(ok, 1, sizeof(ok));
    for (int i = 0; i < R; ++i) {
      int x, y;
      cin >> x >> y;
      ok[x-1][y-1] = 0;
    }
    memset(dp, -1, sizeof(dp));
    printf("Case #%d: %d\n", rr, go(0, 0));
  }
  return 0;
}
