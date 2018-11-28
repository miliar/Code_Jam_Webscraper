#include <stdio.h>
#include <string.h>

char goal[] = "welcome to code jam";

int main() {
  int N, G = strlen(goal);
  scanf("%d\n", &N);
  char line[1024];
  for (int t = 1; t <= N; ++t) {
    fgets(line, 512, stdin);
    int s = strlen(line);
    int dp[G][s];
    for (int i = 0; i < s; ++i) dp[0][i] = ((line[i] == goal[0]) ? 1 : 0);
    for (int i = 1; i < G; ++i)
      for (int j = 0; j < s; ++j)
        dp[i][j] = 0;
    for (int i = 1; i < G; ++i)
      for (int j = 0, sum = 0; j < s; sum = (sum + dp[i-1][j++]) % 10000)
        if (line[j] == goal[i]) dp[i][j] = (dp[i][j] + sum) % 10000;
    int sum = 0;
    for (int i = 0; i < s; ++i) sum = (sum + dp[G-1][i]) % 10000;
    printf("Case #%d: %d%d%d%d\n", t,
           (sum/1000)%10, (sum/100)%10, (sum/10)%10, sum%10);
  }
  return 0;
}
