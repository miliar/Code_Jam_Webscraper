#include <cstdio>
 
int t;
int n;
int min;
int sum;
int s;
int c;
int main()
{
  scanf("%d",&t);
  for (int i=0;i<t;i++)
  {
   scanf("%d",&n);
   sum = 0;
   s = 0;
   min = 1111111;
   for (int j=0;j<n;j++)
   {
     scanf("%d",&c);
     sum = sum + c;
     s = s^c;
     if (c < min) min = c;
   }
   if (s == 0)
    printf("Case #%d: %d\n",i+1,sum-min);
   else
    printf("Case #%d: NO\n",i+1);
  }
  return 0;
}