#include <stdio.h>
#include <string.h>

int R, K, N, G[1111];
long long sexy[1111];
int next[1111];
int IN[1111];
long long S[1111];

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d%d%d", &R, &K, &N);
    for (int i = 0; i < N; i++) scanf("%d", &G[i]);

    for (int i = 0; i < N; i++) {
      long long s = 0;
      bool flag = false;
      for (int j = 0; j < N; j++) {
        int k = (i+j) % N;
        if (s + G[k] <= K) s += G[k];
        else {
          next[i] = (i+j) % N;
          sexy[i] = s;
          flag = true;
          break;
        }
      }
      if (!flag) { next[i] = i; sexy[i] = s; }
    }
  
    memset(IN, -1, sizeof(IN));

    int g = 0, z;
    long long psum = 0;
    for (z = 0; IN[g] == -1 && z < R; g = next[g], z++) {
      IN[g] = z;
      S[g] = psum;
      psum += sexy[g];
    }
    if (z == R) {
      printf("Case #%d: %lld\n", t, psum);
    } else {
      int len = z - IN[g];
      long long m = psum - S[g];
      long long ss = S[g];
      R = R - IN[g];
      ss += m * (R / len);
      R -= (R/len)*len;
      for (int i = 0; i < R; i++) {
        ss += sexy[g];
        g = next[g];
      }

      printf("Case #%d: %lld\n", t, ss);
    }
  }
  return 0;
}
