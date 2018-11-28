#include <math.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <complex>
#include <map>
#include <set>
#include <string>
#include <vector>

const int kMaxN = 1000;

int a[kMaxN], id[kMaxN];

inline bool cmp(int x, int y) {
  return a[x] < a[y];
}

int main() {
  int case_size, n;
  scanf("%d", &case_size);
  for (int T = 1; T <= case_size; ++T) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%d", a + i);
      id[i] = i;
    }
    std::sort(id, id + n, cmp);
    int ans = 0;
    for (int i = 0; i < n; ++i)
      if (id[i] != i) ++ans;
    printf("Case #%d: %d.000000\n", T, ans);
  }
  return 0;
}
