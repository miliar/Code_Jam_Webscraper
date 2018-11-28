#include <cstdio>
#include <vector>
using namespace std;

#define MAXC 1048576
int tab[2][MAXC];

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int N;
    int gx = 0;
    int minval = MAXC + 1;
    int sum = 0;
    scanf("%d", &N);
    vector<int> A(N);
    for(int i = 0; i < N; i++) {
      scanf("%d", &A[i]);
      gx ^= A[i];
      sum += A[i];
      if(A[i] < minval) minval = A[i];
    }
    if(gx != 0) {
      printf("Case #%d: NO\n", t);
      continue;
    }
    printf("Case #%d: %d\n", t, sum - minval);
  }
  return 0;
}

