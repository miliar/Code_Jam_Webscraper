#include <stdio.h>
#include <stdlib.h>

int main()
{

    int T;
    int money=0;
    scanf("%i",&T);
    int R,K,N;


    int i=0;
    for(i=0;i<T;++i)
    {money=0;
     scanf("%i %i %i \n",&R,&K,&N);
    /* printf("%i %i %i\n",R,K,N);*/
     int *g=new int[N];
     int j=0;
     for(j=0;j<N;++j)
     {
      scanf("%i ",&g[j]);

    }

  /*for(j=0;j<N;++j)
     {
      printf("%i ",g[j]);

    }

*/
   int r=R;j=0;
   for(r=R;r>0;r--)
   { int tmp=0;
   int mark=0;
   while(tmp<K)
   {
    ++mark;
    if(mark>N) break;
    tmp+=g[j];
    if(tmp>K) break;
    money+=g[j];
    j=(j+1)%N;
   }

   }
   printf("Case #%i: %i\n",i+1,money);
    }

    return 0;
}
