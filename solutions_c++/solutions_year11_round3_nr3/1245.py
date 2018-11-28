#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <string>
#include <set>
#include <vector>

#define N 105

using namespace std;

namespace {

  int freq[N];
  int a, b, n;

  int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
  }

  bool find(int x) {
    for (int i = 0; i < n; ++i)
      if (freq[i] == x)
	return true;
    return false;
  }

  bool check(int x) {
    for (int i = 0; i < n; ++i) {
      if (freq[i] > x && freq[i] % x != 0)
	return false;
      if (freq[i] < x && x % freq[i] != 0)
	return false;
    }
    return true;
  }

  void solve(int test_case) {
    scanf("%d%d%d", &n, &a, &b);
    for (int i = 0; i < n; ++i)
      scanf("%d", &freq[i]);

    int g = freq[0];
    for (int i = 1; i < n; ++i) {
      g = gcd(g, freq[i]);
    }
    int ret = -1;
   
    for (int f = a; f <= b; ++f) {
      if (check(f)) {
	ret = f;
	break;
      }
    }

    if (ret == -1)
      printf("Case #%d: NO\n", test_case);
    else
      printf("Case #%d: %d\n", test_case, ret);
  }
}

int main() {
  int n_tc; scanf("%d", &n_tc);
  for (int i = 1; i <= n_tc; ++i)
    solve(i);
  return 0;
}
