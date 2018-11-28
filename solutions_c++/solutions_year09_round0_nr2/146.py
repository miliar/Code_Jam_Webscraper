#include "cstdio"
#include "memory"
using namespace std;
typedef long long i64;

const int di[] = {-1, 0, 0, +1};
const int dj[] = {0, -1, +1, 0};
int grid[200][200], m, n;
int basin[200][200], next = 0;

int GetBasin(int i, int j) {
  int lowest = -1, lheight = grid[i][j];
  for (int k = 0; k < 4 && basin[i][j] == -1; ++k) {
    const int ni = i + di[k], nj = j + dj[k];
    if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] < lheight)
      lowest = k, lheight = grid[ni][nj];
  }
  if (lowest != -1) basin[i][j] = GetBasin(i + di[lowest], j + dj[lowest]);
  if (basin[i][j] == -1) basin[i][j] = next++;
  return basin[i][j];
}
int main() {
  int T; scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    scanf("%d %d", &m, &n);
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        scanf("%d", &grid[i][j]);
    memset(basin, -1, sizeof(basin)), next = 0;
    printf("Case #%d:\n", Ti);
    for (int i = 0; i < m; ++i) {
      printf("%c", GetBasin(i, 0) + 'a');
      for (int j = 1; j < n; ++j)
        printf(" %c", GetBasin(i, j) + 'a');
      printf("\n");
    }
  }
  return 0;
}
