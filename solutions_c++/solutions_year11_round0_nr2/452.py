#include <math.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <complex>
#include <map>
#include <set>
#include <string>
#include <vector>

int ans[100];
int gen[26][26];
bool op[26][26];

int main() {
  int case_size, C, D, n;
  char ch1, ch2, ch3;
  scanf("%d", &case_size);
  for (int T = 1; T <= case_size; ++T) {
    memset(gen, -1, sizeof(gen));
    scanf("%d", &C);
    for (int i = 0; i < C; ++i) {
      scanf(" %c%c%c", &ch1, &ch2, &ch3);
      gen[ch1 - 'A'][ch2 - 'A'] = ch3 - 'A';
      gen[ch2 - 'A'][ch1 - 'A'] = ch3 - 'A';
    }
    memset(op, false, sizeof(op));
    scanf("%d", &D);
    for (int i = 0; i < D; ++i) {
      scanf(" %c%c", &ch1, &ch2);
      op[ch1 - 'A'][ch2 - 'A'] = op[ch2 - 'A'][ch1 - 'A'] = true;
    }
    int size = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf(" %c", &ch1);
      int id = ch1 - 'A';
      if (size > 0 && gen[ans[size - 1]][id] != -1) {
        ans[size - 1] = gen[ans[size - 1]][id];
      } else {
        bool found = false;
        for (int j = 0; j < size; ++j) {
          if (op[id][ans[j]]) {
            size = 0;
            found = true;
            break;
          }
        }
        if (!found) ans[size++] = id;
      }
    }
    printf("Case #%d: [", T);
    for (int i = 0; i < size; ++i) {
      if (i != 0) printf(", ");
      printf("%c", ans[i] + 'A');
    }
    puts("]");
  }
  return 0;
}
