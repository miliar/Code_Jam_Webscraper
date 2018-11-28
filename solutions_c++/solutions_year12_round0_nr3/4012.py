#include <cstdio>
#include <set>

using namespace std;

const int MAX_STEPS = 8;

int ten[MAX_STEPS];

int main() {
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);

  ten[0] = 1;
  for (int i = 1; i < MAX_STEPS; ++i) {
    ten[i] = ten[i-1] * 10;
  }

  int tests;
  scanf("%d ", &tests);
  for (int t = 1; t <= tests; ++t) {
    int low, high;
    scanf("%d %d ", &low, &high);
    int sol = 0;

    for (int i = low; i <= high; ++i) {
      int number = i, log10 = 0;
      while (number > 0) {
        number /= 10;
        log10++;
      }

      set<int> used;
      for (int j = 1; j <= log10; ++j) {
        int rest = (i % ten[j]);
        if (rest < ten[j-1]) {
          continue;
        }
        int other = rest * ten[log10-j] + i / ten[j];
        if (other >= low && other < i && used.find(other) == used.end()) {
          used.insert(other);
          ++sol;
        }
      }
    }

    printf("Case #%d: %d\n", t, sol);
  }

  return 0;
}
