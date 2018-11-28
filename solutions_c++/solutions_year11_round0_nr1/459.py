#include <math.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <complex>
#include <map>
#include <set>
#include <string>
#include <vector>

char ch[100];
int pos[100];
int nexto[100], nextb[100];

inline int Sgn(int x) {
  if (x == 0) return 0;
  return x < 0 ? -1 : 1;
}

int main() {
  int case_size, n;
  scanf("%d", &case_size);
  for (int T = 1; T <= case_size; ++T) {
    scanf("%d", &n);
    memset(nexto, -1, sizeof(nexto));
    memset(nextb, -1, sizeof(nextb));
    for (int i = 0; i < n; ++i) {
      scanf(" %c%d", ch + i, pos + i);
    }
    int o = n, b = n;
    for (int i = n - 1; i >= 0; --i) {
      nexto[i] = o;
      nextb[i] = b;
      if (ch[i] == 'O') o = i;
      else b = i;
    }
    o = b = 1;
    int step = 0, delta;
    for (int i = 0; i < n; ++i) {
      if (ch[i] == 'O') {
        delta = std::abs(pos[i] - o) + 1;
        o = pos[i];
        if (nextb[i] != n) {
          if (std::abs(pos[nextb[i]] - b) <= delta) b = pos[nextb[i]];
          else b += Sgn(pos[nextb[i]] - b) * delta;
        }
        step += delta;
      } else {
        delta = std::abs(pos[i] - b) + 1;
        b = pos[i];
        if (nexto[i] != n) {
          if (std::abs(pos[nexto[i]] - o) <= delta) o = pos[nexto[i]];
          else o += Sgn(pos[nexto[i]] - o) * delta;
        }
        step += delta;
      }
    }
    printf("Case #%d: %d\n", T, step);
  }
  return 0;
}
