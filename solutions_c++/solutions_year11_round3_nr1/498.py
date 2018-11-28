#include <cstdio>
#include <climits>
#include <cstring>
#include <cctype>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>

using namespace std;
typedef long long ll;
char tile[60][60];
int R, C;

bool conv(int r, int c) {
  if (r + 1 < R && c + 1 < C &&
      tile[r + 1][c] == '#' &&
      tile[r][c + 1] == '#' &&
      tile[r + 1][c + 1] == '#') {
    tile[r][c] = tile[r+1][c+1] = '/';
    tile[r+1][c] = tile[r][c+1] = '\\';
    return true;
  }
  return false;
}

int main() {
  int ca;
  scanf(" %d", &ca);

  for (int ii = 0; ii < ca; ii++) {
    scanf(" %d%d", &R, &C);

    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
	scanf(" %c", &tile[i][j]);
      }
    }
    
    bool suc = true;

    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
	if (tile[i][j] == '#') {
	  if (!conv(i, j)) {
	    suc = false;
	  }
	}
      }
    }
    
    printf("Case #%d:\n", ii+1);
    if (suc) {
      for (int i = 0; i < R; i++) {
	for (int j = 0;j < C; j++) {
	  printf("%c", tile[i][j]);
	}
	printf("\n");
      }
    } else printf("Impossible\n");

  }
}
