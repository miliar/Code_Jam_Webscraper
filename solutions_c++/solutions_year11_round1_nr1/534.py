
#include <stdio.h>

int prime[101];

long int gcd(long int a,long int b) {
  
  if (a < b) return gcd(b,a);

  if (b == 0) return a;

  return gcd(b,a % b);

}

long int mmc(long int a, long int b) {

  return (a * b) / gcd(a,b);

}

main() {


  for (int i = 1; i <= 100; i++) {
    prime[i] = 1;
  }
  prime[1] = 0;
  
  for (int j = 1 ; j < 11; j++) {
    if (prime[j] == 1) {
      
      for (int p = 2*j; p <= 100; p+=j) {
	prime[p] = 0;
      }
    }
  }

  // for (int i = 1; i <= 100; i++) {
  // if (prime[i]) printf("%d ",i);
  // }

  int T;
  
  scanf("%d",&T);

  for (int t = 1; t <= T; t++) {

    long int n, pd, pg;
    
    scanf("%ld %ld %ld",&n,&pd,&pg);

    // need greatest common multiple of 100 and pd
    
    
    
    long int d = 0;
    if (pd != 0) 
      d = mmc(100,pd) / pd;
    long int g = 0;
    if (pg != 0) 
      g = mmc(100,pg) / pg;
    
    if ((d <= n) && (( pg != 100) || ( pd == pg))
	&& ((pg != 0) || (pd == 0))
	) {
      printf( "Case #%d: Possible\n",t);      
    }
    else {
      printf( "Case #%d: Broken\n",t);      
    }
    


  }



}
