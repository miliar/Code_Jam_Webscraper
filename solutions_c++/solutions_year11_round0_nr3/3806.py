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

int n;
int c[1000];

int main() {
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    // input
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
      scanf("%d", &c[i]);
    // brutal force...
    int max_value = -1;
    for (int s = 1; s < (1 << (n - 1)); ++s) {
      //fprintf(stderr, "s=0%o\n", s);
      int a = 0, b = 0;
      int x = 0, y = 0;
      for (int i = 0, k = s; i < n; ++i, k >>= 1) {
        if ((k & 1) != 0) {
          a += c[i];
          x ^= c[i];
        }
        else {
          b += c[i];
          y ^= c[i];
        }
      }
      if (x == y && max(a, b) > max_value)
        max_value = max(a, b);
      //fprintf(stderr, "x=0%o y=0%o a=%d b=%d max=%d\n", x, y, a, b, max_value);
    }
    // output
    if (max_value == -1)
      printf("Case #%d: NO\n", Ti);
    else
      printf("Case #%d: %d\n", Ti, max_value);
  }
  return 0;
}
