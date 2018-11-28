#include <stdio.h>
#include <string.h>

#define NMAX 10000

long long N, K, T, R;
long long V[NMAX];
long long viz[NMAX];
long long euro[NMAX], cnt[NMAX];

int main() {
  freopen("roller.in", "r", stdin);
  freopen("roller.out", "w", stdout);

  long long i, e, c;
  scanf("%lld ", &T);
  for (int x = 1; x <= T; x++) {
    scanf("%lld %lld %lld ", &R, &K, &N);
    for (i = 1; i <= N; i++) {
      scanf("%lld ", &V[i]);
    }
    memset(viz, 0, sizeof(viz));

    for (i = 1, e = 0, c = 0; viz[i] == 0 && c < R;) {
      viz[i] = 1;
      euro[i] = e;
      cnt[i] = c;

      long long sum = V[i], crt = i + 1;
      if (crt > N) {
        crt = 0;
      }
      while (crt != i) {
        if (sum + V[crt] > K) {
          break;
        }

        sum += V[crt];
        crt++;
        if (crt > N) {
          crt = 1;
        }
      }

      //printf("e = %d s = %d\n", e, sum);

      i = crt;
      e = e + sum;
      c = c + 1;
    }

//    printf("e = %d\n", e);
    if (viz[i] == 1) {
        long long offset_c = c - cnt[i];
        long long offset_e = e - euro[i];
        long long nrc = (R - c) / offset_c;
        e = e + nrc * offset_e;
        c = c + nrc * offset_c;
//        printf("offset_c = %d offset_e = %d nrc = %d\n", offset_c, offset_e, nrc);
//        printf("e = %d c = %d\n", e, c);
    }
    for (c++; c <= R; c++) {
      long long sum = V[i];
      long long crt = i + 1;
      if (crt > N) {
        crt = 1;
      }
      while (crt != i) {
        if (sum + V[crt] > K) {
          break;
        }

        sum = sum + V[crt];
        crt = crt + 1;
        if (crt > N) {
          crt = 1;
        }
      }

      i = crt;
      e += sum;
//      printf("e = %d sum = %d\n", e, sum);
    }

    printf("Case #%d: %lld\n", x, e);
  }

  return 0;
}
