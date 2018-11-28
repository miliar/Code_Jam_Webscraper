#include <cstdio>
#include <cstring>

const int LEN = 512;
const int MOD = 10000;

char welc[] = "welcome to code jam";
int wlen = 19;
char str[LEN];

int dp[LEN][20];

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  gets(str);
  for (t=1; t<=tn; t++){
    gets(str);
    int slen = strlen(str);
    int i, j;
    int res = 0;
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (i=1; i<=slen; i++){
      dp[i][0] = 1; 
      for (j=1; j<=wlen; j++){
        dp[i][j] = dp[i-1][j];
        if (str[i-1] == welc[j-1]){
          dp[i][j] += dp[i-1][j-1];
        }
        dp[i][j] %= MOD;
      }
      //res += dp[i][wlen];
      //res %= MOD;
    }
    res = dp[slen][wlen];
    printf("Case #%d: %04d\n", t, res);
  }
  return 0;
}
