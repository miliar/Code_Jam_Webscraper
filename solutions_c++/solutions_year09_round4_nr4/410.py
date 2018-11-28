#include <math.h>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main() {
  int K, N, T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d\n", &N);
    int plant[N][3];
    for (int i = 0; i < N; ++i)
      scanf("%d %d %d\n", &plant[i][0], &plant[i][1], &plant[i][2]);
    double best;
    if (N == 1) {
      best = (double)plant[0][2];
    } else if (N == 2) {
      best = (double)(max(plant[0][2], plant[1][2]));
    } else {
      best = 1.0E9;
      for (int i = 0; i < N; ++i) {
        for (int j = i+1; j < N; ++j) {
          int k = 3 - i - j;
          double d = hypot(plant[i][0]-plant[j][0], plant[i][1]-plant[j][1]);
          d += plant[i][2] + plant[j][2];
          best = min(best, max(0.5*d, (double)plant[k][2]));
        }
      }
    }
    printf("Case #%d: %.6lf\n", t, best);
  }
  return 0;
}
