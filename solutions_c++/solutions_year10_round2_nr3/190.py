#include <iostream>

using namespace std;

#define MAXN 500
#define MOD 100003

int nTests, test;
int i, j, k;
int n;
int T[MAXN + 1][MAXN + 1][MAXN + 1];
int ans[MAXN+1];

int main() {
  for (k = 0; k <= MAXN; ++k) {
    for (i = 0; i <= MAXN; ++i) {
      for (j = 0; j <= MAXN; ++j) {
        if (k == 0) {
          if (i == 1 && j == 0) {
            T[i][j][k] = 1;
          } else {
            T[i][j][k] = 0;
          }
        } else {
          if (i == k) {
            if (j > 0) {
              T[i][j][k] = T[j][j - 1][k - 1];
            } else {
              if (i == 1) {
                T[i][j][k] = 1;
              } else {
                T[i][j][k] = 0;
              }
            }
          } else {
            if (j > 0) {
              T[i][j][k] = (T[i][j][k - 1] + T[i][j - 1][k - 1]) % MOD;
            } else {
              T[i][j][k] = T[i][j][k - 1];
            }
          }
        }
      }
    }
  }
  for (n = 2; n <= MAXN; ++n) {
    ans[n] = 0;
    for (j = 0; j <= MAXN; ++j) {
      ans[n] = (ans[n] + T[n][j][n]) % MOD;
    }
  }
  scanf("%d", &nTests);
  for (test = 1; test <= nTests; ++test) {
    scanf("%d", &n);
    printf("Case #%d: %d\n",test,ans[n]);
  }
  return 0;
}
