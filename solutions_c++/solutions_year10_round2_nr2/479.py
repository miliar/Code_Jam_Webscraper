#include <cstdio>
#include <algorithm>

using namespace std;

struct ch {
  int x, v;
  bool operator < ( ch b ) const {
    return x < b.x;
  }
};

const int maxN = 55;

ch c[maxN];
int n, k, b, t;

int main() {
  int nt;
  scanf("%d", &nt);
  for (int tt = 1; tt <= nt; tt++) {
    scanf("%d%d%d%d", &n, &k, &b, &t);
    for (int i = 0; i < n; i++) {
      scanf("%d", &c[i].x);
    }
    for (int i = 0; i < n; i++) {
      scanf("%d", &c[i].v);
    }
    sort(c, c + n);
    int ans = 0, cur = 0;
    for (int i = n - 1; i >= 0 && k > 0; i--) {
      if (b - c[i].x > t * c[i].v) {
        cur++;
      } else {
        ans += cur;
        k--;
      }
    }
    printf("Case #%d: ", tt);
    if (k > 0) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ans);
    }
  }
  return 0;
}
