#include <cstdio>
#include <cstdlib>
#include <string>

#define N 1001

using namespace std;

namespace {
  int c[N];
  int n;

  void input() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
      scanf("%d", &c[i]);
  }

}

namespace fast {
  int solve(int test_case) {
    int sum = 0;
    int xor_sum = 0;
    for (int i = 0; i < n; ++i) {
      sum += c[i];
      xor_sum ^= c[i];
    }
    if (xor_sum != 0)
      return -1;

    int least = 0x3f3f3f3f;
    for (int i = 0; i < n; ++i)
      if (c[i] < least)
	least = c[i];
    return sum - least;
  }
}

namespace bf {
  
  int xor_sum(int mask) {
    int ret = 0;
    for (int i = 0; i < n; ++i)
      if ((1 << i) & mask)
	ret ^= c[i];
    return ret;
  }

  int sum(int mask) {
    int ret = 0;
    for (int i = 0; i < n; ++i)
      if ((1 << i) & mask)
	ret += c[i];
    return ret;
  }

  int solve(int test_case) {
    int best = -1;
    const int all_ones = (1 << n) - 1;
    for (int mask = 1; mask < all_ones; ++mask) {
      if (xor_sum(mask) != xor_sum(mask ^ all_ones))
	continue;
      int bigger = std::max(sum(mask), sum(mask ^ all_ones));
      if (bigger > best)
	best = bigger;
    }
    return best;
  }
}

int main() {
  int n_tc;
  scanf("%d", &n_tc);
  for (int i = 1; i <= n_tc; ++i) {
    input();
    int sol = (n < 16 ? bf::solve(i) : fast::solve(i));
    if (sol < 0)
      printf("Case #%d: NO\n", i);
    else
      printf("Case #%d: %d\n", i, sol);
  }
  return 0;
}
