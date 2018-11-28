#include <stdio.h>

main() {


  int T;

  scanf("%d",&T);

  for (int i = 1; i <=T; i++) {
    int n,k;

    scanf("%d %d",&n,&k);
    
    int power = 1 << n;
    
    if ( (k % power) == (power - 1)) {
      printf("Case #%d: ON\n",i);
    }
    else {
      printf("Case #%d: OFF\n",i);
    }
  }


}
