#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 1000
char s[N];
const char msg[] = "welcome to code jam";
int c[N][20];
int main()
{
  int t;
  const int m = strlen(msg);
  int n;
  scanf("%d", &t);
  fgets(s, N, stdin);
  for(int index = 1; index <= t; index++) {
    fgets(s, N, stdin);
    n = strlen(s);
    for(int i = 0; i <= n; i++)
      c[i][0] = 1;
    for(int i = 1; i <= m; i++)
      c[0][i] = 0;
    for(int i = 1; i <= n; i++)
      for(int j = 1; j <= m; j++) {
        c[i][j] = c[i-1][j] + c[i-1][j-1]*(s[i-1]==msg[j-1]);
        if(c[i][j] >= 10000) c[i][j] -= 10000;
      }
    printf("Case #%d: %04d\n", index, c[n][m]);
  }
  return 0;
}
