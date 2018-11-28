#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int gcd(int a, int b) {
  int g = 1;
  for (int i = max(a, b); i >= 1; --i) {
    if (a%i == 0 && b%i == 0) {
      a/=i;
      b/=i;
      g *=i;
    }
  }

  return g;
}

int main(void) {
  int nc;

  long long pd, pg, n;

  freopen("A-large.in", "r", stdin);
  freopen("A.large.out", "w", stdout);

  scanf("%d", &nc);

  for (int c = 1; c <= nc; c++) {
    scanf("%lld %lld %lld", &n, &pd, &pg);

    bool poss = false;
    if (pg == 0) {
      if (pd == 0) {
        poss = true;
      } else {
        poss = false;
      }
    } else if (pg == 100) {
      if (pd == 100) {
        poss = true;
      } else {
        poss = false;
      }
    } else {
      int g = gcd(pd, 100);

      g = 100 / g;

      if (g <= n) poss = true;
      else poss = false;
    }





    if (poss) {
      printf("Case #%d: Possible\n", c);
    } else {
      printf("Case #%d: Broken\n", c);
    }
  }

  return 0;
}