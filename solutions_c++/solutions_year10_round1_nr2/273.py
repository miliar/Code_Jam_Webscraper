#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <assert.h>
using namespace std;
int T, D, I, M, N, dp[256][101][2][2], a[101];
int go(int last, int at, int ins, int inc) {
  if (at == N)
    return 0;
  int &ret = dp[last][at][ins][inc];
  if (ret != -1)
    return ret;
  ret = 1000000000;
  ret = min(ret, D + go(last, at+1, ins, inc));
  for (int t = max(0, last-M); t <= min(255, last+M); ++t)
    ret = min(ret, abs(a[at]-t) + go(t, at+1, 0, 0));
  if (ins) {
    if (inc)
      for (int t = last+1; t <= min(255, last+M); ++t)
	ret = min(ret, I + go(t, at, 1, inc));
    else
      for (int t = last - 1; t >= max(0, last-M); --t)
	ret = min(ret, I + go(t, at, 1, inc));
  } else {
    for (int t = max(0, last-M); t <= min(255, last+M); ++t)
      if (t != last)
	ret = min(ret, I + go(t, at, 1, t>last));
  }
  return ret;
}
int main() {
  cin >> T;
  for (int rr = 1; rr <= T; ++rr) {
    cin >> D >> I >> M >> N;
    for (int i = 0; i < N; ++i)
      cin >> a[i];
    int ans = N*D;
    memset(dp, -1, sizeof(dp));
    for (int i = 1; i <= N; ++i)
      for (int t = 0; t <= 255; ++t)
	ans = min(ans, (i-1)*D + abs(t-a[i-1]) + go(t, i, 0, 0));
    cout << "Case #" << rr << ": " << ans << endl;
  }
  return 0;
}
