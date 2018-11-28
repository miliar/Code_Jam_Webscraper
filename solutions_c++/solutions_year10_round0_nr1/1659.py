#include <stdio.h>
#include <math.h>

int main()
{
  int T;
  
  scanf("%d", &T);
  
  for(int i = 0; i < T; i++)
  {
    unsigned int N, K;
    unsigned int Kp;
    scanf("%u %u", &N, &K);
    
    Kp = pow(2, N);
    
    //printf("%u %u: %u\n", N, K, Kp);
    //printf(" - %u == %u\n", K & (Kp-1), Kp-1);
    
    printf("Case #%i: %s\n", i+1, (K & (Kp-1)) == Kp-1 ? "ON" : "OFF");
  }
  
  return 0;
}

