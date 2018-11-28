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
  int op[26][26];
  char comb[26][26];
  char res[10000000], str[3], ch;
  int len, t, a, b, c, n;
  scanf("%d\n", &t);
  forn(tt, t) {
    forn(i, 26) forn(j, 26) {
      op[i][j] = 0;
      comb[i][j] = '0';
    }
    len = 0;
    scanf("%d", &n);
    forn(i, n) {
      scanf("%s", str);
      a = (int)(str[0] - 'A');
      b = (int)(str[1] - 'A');
      comb[a][b] = comb[b][a] = str[2];
    }
    scanf("%d", &n);
    forn(i, n) {
      scanf("%s", str);
      a = (int)(str[0] - 'A');
      b = (int)(str[1] - 'A');
      op[a][b] = op[b][a] = 1;
    }
    scanf("%d ", &n);
    forn(i, n) {
      ch = getchar();
      a = (int) (ch - 'A');
      if (len == 0) {
        res[len++] = ch;
        c = a;
      } else {
        int addIt = 1, oposed = 0;
        if (comb[a][b] != '0') {
          res[len - 1] = comb[a][b];
          a = (int) comb[a][b];
          if (len - 1 == 0) c = a;
          addIt = 0;
        }
        forn(i, len) {
          if (op[a][(int)(res[i] - 'A')]) {
            oposed = 1;
            addIt = 0;
            break;
          }
        }
        if (oposed) {
          len = 0;
        }
        if (addIt) res[len++] = ch;
      }
      b = a;
    }
    printf("Case #%d: [", tt+1);
    forn(i, len) {
      if (i == 0) printf("%c", res[i]);
      else printf(", %c", res[i]);
    }
    printf("]\n");
  }
}

int main() {
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  calc();

  return 0;
}
