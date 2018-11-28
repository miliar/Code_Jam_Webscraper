#include "cmath"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

char combo[26 * 26];
bool oppo[26][26];
char seq[100];
int len;

int main() {
  freopen("B-small-attempt3.in","r",stdin);freopen("B-small-attempt3.out","w",stdout);
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    // solve
    memset(combo, -1, sizeof(combo));
    memset(oppo, 0, sizeof(oppo));
    memset(seq, -1, sizeof(seq));
    len = 0;
    // input
    int c, d, n;
    char x, y, z;
    int k;
    scanf("%d", &c);
    fprintf(stderr, "c=%d\n", c);
    for (int i = 0; i < c; ++i) {
      scanf(" %c%c%c", &x, &y, &z);
      x -= 'A';
      y -= 'A';
      z -= 'A';
      k = min(x, y) * 26 + max(x, y);
      combo[k] = z;
    }
    scanf("%d", &d);
    fprintf(stderr, "d=%d\n", d);
    for (int i = 0; i < d; ++i) {
      scanf(" %c%c", &x, &y);
      x -= 'A';
      y -= 'A';
      oppo[x][y] = true;
      oppo[y][x] = true;
    }
    scanf("%d ", &n);
    fprintf(stderr, "n=%d\n", n);
    for (int i = 0; i < n; ++i) {
      scanf("%c", &x);
      fprintf(stderr, "%c", x);
      x -= 'A';
      while (len > 0) {
        y = seq[len - 1];
        k = min(x, y) * 26 + max(x, y);
        if (combo[k] != -1) {
          x = combo[k];
          //seq[--len] = -1;
          --len;
        }
        else {
          break;
        }
      }
      bool clear = false;
      for (int j = 0; j < len; ++j) {
        if (oppo[x][seq[j]]) {
          clear = true;
          break;
        }
      }
      if (clear) {
        //memset(seq, -1, sizeof(seq));
        len = 0;
      }
      else {
        seq[len++] = x;
      }
    }
    fprintf(stderr, "\n");
    // output
    printf("Case #%d: [", Ti);
    for (int i = 0; i < len; ++i) {
      printf("%c", seq[i] + 'A');
      if (i < len - 1)
        printf(", ");
    }
    printf("]\n");
  }
  return 0;
}
