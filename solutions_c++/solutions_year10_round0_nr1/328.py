#include <cstdio>

void process(int t)
{						
  int n,k;

  scanf("%d %d",&n,&k);
  k &= ((1 << n) - 1);
  if(k == (1 << n) -1)
    printf("Case #%d: ON\n",t);
  else
    printf("Case #%d: OFF\n",t);
}

main()
{
  int t;
  scanf("%d",&t);
  for(int i=0; i<t; i++)
    process(i+1);
}
