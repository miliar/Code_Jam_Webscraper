#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MAX = 100;

bool test(long long n, int pd, int pg) {
  if (pg == 100 && pd < 100) {
    return false;
  }
  
  if (pg == 0 && pd > 0) {
    return false;
  }

  bool validpd = false;
  for (int d = 1; !validpd && d <= n && d <= MAX; d++) {
    if ((d * pd) % MAX == 0) {
      validpd = true;
    }
  }

  return validpd;
}

int main() {
  int tt;
  scanf("%d", &tt);
  for (int t = 1; t <= tt; ++t) {
    long long n;
    int pd, pg;
    scanf("%lld %d %d\n", &n, &pd, &pg);
    if (test(n, pd, pg)) {
      printf("Case #%d: Possible\n", t);
    } else {
      printf("Case #%d: Broken\n", t);
    }
  }

  return 0;
}
