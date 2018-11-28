#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

typedef signed   long long i64;
typedef unsigned long long u64;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define setall(x, val) memset((x), (val), sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define For(i, st, en) for(iint i=(st); i<=(en); i++)
#define Ford(i, st, en) for(iint i=(st); i>=(en); i--)
#define forn(i, n) for(int i=0; i<(i64)(n); i++)
#define fors(i, n, s) for(int i=s; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define ind(i, j, cols) (i * cols + j)


void calc() {
  int posb, poso, diff, go, gb, b, n, t, res, add;
  char pch[1];
  scanf("%d\n", &t);
  forn(tt, t) {
    scanf("%d", &n);
    res = posb = poso = diff = 0;
    go = gb = 0;
    while (n--) {
      scanf("%s %d", pch, &b); b--;
      if (pch[0] == 'B') {
        diff = abs(posb - b);
        posb = b;
        add = diff + 1 - go;
        if (add < 1) add = 1;
        gb += add;
        go = 0;
      } else {
        diff = abs(poso - b);
        poso = b;
        add = diff + 1 - gb;
        if (add < 1) add = 1;
        go += add;
        gb = 0;
      }
      res += add;
    }
    printf("Case #%d: %d\n", tt+1, res);
  }
}

int main() {
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  calc();

  return 0;
}
