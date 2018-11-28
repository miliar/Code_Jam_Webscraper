#include <stdio.h>
#include <string.h>

int pai[100*100+10];
int rank[100*100+10];

void inic() {
  for (int i = 0; i < 100*100+10; i++) {
    pai[i] = i;
    rank[i] = 0;
  }
}

int rep(int a) {
  if (pai[a] != a)
    pai[a] = rep(pai[a]);
  return pai[a];
}

bool unio(int a, int b) {
  a = rep(a);
  b = rep(b);
  if (a == b)
    return false;
  if (rank[a] < rank[b])
    pai[a] = b;
  else
    pai[b] = a;
  if (rank[a] == rank[b])
    rank[a]++;
  return true;
}

int mapa[110][110];
char base[110][110];
int dir[][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; t++) {
    inic();
    int H, W;
    scanf("%d %d", &H, &W);
    for (int i = 0; i < H; i++)
      for (int j = 0; j < W; j++)
        scanf("%d", &mapa[i][j]);
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        int mais = mapa[i][j];
        int dd = -1;
        for (int d = 0; d < 4; d++) {
          int ii = i + dir[d][0];
          int jj = j + dir[d][1];
          if (ii < 0 || ii >= H || jj < 0 || jj >= W)
            continue;
          if (mapa[ii][jj] < mais) {
            mais = mapa[ii][jj];
            dd = d;
          }
        }
        if (dd == -1)
          continue;
        int ii = i + dir[dd][0];
        int jj = j + dir[dd][1];
        unio(100*ii+jj, 100*i+j);
      }
    }
    memset(base, 0, sizeof(base));
    char atu = 'a';
    for (int i = 0; i < H; i++)
      for (int j = 0; j < W; j++) {
        if (base[i][j] != 0)
          continue;
        base[i][j] = atu;
        for (int k = 0; k < H; k++)
          for (int l = 0; l < W; l++)
            if (rep(100*i+j) == rep(100*k+l))
              base[k][l] = atu;
        atu++;
      }
    printf("Case #%d:\n", t+1);
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        if (j)
          printf(" ");
        printf("%c", base[i][j]);
      }
      printf("\n");
    }
  }
  return 0;
}
