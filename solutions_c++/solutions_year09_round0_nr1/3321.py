#include <stdio.h> 

int main()
{
   int a,b,c,d;
   for(a=4;a<=9;a++)
   {
      for(b=0;b<=9;b++)
      {
         for(c=0;c<=9;c++)
         {
            for(d=0;d<=9;d++)
            {
               if ( 100*a+110*b+11*c+d == 906 )
                  printf("%d %d %d %d =====  %d %d \n ",a,b,c,d, (100*a+10*b+c) - 453, 453 - (100*b + 10 * c + d)  );
            }
         }
      }
   }
return 0;
}
