#include <cstdio>
 
int t;
int n;
int a;
int res;
int main()
{
  scanf("%d",&t);
  for (int i=0; i<t; i++)
  {
    scanf("%d",&n);
    res = 0;
    for (int j=1;j<=n;j++)
    {
      scanf("%d", &a);
      if (a!=j) res++;
    }
    printf("Case #%d: %d\n",i+1,res);
  }
  return 0;
}