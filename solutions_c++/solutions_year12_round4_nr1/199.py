#include <cassert>
#include <cstdio>
#include <cstring>

#include <algorithm>

int main() {
  using namespace std;
  int tn;
  assert(scanf("%d", &tn) == 1);
  for (int tt = 1; tt <= tn; tt++) {
    int n;
    assert(scanf("%d", &n) == 1);
    int d[n + 1], l[n + 1];
    for (int i = 0; i < n; i++)
      assert(scanf("%d%d", &d[i], &l[i]) == 2);
    assert(scanf("%d", &d[n]) == 1);
    l[n] = 0;
    int r[n + 1];
    memset(r, -1, sizeof(r[0]) * (n + 1));
    r[0] = d[0];
    for (int i = 0; i < n; i++) {
      // fprintf(stderr, "r[i=%d] = %d\n", i, r[i]);
      if (r[i] == -1)
        continue;
      for (int j = i + 1; j <= n; j++) {
        if (r[i] < d[j] - d[i])
          continue;
        r[j] = max(r[j], min(d[j] - d[i], l[j]));
      }
    }
    printf("Case #%d: %s\n", tt, r[n] == -1 ? "NO" : "YES");
  }
  return 0;
}

