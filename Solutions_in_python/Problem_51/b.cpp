#include <stdio.h>
int T, K, NW, NP, result;
int W[128][32], P[64][16], stk[64], len[128];

#define MOD 10009

void bkt(int lv, int k) {
  int i, j;
  if (lv == k) {
    int total[26] = {0};
    for (i = 0; i < 26; ++i) {
      for (total[i] = j = 0; j < lv; ++j)
        total[i] += W[stk[j]][i];
      total[i] %= MOD;
    }
    int r = 0;
    for (i = 0; i < NP; ++i) {
      int v = 1;
      for (j = 0; j < len[i]; ++j) {
        v = (v*total[P[i][j]]) % MOD;
      }
      r += v;
      r %= MOD;
    }
    result += r;
    result %= MOD;
    return;
  }
  for (i = 0; i < NW; ++i) {
    stk[lv] = i;
    bkt(lv+1, k);
  }
}

int main(void) {
  int t, i, j;

  scanf("%d", &T);
  for (t = 1; t <= T; ++t) {
    scanf("%d", &NW);
    for (i = 0; i < NW; ++i)
      for (j = 0; j < 26; ++j)
        scanf("%d", W[i]+j);
    scanf("%d", &NP);
    for (i = 0; i < NP; ++i) {
      scanf("%d", len+i);
        for (j = 0; j < len[i]; ++j)
          scanf("%d", P[i]+j);
    }
    scanf("%d", &K);

    printf("Case #%d:", t);
    for (i = 1; i <= K; ++i) {
      result = 0;
      bkt(0, i);
      printf(" %d", result);
    }
    printf("\n");
    fprintf(stderr, ">>> Gata %d\n", t);
  }
  return 0;
}
