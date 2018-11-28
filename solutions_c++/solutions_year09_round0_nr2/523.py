#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
#define debug(x) cerr << __LINE__ << ": " << #x << " = " << (x) << "\n"
#define debugf(x...) fprintf(stderr, x)

const int MAXN = 105;

int a[MAXN][MAXN], h, w, b[MAXN][MAXN], map[26], m;

const int dc[] = {0, -1, 1, 0}, dr[] = {-1, 0, 0, 1};

int find(int r, int c) {
  int &ans = b[r][c];
  if (ans != -1) return ans;
  int mi = a[r][c] - 1;
  for (int i = 0; i < 4; ++i) {
    int nr = r + dr[i], nc = c + dc[i];
    if (nr >= 0 && nr < h && nc >= 0 && nc < w && a[nr][nc] < mi) mi = a[nr][nc];
  }
  for (int i = 0; i < 4; ++i) {
    int nr = r + dr[i], nc = c + dc[i];
    if (nr >= 0 && nr < h && nc >= 0 && nc < w && a[nr][nc] == mi) return ans = find(nr, nc);
  }
  return ans = m++;
}

void solve() {
  scanf("%d%d", &h, &w);
  for (int r = 0; r < h; ++r) for (int c = 0; c < w; ++c) scanf("%d", &a[r][c]);

  memset(b, 255, sizeof(b));

  m = 0;
  for (int r = 0; r < h; ++r) for (int c = 0; c < w; ++c) find(r, c);

  memset(map, 255, sizeof(map));
  m = 0;
  for (int r = 0; r < h; ++r) {
    for (int c = 0; c < w; ++c) {
      if (map[b[r][c]] == -1) map[b[r][c]] = m++;
      printf("%c ", map[b[r][c]] + 'a');
    }
    printf("\n");
  }
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i) printf("Case #%d:\n", i), solve();
  return 0;
}
