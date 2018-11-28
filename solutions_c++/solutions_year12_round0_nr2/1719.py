#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <cctype>
#include <numeric>
using namespace std;

#define rep(i,n) for(int (i)=0; (i)<(int)(n); ++(i))
#define foreach(c,i) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)

vector<vector<int> > v[31];
bool is_surprise[31][2];
int best_result[31][2];
int t[102];
int dp[102][102]; // dp[i][j] := i番目までにおける、surpriseなスコアがjの場合における、最大の数

void f() {
  for (int i = 0; i <= 10; ++i) {
    for (int j = i; j <= 10; ++j) {
      for (int k = j; k <= 10; ++k) {
        vector<int> tv;
        tv.push_back(i);
        tv.push_back(j);
        tv.push_back(k);
        if (*max_element(tv.begin(), tv.end()) -
            *min_element(tv.begin(), tv.end()) > 2)
          continue;
        int sums = accumulate(tv.begin(), tv.end(), 0);
        v[sums].push_back(tv);
      }
    }
  }
  for (int i = 0; i <= 30; ++i) 
    if (v[i].size() == 1) v[i].push_back(v[i][0]);
  
  for (int i = 0; i <= 30; ++i) {
    for (int j = 0; j < 2; ++j) {
      vector<int> tv = v[i][j];
      is_surprise[i][j]
          = (*max_element(tv.begin(), tv.end()) -
             *min_element(tv.begin(), tv.end()) == 2) ? true : false ;
      best_result[i][j] = *max_element(tv.begin(), tv.end());
    }
  }
}

int main() {
  f();
  int T, N, S, p;
  scanf("%d", &T);
  rep(loop,T) {
    scanf("%d%d%d", &N, &S, &p);
    rep(i,N) scanf("%d",t+i);
    memset(dp, 0, sizeof dp);
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j <= S; ++j) {
        const int ti = t[i];
        for (int k = 0; k < 2; ++k) {
          if (is_surprise[ti][k]) {
            if (best_result[ti][k] >= p)
              dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1);
            else
              dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]);
          } else {
            if (best_result[ti][k] >= p)
              dp[i+1][j] = max(dp[i+1][j], dp[i][j] + 1);
            else
              dp[i+1][j] = max(dp[i+1][j], dp[i][j]);
          }
        }
      }
    }
    // rep(i,N+1) {
    //   rep(j,S+1) printf("%3d", dp[i][j]);
    //   puts("");
    // }
    // puts("==");
    printf("Case #%d: %d\n", loop+1, dp[N][S]);
  }

  return 0;
}
