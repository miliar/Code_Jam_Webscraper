#include<cstdio>
int main()
{
  int t;
  scanf("%d",&t);
  for(int i=1;i<=t;++i)
  {
    int add=0,sum=0,min=1000000000,n;
    for(scanf("%d",&n);n;--n)
    {
      int x;
      scanf("%d",&x);
      add^=x;
      sum+=x;
      if(x<min)
        min=x;
    }
    printf("Case #%d: ",i);
    if(add)
      puts("NO");
    else
      printf("%d\n",sum-min);
  }
  return 0;
}
