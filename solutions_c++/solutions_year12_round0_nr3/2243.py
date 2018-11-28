#include <cstdio>
#include <set>
using namespace std;

int main() {
  int pw[9];
  pw[0] = 1;
  for (int i = 1; i < 9; i++) pw[i] = pw[i-1] * 10;

  int T;
  scanf("%d", &T);
  for (int Tn = 1; Tn <= T; Tn++) {
    int A, B;
    scanf("%d%d", &A, &B);
    int nn = 1;
    while (A >= pw[nn]) nn++;
    long long R = 0;
    for (int i = A; i <= B; i++) {
      int N = i;
      int M = i;
      set<int> found;
      for (int j = 0; j < nn-1; j++) {
        M = M/10 + (M%10)*pw[nn-1];
        if (N < M && A <= M && M <= B) {
          //printf("(%d,%d)\n", N, M);
          found.insert(M);
        }
      }
      R += found.size();
    }
    printf("Case #%d: %lld\n", Tn, R);
  }
  return 0;
}
