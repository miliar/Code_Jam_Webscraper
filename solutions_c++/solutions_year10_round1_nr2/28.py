#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

const int MAX = 300;
const int VAL = 256;

int del, ins, m, n;
int arr[MAX];
int dp[MAX][MAX];

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    scanf("%d%d%d%d", &del, &ins, &m, &n);
    for (int i=0; i<n; i++){
      scanf("%d", &arr[i]);
    }
    memset(dp, 0x3F, sizeof(dp));
    dp[0][VAL] = del;
    for (int v=0; v<VAL; v++){
      dp[0][v] = min(abs(arr[0] - v), del + ins);
    }
    for (int i=1; i<n; i++){
      dp[i][VAL] = dp[i-1][VAL] + del;
      for (int need=0; need<VAL; need++){
        // have = VAL
        dp[i][need] = dp[i-1][VAL] + min(abs(arr[i] - need), del + ins);
        //if (i==1 && need==7) printf("%d\n", dp[i][need]);
        for (int have=0; have<VAL; have++){
          if (m == 0 && have != need) continue;
          int diff = abs(need - have);
          int toins;
          if (diff == 0) toins = 0;
          else toins = ((diff - 1) / m) * ins;
          toins += dp[i-1][have];
          int toch;
          // leave
          toch = abs(arr[i] - need);
          if (toins + toch < dp[i][need]) dp[i][need] = toins + toch;
          // del + add
          toch = (need == have) ? del : del + ins;
          if (toins + toch < dp[i][need]) dp[i][need] = toins + toch;
          //if (i==1 && need==7) printf("%d %d\n", have, dp[i][need]);
        }
        //printf("%d %d %d\n", i, need, dp[i][need]);
      }
    }
    int ans = 1<<30;
    for (int i=0; i<=VAL; i++){
      if (dp[n-1][i] < ans) ans = dp[n-1][i];
    }
    printf("Case #%d: %d\n", t, ans);
    fflush(stdout);
  }
  
  return 0;
}
