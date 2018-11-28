#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>

using namespace std;

const int N = 502;
const int M = 100003;

static int nk[N][N];
static int dp[N][N];

void cmpNK() {
  nk[0][0] = 1;
  for (int i=1; i<N; ++i) {
    nk[i][0] = 1;
    for (int j=1; j<=i; ++j) {
      nk[i][j] = (nk[i-1][j-1]+nk[i-1][j]) % M;
    }
  }
}

void cmpDP() {
  for (int i=2; i<N; ++i) {
    dp[i][1] = 1;
    for (int j=2; j<i; ++j) {
      dp[i][j] = 0;
      for (int k=1; k<j; ++k) {
        dp[i][j] += dp[j][k]*nk[i-j-1][j-k-1];
        dp[i][j] %= M;
      }
    }

    dp[i][0] = 0;
    for (int j=1; j<i; ++j) {
      dp[i][0] += dp[i][j];
      if (dp[i][0] >= M) dp[i][0] -= M;
    }
  }
}

int main() {
  cmpNK();
  cmpDP();

  int t,n;
  scanf("%d",&t);
  for (int tc=1;tc<=t;++tc) {
    scanf("%d",&n);
    printf("Case #%d: %d\n",tc,dp[n][0]);
  }
  return 0;
}
