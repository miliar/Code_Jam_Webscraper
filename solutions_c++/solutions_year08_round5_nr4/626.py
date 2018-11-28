# include <cstdio>
# include <cstring>

int map[120][120], n, m, r;
int f[120][120];

int main( ){
  int tt, i;
  for (scanf("%d", &tt), i = 1; i <= tt; ++i) {
    printf("Case #%d: ", i);
    memset(map, 0, sizeof(map));
    scanf("%d%d", &n, &m);
    scanf("%d", &r);
    for (int i = 0; i < r; ++i) {
      int x, y;
      scanf("%d%d", &x, &y);
      map[x][y]++;
    }

    memset(f, 0, sizeof(f));
    f[1][1] = 1;
    if (map[1][1] > 0) f[1][1] = 0;

    for (int i = 1; i <= n; ++i)
      for (int j = 1; j <= m; ++j) if (map[i][j]==0) {
	int lx = i - 2, ly = j - 1;
	if (lx >= 0 && ly >= 0)
	  f[i][j] += f[lx][ly];
	lx = i - 1; ly = j - 2;
	if (lx >= 0 && ly >= 0)
	  f[i][j] += f[lx][ly];
	f[i][j] %= 10007;
      }

    printf("%d\n", f[n][m]);
  }
}
