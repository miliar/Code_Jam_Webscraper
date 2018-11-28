#include <stdio.h>

void main(void)
{
   long long ciclo[31];
   int sockets, estalos, T, i;

   ciclo[1] = 1;
   for ( i = 2 ; i < 31 ; i ++ )
   {
      ciclo[i] = ciclo[i-1]*2 + 1;
   }
   scanf("%d", &T);
   for (i = 0 ; i < T ; i ++ )
   {
      scanf("%d %d",&sockets, &estalos);
      if ( estalos < ciclo[sockets] )
         printf("Case #%d: OFF\n", i+1);
      else if (estalos == ciclo[sockets] )
         printf("Case #%d: ON\n", i+1);
      else
         printf("Case #%d: %s\n", i+1, ((estalos - ciclo[sockets])% (ciclo[sockets]+1)==0)?"ON":"OFF");
   } 
}
