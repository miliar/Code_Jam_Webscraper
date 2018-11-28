#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
  int T;

  scanf("%d", &T);

  for (int k = 1; k <= T; k++) {
    int n, s, p, t[100];

    scanf("%d%d%d", &n, &s, &p);
    for (int i = 0; i < n; i++) {
      scanf("%d", &t[i]);
    }

    sort(t, t + n);

    int count = 0;

    for (int i = 0; i < n; i++) {
      int maxScore = (t[i] + 2) / 3;
      int surScore = t[i] > 2 ? (t[i] + 4) / 3 : t[i];
      if (maxScore >= p) {
        count++;
      } else if (s > 0 && surScore >= p) {
        count++;
        s--;
      }
    }

    printf("Case #%d: %d\n", k, count);
  }

  return 0;
}
