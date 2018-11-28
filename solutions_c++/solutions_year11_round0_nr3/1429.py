#include <stdio.h>


main() {

  int T;
  
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {

    
    int N;
    scanf("%d",&N);
    
    long int min = 100000000;
    long int sum = 0;
    long int x = 0;
    
    for (int n = 0; n < N; n++) {
      long int val;
      scanf("%ld",&val);
      x = x xor val;
      if (val < min) {
	min = val;
      }
      sum += val;
    }

    if (x != 0) {
      printf("Case #%d: NO\n",t);
    }
    else {
      printf("Case #%d: %ld\n",t,sum-min);
    }
    
  }



}
