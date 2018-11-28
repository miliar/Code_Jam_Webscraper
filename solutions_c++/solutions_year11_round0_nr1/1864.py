
#include <cstdio>

int solve () {

  int n = 0;
  int dp[2][2];
  int pp[2];

  pp[0] = pp[1] = 1;
  dp[0][0] = dp[0][1] = dp[1][0] = dp[1][1] = 0;

  scanf ("%d", &n);

  int res = 0;
  for (; n--; ) {
    char flag[2];
    int pos;

    scanf ("%s%d", flag, &pos);

    int i;
    if (flag[0] == 'O')
      i = 0;
    else 
      i = 1;

    int ii = 1^i;

    //move
    int t = pos - pp[i];
    if (t < 0) t = -t;
    pp[i] = pos;

    dp[i][0] = dp[i][1] + t;

    //pass
    dp[i][1] = dp[i][0];
    if (dp[ii][1] > dp[i][1])
      dp[i][1] = dp[ii][1];
    dp[i][1]++;

    res = dp[i][1];
  }

  return res;
}

int main() {

  int TC;

  scanf ("%d", &TC);

  for (int tc = 1; tc <= TC; tc++) {
    printf ("Case #%d: %d\n", tc, solve ());
  }

  return 0;
}
