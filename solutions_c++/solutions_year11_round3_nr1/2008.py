#include <cstdio>
#include <cstring>
#define MAX 50

#define D 1

bool makesquares(char matrix[MAX][MAX+1], int r, int c) {
  for (int i = 0; i < r-1; i++) {
    for (int j = 0; j < c-1; j++) {
      if (matrix[i][j] == '#') {
        if (matrix[i][j+1] == '#' && matrix[i+1][j] == '#' && matrix[i+1][j+1] == '#') {
          matrix[i][j] = '/'; matrix[i][j+1] = '\\';
          matrix[i+1][j] = '\\'; matrix[i+1][j+1] = '/';
        }
      }
    }
  }
  for (int i = 0; i < r; i++)
    for (int j = 0; j < c; j++)
      if (matrix[i][j] == '#') return false;
  return true;
}

int main() {
  int kases;
  scanf("%d", &kases);
  for (int m = 1; m <= kases; m++) {
    int R, C;
    scanf("%d %d", &R, &C);
    char matrix[MAX][MAX+1] = {};
    for (int i = 0; i < R; i++)
      scanf("%s", matrix[i]);
    bool possible = makesquares(matrix, R, C);
    printf("Case #%d:\n", m);
    if (!possible) 
      printf("Impossible\n");
    else
      for (int i = 0; i < R; i++)
        printf("%s\n", matrix[i]);
  }
}
