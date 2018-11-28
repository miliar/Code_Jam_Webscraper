#include <stdio.h>
#include <string.h>

int N, n;
char s[1000];
int cnt;
char y[20] = "welcome to code jam";
int dp[19][500];
int i, j, len;

int main() {

  gets(s);
  sscanf(s, "%d", &N);

  for (n = 1; n <= N; n++) {
    gets(s);

    len = strlen(s);

    for (j = 0; j < len; j++) {
      for (i = 0; i < 19; i++) {
        dp[i][j] = 0;
      }
    }   
       
    if (y[0] == s[0])
        dp[0][0] = 1;
    else
        dp[0][0] = 0;  
    

    for (j = 1; j < len; j++) {
      if (y[0] == s[j])
        dp[0][j] = dp[0][j-1]+1;
      else
        dp[0][j] = dp[0][j-1];  
    }

    for (j = 1; j < len; j++) {
      for (i = 1; i < 19; i++) {
        if (y[i] == s[j]) {
          dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 10000;
        } else {
          dp[i][j] = dp[i][j-1];
        } 
      }
    }
/*
    for (i = 0; i < 19; i++) {
      for (j = 0; j < len; j++) {
        printf("%d ", dp[i][j]);
      }
      printf("\n"); 
    }   
*/

    printf("Case #%d: %04d\n", n, dp[18][len-1]);
  }

  return 0;
}