#include <stdio.h>
int main()
{
    int t0, t;
    scanf("%ld",&t0); for (t = 1; t<= t0; t++) {
       long  n , k ;
       scanf("%ld%ld",&n,&k);
       long  w = (k & ((1 << n) -1));
//       printf("%d\n",w);
       if (w == (1<<n)-1) printf("Case #%d: ON\n",t);
         else printf("Case #%d: OFF\n",t);
    }
    return 0;
}
