#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;

int M[111][111];
int R, C;
bool B[111][111];
char D[111][111];
char ass;

// North, West, East, South
int dir[][2] = {{-1,0},{0,-1},{0,1},{1,0}};

#define RANGE(a, b, c) ((a) <= (b) && (b) <= (c))

char dfs(int r, int c) {
  if (B[r][c]) return D[r][c];
  B[r][c] = true;
  int min_level = 12341234;
  for (int i = 0; i < 4; i++) {
    int nr = r + dir[i][0];
    int nc = c + dir[i][1];
    if (RANGE(0, nr, R-1) && RANGE(0,nc,C-1)) {
      min_level = min(min_level, M[nr][nc]);
    }
  }

  if (min_level >= M[r][c]) {
    D[r][c] = ass++;
    return D[r][c];
  }

  for (int i = 0; i < 4; i++) {
    int nr = r + dir[i][0];
    int nc = c + dir[i][1];
    if (RANGE(0, nr, R-1) && RANGE(0,nc,C-1) && M[nr][nc]==min_level) {
      D[r][c] = dfs(nr, nc);
      return D[r][c];
    }
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    scanf("%d%d", &R, &C);
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) scanf("%d", &M[i][j]);
    }
    memset(B, 0, sizeof(B));
    ass = 'a';
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        if (!B[i][j]) dfs(i, j);
      }
    }

    printf("Case #%d:\n", tc);
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        printf("%c ", D[i][j]);
      }
      printf("\n");
    }
  }
  return 0;
}
