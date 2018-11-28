#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <utility>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

typedef double decimal;
const decimal EPS = 1e-16;

decimal CO[48][48];

decimal co(int n, int x){
  if(n < x) return 0.0;
  if(n == x) return 1.0;
  return 1.0 * n / (n-x) * co(n-1, x);
}

int nCases;
int C, N;
decimal dp[48];
decimal dp2[48];

static inline decimal mv(int i, int j){
  return CO[i][N-j] * CO[C-i][j] / CO[C][N];
}

int main(){
  REP(i, 48){
    REP(j, 48){
      CO[i][j] = co(i, j);
    }
  }
  cin >> nCases;
  REP(ic, nCases){
    cin >> C >> N;
    memset(dp, 0, sizeof(dp));
    dp[0] = 1.0;
    decimal ret = 0.0;
    if(C == N){
      ret = 1.0;
      goto shortcut;
    }
    for(int n = 1; ; n++){
      memset(dp2, 0, sizeof(dp2));
      REP(i, C+1){
        REP(j, N+1){
          if(i+j <= C){
            dp2[i+j] += dp[i] * mv(i, j);
          }
        }
      }
      memcpy(dp, dp2, sizeof(dp));
      if(dp[C] > 0 && n * dp[C] < EPS) break;
      ret += n * dp[C];
      dp[C] = 0.0;
    }
shortcut:
    printf("Case #%d: %.20f\n", ic+1, ret);
  }

  return 0;
}

