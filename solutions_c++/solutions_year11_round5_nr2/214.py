#include <iostream>
#include <cstdio>
#include <sstream>
#include <cstring>
using namespace std;

int a[10020];
char buf[200000];
void solve() {
  int n = 0, m = 0, t;
  memset(a, 0, sizeof(a));
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", &t);
    m = max(m, t);
    ++a[t];
  }
  
  int ans = n;
  for (int i = 0; i <= m; ++i)
    while (a[i]) {
      int now = a[i];
      int cnt = 0;
      int j = i;
      while (a[j] >= now) {
	now = a[j];
	++cnt;
	--a[j];
	++j;
      }
      ans = min(ans, cnt);
    }
  printf("%d\n", ans);
}

int main() {
  freopen("input.txt", "r", stdin);
  int T, tc = 0;
  scanf("%d\n", &T);
  while (T--) {
    printf("Case #%d: ", ++tc);
    solve();
  }
  return 0;
}
