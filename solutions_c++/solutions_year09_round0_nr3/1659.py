#include <stdio.h>
#include <string.h>


#define MAXN 1024

int N,T,M;
char str1[MAXN];
char str2[] = "welcome to code jam";

int dp[MAXN][MAXN];

int solve () {
    N = strlen(str1);
    M = strlen(str2);

    int ans = 0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            if (str1[i] == str2[j]) {
               if (j == 0) {
                  dp[i][j] = 1;
               } else {
                  for (int k=0; k<i; k++) {
                      if (str1[k] == str2[j-1]) {
                         dp[i][j] += dp[k][j-1];
                      }
                  }
               }
            }
        }
        ans = (ans + dp[i][M-1])%10000;
    }
    return ans;
}

int main () {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);


    scanf("%d\n",&T);
    for (int t=1; t<=T; t++) {
        memset(dp,0,sizeof(dp));
        gets(str1);
        printf("Case #%d: %04d\n",t,solve()%10000);
    }

    return 0;
}
