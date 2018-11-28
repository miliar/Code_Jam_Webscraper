#include <stdio.h>

int main() {
  int T, N;
  char b[41][41];
  int d[41];
  scanf("%d", &T);

  for (int cs=1; cs<=T; cs++) {
    scanf("%d", &N);

    for (int i=0; i<N; i++) {
      scanf("%s", b[i]);
      int j;
      for (j=N-1; j; j--)
        if (b[i][j] == '1') break;
      d[i] = j;
    }

    int k=0;
    for (int i=0; i<N; i++) {
      if (d[i] > i) {
        int j;
        for (j=i+1; j<N; j++) {
          if (d[j] <= i) break;
        }
        k += j-i;
        for (;j!=i;j--) {
          int tmp = d[j];
          d[j] = d[j-1];
          d[j-1] = tmp;
        }
      }
    }

    printf("Case #%d: %d\n", cs, k);
  }
  return 0;
}
