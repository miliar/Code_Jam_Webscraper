#include<stdio.h>


int T, N;

int main() {
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    scanf("%d", &N);
    int xorr = 0, sum= 0, min = 10000000;
    for (int k = 0; k < N; k++) {
      int t;
      scanf("%d", &t);
    
      xorr ^= t;
      sum += t;
      min = (t < min) ? t : min;
    }
    if (xorr == 0) printf("Case #%d: %d\n", i +1, sum - min);
    else printf("Case #%d: NO\n", i+1);
    
  }
    
}
