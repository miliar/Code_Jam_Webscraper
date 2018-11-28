#include <stdio.h>
#include <string.h>
#include <algorithm>

const int TOP = 1000000000;
const int MAXN = 10000;

int h[MAXN];
int next[MAXN];
int n;

bool check(int l, int r) {
  if (l == r - 1) {
    return next[l] == r;
  }
  if (next[l] < l || next[l + 1] < l + 1 || next[l + 1] > r) return false;
  bool result = true;
  for (int i = l + 1; i < next[l]; ++i) {
    if (next[i] > next[l]) return false;
  }
  if (next[l] == r) {
    result &= check(l + 1, next[l + 1]);
    if (next[l + 1] < r) result &= check(next[l + 1], r);
  } else {
    result &= check(l, next[l]);
    if (next[l] < r) result &= check(next[l], r);
  }
  return result;
}

std::pair<int, int> dfs(int l, int r, int x, int y, int top) {
  std::pair<int, int> p(x, y);
  if (next[l] == r) {
    if (h[r] == -1) {
      h[l] = h[r] = top;
    } else {
      h[l] = h[r] - ((long long) y * (r - l)) / x - 2;
    }
    p.first = r - l;
    p.second = h[r] - h[l];
  }
  if (l == r - 1) return p;
  std::pair<int, int> q(p);
  if (next[l] == r) {
    if (next[l + 1] < r) q = dfs(next[l + 1], r, q.first, q.second, top);
    q = dfs(l + 1, next[l + 1], q.first, q.second, top);
  } else {
    if (next[l] < r) q = dfs(next[l], r, q.first, q.second, top);
    q = dfs(l, next[l], q.first, q.second, top);
    p = q;
  }
  return p;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    scanf("%d", &n);
    for (int i = 0; i < n - 1; ++i) {
      scanf("%d", &next[i]);
      --next[i];
    }
    printf("Case #%d:", tt);
    if (!check(0, n - 1)) {
      puts(" Impossible");
      continue;
    }
    memset(h, -1, sizeof(h));
    dfs(0, n - 1, 1, 0, TOP);
    for (int i = 0; i < n; ++i) printf(" %d", h[i]);
    puts("");
  }
  return 0;
}
