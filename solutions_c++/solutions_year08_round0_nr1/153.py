#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>

const int S = 110;
const int LEN = 110;
const int Q = 1010;
const int INF = 1000000000;

char names[S][LEN];
int dp[Q][S];
char tmp[LEN];

int main(){
  freopen("a.in2", "r", stdin);
  freopen("a.out2", "w", stdout);
  int tn, t;
  scanf("%d\n", &tn);
  for (t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    int s, q;
    scanf("%d", &s);
    gets(tmp);
    int i, j, h;
    for (i=1; i<=s; i++){
      gets(names[i]);
    }
    scanf("%d", &q);
    gets(tmp);
    if (q == 0){
      printf("0\n");
      continue;
    }
    for (i=1; i<=q; i++){
      gets(tmp);
      if (i == 1){
        for (j=1; j<=s; j++){
          if (!strcmp(names[j], tmp)) dp[1][j] = -1;
          else dp[1][j] = 0;
        }
        continue;
      }
      for (j=1; j<=s; j++){
        if (!strcmp(names[j], tmp)) dp[i][j] = -1;
        else{
          dp[i][j] = INF;
          for (h=1; h<=s; h++){
            if ((dp[i-1][h] >= 0) && (dp[i-1][h] + (h!=j) < dp[i][j])){
              dp[i][j] = dp[i-1][h] + (h!=j);
            }
          }
        }
      }
    }
    /*for (i=1; i<=q; i++){
      for (j=1; j<=s; j++) printf("%d ", dp[i][j]);
      printf("\n");
    }*/
    int ans = INF;
    for (j=1; j<=s; j++){
      if ((dp[q][j] >= 0) && (dp[q][j] < ans)) ans = dp[q][j];
    }
    printf("%d\n", ans);
  }
  return 0;
}