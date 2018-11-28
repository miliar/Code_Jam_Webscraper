#include <stdio.h>

int main() {

  int T;
  scanf("%d", &T);
  for(int i = 0; i < T; ++i) {
    int n;
    int smallest = -1;
    int sum = 0;
    int bsum = 0;
    scanf("%d", &n);
    for(int j = 0; j < n; ++j) {
      int v;
      scanf("%d", &v);
      if(smallest == -1 || smallest > v) {
	smallest = v;
      }
      sum += v;
      bsum ^= v;
    }
    if(bsum == 0) {
      printf("Case #%d: %d\n", 1+i, sum-smallest);
    } else {
      printf("Case #%d: NO\n", 1+i);
    }
  }

  return(0);
}
