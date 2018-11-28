#include <cstdio>
#include <memory.h>

#define maxn 1010

int T;
int n;
int per[maxn];
int was[maxn];

long double ch[maxn];
long double rfact[maxn];
long double p[maxn];
long double d[maxn];


int main() {
  rfact[0] = 1;
  for (int i = 1; i <= 1000; i++) {
    rfact[i] = rfact[i - 1] / i;
  }

  ch[0] = 1;
  int sgn = 1;
  for (int i = 1; i <= 1000; i++) {
    sgn *= -1;
    ch[i] = ch[i - 1] + sgn * rfact[i];
  }

  d[0] = 0;
  d[1] = 0;
  for (int i = 2; i <= 1000; i++) {
    for (int j = 0; j <= i; j++) {
      p[i - j] = ch[j] * rfact[i - j];
    }

    long double cur = 1;
    for (int j = 1; j <= i; j++) {
      cur += p[j] * d[i - j];
    }

    d[i] = cur / (1 - p[0]);
  }


  scanf("%d", &T);  
  for (int q = 1; q <= T; q++) {
    scanf("%d", &n);
    int m = 0;
    for (int i = 0; i < n; i++) {
      scanf("%d", &per[i]), per[i]--;
      if (per[i] != i) m++;
    }

    printf("Case #%d: %.6lf\n", q, (double)d[m]);
  }
  return 0;
}
