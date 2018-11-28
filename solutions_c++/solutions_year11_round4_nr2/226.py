#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int mp[16][16];

void next(int & i) {
  do {
    i = getchar();
  } while (i < '0' || i > '9');
  i -= '0';
}

int R, C, D;

bool check(int x, int y, int k) {
  double s1 = 0;
  double s2 = 0;
  double mx = (k - 1) / 2.0;
  double my = (k - 1) / 2.0;
  for (int i = 0; i < k; ++i)
    for (int j = 0; j < k; ++j) {
      if ((i == 0 || i == k - 1) &&
	  (j == 0 || j == k - 1)) continue;
      s1 += (i - mx) * mp[i+x][j+y]; 
      s2 += (j - my) * mp[i+x][j+y];
    }
  return s1 == 0 && s2 == 0;
} 

void solve() {
  scanf("%d%d%d", &R, &C, &D);
  for (int i = 0; i < R; ++i)
    for (int j = 0; j < C; ++j)
      next(mp[i][j]);
  int ans = -1;
  int mk = min(R, C);
  for (int k = 3; k <= mk; ++k) {
    bool ok = false;
    for (int i = 0; !ok && i + k <= R; ++i)
      for (int j = 0; j + k <= C; ++j) {
	if (check(i, j, k)) {
	  ok = true;
	  break;
	}
      }
    if (ok) ans = k;
  }
  if (ans == -1) printf("IMPOSSIBLE\n");
  else printf("%d\n", ans);
}

int main() {
  freopen("input.txt", "r", stdin);
  int T, tc = 0;
  scanf("%d", &T);
  while (T --) {
    printf("Case #%d: ", ++tc);
    solve();
  }
}
