#include <stdio.h>

int n,sum,min,x,xs,t;

int main()
{
   scanf("%d", &t);
   for (int i=1; i<=t; i++)
   {
       min=10000000;
       sum=0;
       xs=0;
       scanf("%d", &n);
       for (int j=1; j<=n; j++)
       {
           scanf("%d", &x);
           sum = sum + x;
           xs = xs xor x;
           if (x<min) min = x;
       }
       if (xs==0)
       {
           printf("Case #");
           printf("%d", i);
           printf(": ");
           printf("%d\n", sum-min);
       }
       else
       {
           printf("Case #");
           printf("%d", i);
           printf(": ");
           printf("NO\n");
       }
   }
return 0;
}
