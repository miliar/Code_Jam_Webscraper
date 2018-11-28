#include <stdio.h>
#include <math.h>

int main()
{
   int kases;
   long long int store;
   scanf("%d", &kases);
   int i, N, K;

   for (i = 1; i <= kases; i++) {
      scanf("%d %d", &N, &K);
      store = (int)pow(2,N);
      printf("Case #%d: ", i);
      if ((K+1)%store == 0)
         printf("ON\n");
      else
         printf("OFF\n");
   }
   return 0;
}
