#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <assert.h>
using namespace std;
#define MAXN 42
int N, M[MAXN][MAXN];
vector<int> ok[MAXN];
int main() {
  int T;
  cin >> T;
  for (int rr = 1; rr <= T; ++rr) {
    cin >> N;
    for (int i = 0; i < N; ++i)
      ok[i] = vector<int>(N, 1);
    memset(M, 1, sizeof(M));
    for (int i = 0; i < N; ++i) {
      string s;
      cin >> s;
      for (int j = 0; j < N; ++j)
	M[i][j] = s[j] - '0';
    }
    for (int i = 0; i < N; ++i)
      for (int j = N-1; j >= 0; --j)
	if (M[i][j]) {
	  for (int k = 0; k < j; ++k)
	    ok[i][k] = 0;
	  break;
	}
    int ans = 0;
    for (int i = 0; i < N; ++i)
      if (!ok[i][i]) {
	for (int k = i + 1; k < N; ++k)
	  if (ok[k][i]) {
	    ans += k - i;
	    for (int t = k; t > i; --t)
	      swap(ok[t], ok[t-1]);
	    break;
	  }
      }
    printf("Case #%d: %d\n", rr, ans);
  }
  return 0;
}
