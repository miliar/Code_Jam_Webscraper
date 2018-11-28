#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int t=0; t<T; t++) {
    printf("Case #%d:\n", t+1);
    int R, C;
    scanf("%d %d\n", &R, &C);
    char B[R][C];
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        scanf("%c", &B[r][c]);
      }
      scanf("\n");
    }
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (B[r][c] == '.') { continue; }
        if (B[r][c] == '#') { 
          if (r >= R - 1 || c >= C-1) { goto impossible; }
          if (B[r + 1][c] != '#' ||
              B[r + 1][c + 1] != '#' ||
              B[r][c+1] != '#') { goto impossible; }
          B[r][c] = '/';
          B[r][c+1] = '\\';
          B[r+1][c] = '\\';
          B[r+1][c+1] = '/';
        }
      }
    }
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        printf("%c", B[r][c]);
      }
      printf("\n");
    }
    continue;
impossible:
    printf("Impossible\n");
  }
  return 0;
}
