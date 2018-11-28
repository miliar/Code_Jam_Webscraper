#include <math.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <complex>
#include <map>
#include <set>
#include <string>
#include <vector>

int gcd(int a, int b) {
  if (b == 0) return a;
  else return gcd(b, a % b);
}

int Sign(double x) {
  if (fabs(x) < 1e-9) return 0;
  return x < 0 ? - 1 : 1;
}

int main() {
  int T, a, b;
  long long N;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%lld%d%d", &N, &a, &b);
    printf("Case #%d: ", t);
    if (b == 0) {
      if (a == 0) puts("Possible");
      else puts("Broken");
      continue;
    }
    if (b == 100) {
      if (a == 100) puts("Possible");
      else puts("Broken");
      continue;
    }
    int ga = gcd(a, 100);
    if (N >= 100 / ga) puts("Possible");
    else puts("Broken");
  }
  return 0;
}
