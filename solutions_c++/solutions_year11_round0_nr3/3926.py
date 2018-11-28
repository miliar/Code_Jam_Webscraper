#include <stdio.h>
int main()
{
    int n,sum,min,x,x1,t;
   //freopen("C-small-attempt0.in","r",stdin);
   //freopen("output.txt","w",stdout);
   scanf("%d", &t);
   for (int i=1; i<=t; i++)
   {
       min=1000000;
       sum=0;
       x1=0;
       scanf("%d", &n);
       for (int j=1; j<=n; j++)
       {
           scanf("%d", &x);
           sum = sum + x;
           x1 = x1 xor x;
           if (x<min) min = x;
       }
       if (x1==0)
           printf("Case #%d: %d\n", i, sum-min);
       else
           printf("Case #%d: NO\n", i);
   }
}
