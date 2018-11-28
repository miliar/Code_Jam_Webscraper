#include <stdio.h>
#include <string.h>
char g[55][55];
int n, m;
bool put(int x, int y) {
  if(x+1 >= n || y+1 >= m) return false;
  if(g[x][y]=='#' && g[x+1][y]=='#' && g[x][y+1]=='#' && g[x+1][y+1]=='#') {
    g[x][y]='/'; g[x][y+1]='\\';
    g[x+1][y]='\\'; g[x+1][y+1]='/';
    return true;
  }
  return false;
}
int main() {
  int casn;
  scanf("%d", &casn);
  for(int cas=1; cas<=casn; ++cas) {
    printf("Case #%d:\n", cas);
    memset(g, 0, sizeof g);
    scanf("%d%d", &n, &m);
    for(int i=0; i<n; ++i) scanf("%s", g[i]);
    for(int i=0; i<n; ++i) {
      for(int j=0; j<m; ++j)
        if(g[i][j] == '#')
          if(!put(i, j)) goto fail;
    }

    for(int i=0; i<n; ++i) {
      for(int j=0; j<m; ++j) {
        putchar(g[i][j]);
      }
      printf("\n");
    }
    continue;
    fail: puts("Impossible");
  }
  return 0;
}
