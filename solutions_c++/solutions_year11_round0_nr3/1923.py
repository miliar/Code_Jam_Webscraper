#include <stdio.h>
#include <algorithm>
#define FOR(q,n) for(int q=0; q<n; q++)

void solve() {
  int n;
  scanf("%d", &n);
  int data[1000];
  FOR(q,n) scanf("%d", &data[q]);
  int x = 0;
  FOR(q,n) x ^= data[q];
  if (x != 0) {
    printf("NO\n");
    return;
  }
  std::sort(data, data+n);
  int s = 0;
  FOR(q, n) if(q) s += data[q];
  printf("%d\n", s);

}

int main() {
  int t;
  scanf("%d", &t);
  FOR(q, t) {
    printf("Case #%d: ", q+1);
    solve();
  }

}
