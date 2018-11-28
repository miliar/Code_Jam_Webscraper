#include <stdio.h>
#include <stdlib.h>
int  main()
{
      int test,i,j;
      //freopen("A-large.in","r",stdin);
     // freopen("out.txt","w",stdout);
      scanf("%d",&test);
      for( i = 1; i <= test; i++ ) {
             int  n , k;
             scanf("%d%d",&n,&k);
             n = (1<<n);
             k  = k%n;
             printf("Case #%d: ",i);
             if( k == n-1 ) puts("ON");
             else  puts("OFF");
      }
      return 0;
}
