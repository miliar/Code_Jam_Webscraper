#include <cstdio>

using namespace std;

int eleva (int a, int b) {
  int res = 1;
  for (int i = 0; i < b; i++)
    res *= a;
  return res;
}

int main () {
  int T, N, K;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d%d", &N, &K);
    int pot = eleva (2, N);
    int min = eleva (2, N) - 1;
    //printf("min: %d\n", min);
    
    for (int a = 0; ; a++) {
      if (K < min) {
        printf ("Case #%d: OFF\n", t);
        break;
      }
      else if (K == min) {
        printf ("Case #%d: ON\n", t);
        break;
      }
      min += pot;
    }
  }
  return 0;
}
