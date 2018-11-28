#include <cassert>
#include <cstdio>

bool f;
void build( int n, int *next, int *h, int st, int fi, int hh, int kk ) {
  // fprintf(stderr, "%*sbuild(%d,%d)\n", kk, "", st, fi);
  // if (kk >= 2)
  //   return;
  if (st >= fi)
    return;
  h[st] = hh - (fi - st) * kk;
  for (int i = st, j; i != fi && !f; i = j) {
    j = next[i];
    if (j > fi) {
      f = true;
      return;
    }
    h[j] = hh - (fi - j) * kk;
    // fprintf(stderr, "%*s--(%d,%d) -> (%d,%d)\n", kk, "", st, fi, i + 1, j);
    build(n, next, h, i + 1, j, h[j], kk + 1);
  }
}

int main() {
  int tn;
  assert(scanf("%d", &tn) == 1);
  for (int tt = 1; tt <= tn; tt++) {
    int n;
    assert(scanf("%d", &n) == 1);
    int next[n];
    for (int i = 0; i < n - 1; i++)
      assert(scanf("%d", &next[i]) == 1), next[i]--;
    next[n - 1] = n;
    int h[n];
    f = false;
    build(n, next, h, 0, n, (int)1e9, 0);
    printf("Case #%d:", tt);
    if (f) {
      printf(" Impossible\n");
    } else {
      for (int i = 0; i < n; i++)
        printf(" %d", h[i]);
      printf("\n");
    }
  }
  return 0;
}

