#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <list>

#define FOR(i, m, n) for (int i=m; i<n; i++)

using namespace std;

int R, C;
char mat[60][60];

void solve() {
  scanf("%d%d", &R, &C);
  FOR (r, 0, R) FOR (c, 0, C)
    scanf(" %c", &mat[r][c]);
  FOR (i, 0, C+1)
    mat[R][i] = '.';
  FOR (i, 0, R+1)
    mat[i][C+1] = '.';
  bool b = true;
  FOR (i, 0, R) FOR (j, 0, C)
    if (mat[i][j]=='#' && mat[i+1][j]=='#' && mat[i][j+1]=='#' && mat[i+1][j+1]=='#') {
      mat[i][j] = '/'; mat[i+1][j+1] = '/'; mat[i+1][j] = '\\'; mat[i][j+1] = '\\';
    }
    else if (mat[i][j]=='#') {
      b = false;
      goto ven;
    }
ven:
  if (!b)
    printf("Impossible\n");
  else {
    FOR (i, 0, R) {
      FOR (j, 0, C)
        printf("%c", mat[i][j]);
      printf("\n");
    }
  }
}

int main() {
  int T; scanf("%d", &T);
  FOR (qq, 0, T) {
    printf("Case #%d:\n", qq+1);
    solve();
  }
  return 0;
}
