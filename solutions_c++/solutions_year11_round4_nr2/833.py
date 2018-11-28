#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <cstring>
#include <cctype>
#include <climits>

using namespace std;
const int maxv = 987654321;
typedef long long ll;
char w[500][500];
int R, C, D;

bool check(int r, int c, int size) {
  
  ll x = 0, y = 0;

  for (int i = 0; i <  size; i++) {
    for (int j = 0; j < size; j++) {
      if ((i == 0 || i == size - 1) && (j == 0 || j == size - 1)) continue;
      if (j * 2 + 1 != size) {
	x += ((j * 2 + 1) - size) * (D + w[i + r][j + c]);
      }
      if (i * 2 + 1 != size) {
	y += ((i * 2 + 1) - size) * (D + w[i + r ][j + c]);
      }
    }
  }
  //printf("%d %d %lld %lld\n",r,c, x, y);
  return x == 0 && y == 0;
}

int main() {
  int ca;
  scanf(" %d", &ca);
  
  for (int ii = 0; ii < ca; ii++) {
    scanf(" %d%d%d", &R, &C, &D);

    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
	scanf(" %c", &w[i][j]);
	w[i][j] -= '0';
      }
    }
    
    int ans = -1;

    for (int i = min(R, C); i >= 3; i--) {
      for (int r = 0; r < R - i + 1; r++) {
	for (int c = 0; c < C - i + 1; c++) {
	  if (check(r, c, i)) {
	    ans = i;
	    goto end;
	  }
	}
      }
    }
  end:;
    printf("Case #%d: ", ii + 1);
    if (ans == -1) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ans);
    }
      
  }
}
