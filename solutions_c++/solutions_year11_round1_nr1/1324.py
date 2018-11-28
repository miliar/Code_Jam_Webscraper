#include <cstdio>

long long nn;
int n;
int pd,pg;

bool solve()
{
  scanf("%lld %d %d",&nn,&pd,&pg);
  if(nn>=100)
    return true;
  if((pd > 0) && (pg == 0))
    return false;
  if((pd < 100) && (pg == 100))
    return false;
  n = (int) nn;
  for(int i = 1; i<=n; i++)
    if(pd * i % 100 == 0)
      return true;
  return false;
}

main()
{
  int t;
  scanf("%d",&t);
  for(int tt=0; tt < t; tt++)
    if(solve())
      printf("Case #%d: Possible\n",tt+1);
    else
      printf("Case #%d: Broken\n",tt+1);
}
