#include <cstdio>
#include <string>
#include <vector>
#include <set>

using namespace std;

int main () {
  int C, N, K, B, T;
  scanf ("%d", &C);
  for (int c = 1; c <= C; c++) {
    int swaps = 0, chicks = 0;
    scanf ("%d%d%d%d", &N, &K, &B, &T);
    vector<int> X = vector<int> (N), V = vector<int> (N);
    for (int i = 0; i < N; i++) {
      int x;
      scanf("%d", &x);
      X[i] = x;
    }
    for (int i = 0; i < N; i++) {
      int x;
      scanf("%d", &x);
      V[i] = x;
    }
    
    for (int i = N-1; i >= 0; i--) {
      //printf ("%f\n", ((1.0*B) - (1.0*X[i]))/(1.0*V[i]) );
      if ((1.0*B - 1.0*X[i])/(1.0*V[i]) <= T) {
        //printf ("%d\n", i);
        chicks++;
        for (int j = i + 1; j < N; j++) {
          if ( (1.0*B - 1.0*X[j])/(1.0*V[j]) > T)
            swaps++;
        }
        if (chicks >= K)
          break;
      }
    }
    if (chicks < K) 
      printf ("Case #%d: IMPOSSIBLE\n", c);
    else
      printf ("Case #%d: %d\n", c, swaps);
  }
  return 0;
}
