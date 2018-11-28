#include<cstdio>

int t, caso, r, x, a, n, menor, suma;

main(){

scanf("%d", &t);
for(caso=1;caso<=t;caso++)
{
   menor = 2000000;
   suma = 0;
   scanf("%d", &n);
   for(r=x=0;x<n;x++)
   {
      scanf("%d", &a);
      suma += a;
      if( a < menor )
          menor = a;
      r = (r^a);
   }
   printf("Case #%d: ", caso);
   if( r == 0 )
      printf("%d\n", suma-menor);
   else
      printf("NO\n");
}

return 0;
}
