#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int MAXN = 128;

int nt0,nt;
int dp[MAXN][MAXN];
int n,s,p;

int main() {
  scanf(" %d", &nt0);
  for(nt=1 ; nt<=nt0 ; ++nt) {
    printf("Case #%d: ", nt);

    scanf(" %d %d %d", &n, &s, &p);

    for(int i=0 ; i<=s ; i++)
      dp[0][i] = 0;

    for(int i=1 ; i<=n ; i++) {
      int total, best;
      scanf(" %d", &total);

      // not surprising
      if(total%3 == 0) best = total/3;
      else best = total/3 + 1;
      for(int j=0 ; j<=s ; ++j)
        dp[i][j] = dp[i-1][j]+(best>=p);

      // surprising
      if(total%3 == 2) best = total/3 + 2;
      else best = total/3 + 1;
      if(best-2 < 0) best = 0;
      for(int j=0 ; j<=s-1 ; ++j)
        dp[i][j+1] = max(dp[i][j+1], dp[i-1][j]+(best>=p));
    }

    printf("%d\n", dp[n][s]);
  }

  return 0;
}
