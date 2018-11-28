#include <stdio.h>

int main() {
  int C;
  scanf("%d", &C);

  for (int cs=1; cs<=C; cs++) {
    int N;
    int t[3];
    scanf("%d", &N);

    for (int i=0; i<N; i++)
      scanf("%d", t+i);

    int m = t[0];
    for (int i=1; i<N; i++)
      m = m > t[i] ? m : t[i];

    for (; m; m--) {
      int i, k = t[0]%m;
      for (i=1; i<N; i++)
        if (t[i]%m != k) break;

      if (i == N) break;
    }

    int tm = t[0] % m;
    printf("Case #%d: %d\n", cs, tm == 0 ? 0 : (m - tm));
  }

  return 0;
}
