#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;

const int maxn = 512;
typedef long long ll;
ll mass[maxn][maxn], sumx[maxn][maxn], sumy[maxn][maxn], summ[maxn][maxn];

ll val(ll a[][maxn], int y, int x) {
  if (y < 0 || x < 0) return 0;
  else return a[y][x];
}

ll calc(ll a[][maxn], int y, int x, int l) {
  ll ret = val(a, y + l - 1, x + l - 1) + val(a, y - 1, x - 1) - 
           val(a, y + l - 1, x - 1) - val(a, y - 1, x + l - 1);
  return ret;
}

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    printf("Case #%i: ", numcase);
    int ly, lx, d;
    scanf("%i%i%i", &ly, &lx, &d);
    for (int i = 0; i < ly; ++i) 
      for (int j = 0; j < lx; ++j) {
        char c;
        scanf(" %c", &c);
        mass[i][j] = (c - '0') + d;
      }

    for (int y = 0; y < ly; ++y) {
      for (int x = 0; x < lx; ++x) {
        sumy[y][x] = mass[y][x] * (2 * y + 1);
        if (x > 0) sumy[y][x] += sumy[y][x - 1];

        sumx[y][x] = mass[y][x] * (2 * x + 1);
        if (x > 0) sumx[y][x] += sumx[y][x - 1];

        summ[y][x] = mass[y][x];
        if (x > 0) summ[y][x] += summ[y][x - 1];
      }
      if (y > 0)
        for (int x = 0; x < lx; ++x) {
          sumx[y][x] += sumx[y - 1][x];
          sumy[y][x] += sumy[y - 1][x];
          summ[y][x] += summ[y - 1][x];
        }
    }

    bool possible = false;
    for (int l = max(ly, lx); l >= 3; --l) {
      for (int y = 0; y + l <= ly; ++y)
        for (int x = 0; x + l <= lx; ++x) {
 //         if (l == 5 && y == 1 && x == 1)
   //         puts("ya");
          ll sy = calc(sumy, y, x, l),
             sx = calc(sumx, y, x, l),
             total = calc(summ, y, x, l);
          for (int a = 0; a < 2; ++a)
            for (int b = 0; b < 2; ++b) {
              int i = y + a * (l - 1),
                  j = x + b * (l - 1);
              sy -= mass[i][j] * (2 * i + 1);
              sx -= mass[i][j] * (2 * j + 1);
              total -= mass[i][j];
            }

          if (sy == (l + 2 * y) * total && sx == (l + 2 * x) * total) {
            possible = true;
            printf("%i\n", l);
            goto end;
          }
        }
    }
end:;
    if (!possible) puts("IMPOSSIBLE");
  }
  return 0;
}
