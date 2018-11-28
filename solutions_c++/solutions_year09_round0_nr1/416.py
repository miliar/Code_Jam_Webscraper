#include <stdio.h>
#include <string.h>

char pal[5010][20];
char pode[20][256];
char buf[10000];
int main() {
  int L, D, N;
  scanf("%d %d %d", &L, &D, &N);
  for (int i = 0; i < D; i++)
    scanf(" %s", pal[i]);
  for (int _41 = 0; _41 < N; _41++) {
    memset(pode, 0, sizeof(pode));
    int t = 0;
    bool dentro = false;
    scanf(" %s", buf);
    int atu = 0;
    while (t < L) {
      if (buf[atu] == '(')
        dentro = true;
      else if (buf[atu] == ')') {
        dentro = false;
        t++;
      } else {
        pode[t][buf[atu]] = 1;
        if (!dentro)
          t++;
      }
      atu++;
    }
    int r = 0;
    for (int i = 0; i < D; i++) {
      int j;
      for (j = 0; j < L; j++)
        if (!pode[j][pal[i][j]])
          break;
      if (j == L)
        r++;
    }
    printf("Case #%d: %d\n", _41+1, r);
  }
  return 0;
}
