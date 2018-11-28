# include <stdio.h>
# include <string.h>

int main()
{
    long l,test,p,q,k,n;



   scanf("%ld",&test);
   for(l=1;l<=test;l++)
   {

       scanf("%ld%ld",&n,&k);
       p = (1 << n)-1;
       q = k%(1<<n);

       if(p == q)printf("Case #%ld: ON\n",l);
       else printf("Case #%ld: OFF\n",l);
   }
  return 0;
}
