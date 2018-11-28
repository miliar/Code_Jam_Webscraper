#include <stdio.h>
#include <algorithm>

using namespace std;

#define NMAX 35
#define INF 0x3f3f3f3f

int A[NMAX];
int din[NMAX];

int main() {
  freopen("load.in", "r", stdin);
  freopen("load.out", "w", stdout);

  int T;
  scanf("%d ", &T);

  for (int t = 1; t <= T; t++) {
    int L, P, C;
    scanf("%d %d %d", &L, &P, &C);

    if (L > P / C) {
      printf("Case #%d: 0\n", t);
      continue;
    }

    int cnt = 1;
    for (long long i = L * C; P > i; i = i * C, cnt++) {
      A[cnt] = i;
    }
    cnt--;

    din[0] = 0;
    din[1] = 1;
    for (int i = 2; i <= cnt; i++) {
      din[i] = INF;
      for (int j = 1; j <= i; j++) {
        din[i] = min(din[i], max(din[j - 1], din[i - j]) + 1);
      }
    }

    printf("Case #%d: %d\n", t, din[cnt]);
  }
}
