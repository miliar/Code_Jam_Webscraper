
#include <stdio.h>
#include <string.h>
#include <malloc.h>


main() {

  
  int T;
  scanf("%d",&T);
  
  

  for (int t = 1; t <= T; t++) {
    int m;
    int N;
    int S;
    int p;

    scanf("%d %d %d",&N,&S,&p);
    
    int n = 0;
    int s = 0;
    
    for (int i = 0; i < N; i++) {
      int t;
      scanf("%d",&t);
      if (t > 3*p - 3) {
	n++;
      }
      else {
	if ((t>=2) && (t >= 3*p - 4)) {
	  s++;
	}
      }
      if (s > S) s = S;
      
      

    }
        
    printf("Case #%d: %d\n",t,n+s);
  }





}
