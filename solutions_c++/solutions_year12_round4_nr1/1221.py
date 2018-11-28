#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int caseno = 1; caseno <= T; caseno++) {
    int N;
    scanf("%d", &N);
    vector<int> D(N), L(N);
    for (int i = 0; i < N; i++) scanf("%d%d", &D[i], &L[i]);
    int DT;
    scanf("%d", &DT);
    bool result = false;
    vector<int> best(N, -1);
    best[0] = D[0];
    int reached = 1;
    for (int i = 0; i < N; i++) {
      if (best[i] == -1) continue;
      best[i] = min(best[i], L[i]);
      int y = best[i];
//      fprintf(stderr, "[case%d] x=%d y=%d\n", caseno, D[i], y);
      while (reached < N && D[reached]-D[i] <= y) {
        best[reached] = D[reached]-D[i];
        reached++;
      }
      if (D[i]+y >= DT) result = true;
    }
    printf("Case #%d: %s\n", caseno, result ? "YES" : "NO");
  }
  return 0;
}
