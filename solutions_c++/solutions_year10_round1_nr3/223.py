#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
  int t, a1, a2, b1, b2, a, b, i;
  long long c;
  double phi1, phi2, low, high;
  phi1 = ( - 1 + sqrt(5.0) ) / 2.0;
  phi2 = ( 1 + sqrt(5.0) ) / 2.0;
  
  scanf("%d", &t);
  for (i = 0; i < t; i++) {
    c = 0;
    scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
    for (a = a1; a <= a2; a++) {
      low = (int)ceil(phi1 * a);
      high = (int)floor(phi2 * a);
      if ( low < b1 )
        low = b1;
      if ( low > b2 )
        low = b2 + 1;
      if ( high < b1 )
        high = b1 - 1;
      if ( high > b2 )
        high = b2;
      c += low - b1 + b2 - high;
    }
    
    
    printf("Case #%d: %lld\n", i + 1, c);
  }
  return 0;
}