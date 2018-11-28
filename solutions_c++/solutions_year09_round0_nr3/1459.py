#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;
FILE* fin = freopen("c.in", "r", stdin);
FILE* fout = freopen("c.out", "w", stdout);

int N, dp[20];
char *S = "welcome to code jam", str[512];

int main() {
  scanf("%d ", &N);
  for (int i = 0; i < N; i++) {
    gets(str);
    memset(dp, 0, sizeof(dp));
    dp[0] = 1;
    for (char *s = str; *s; s++)
      for (int j = 0; j < 19; j++)
        if (*s == S[j]) dp[j+1] = (dp[j+1]+dp[j])%10000;
    //for (int j = 0; j < 19; j++) printf("%d ", dp[j+1]);
    //printf("\n");
    printf("Case #%d: %04d\n", i+1, dp[19]);
  }
  fclose(fout);
  //while(1); // debug
}
