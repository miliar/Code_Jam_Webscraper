#include <cassert>
#include <cstdio>

const int maxn = 1000;

int a[maxn], next[maxn], bonus[maxn];

int main() {
  int t, r, k, n;
  assert(scanf("%d", &t) == 1);
  for (int test = 1; test <= t; test++) {
    assert(scanf("%d%d%d", &r, &k, &n) == 3);
    for (int i = 0; i < n; i++)
      assert(scanf("%d", &a[i]) == 1);
    for (int i = 0; i < n; i++) {
      int sum = 0, target = i;
      while (sum + a[target] <= k) {
        sum += a[target], target = (target + 1) % n;
        if (target == i)
          break;
      }
      next[i] = target;
      bonus[i] = sum;
    }
    long long ans = 0;
    for (int i = 0, j = 0; i < r; i++)
      ans += bonus[j], j = next[j];
    printf("Case #%d: %lld\n", test, ans);
  }
  return 0;
}

