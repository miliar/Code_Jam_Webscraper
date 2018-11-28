#include <math.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <complex>
#include <map>
#include <set>
#include <string>
#include <vector>

int main() {
  int case_size, n;
  scanf("%d", &case_size);
  for (int T = 1; T <= case_size; ++T) {
    scanf("%d", &n);
    int x = 0, y = 0, sum = 0, min = 10000000;
    for (int i = 0; i < n; ++i) {
      scanf("%d", &x);
      y ^= x;
      sum += x;
      min = std::min(min, x);
    }
    if (y == 0) printf("Case #%d: %d\n", T, sum - min);
    else printf("Case #%d: NO\n", T);
  }
  return 0;
}
