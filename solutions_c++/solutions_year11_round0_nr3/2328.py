#include <cstdio>
#include <cstring>

int main ()
{
  int cases,index;
  scanf("%d",&cases);
  for(index=0;index<cases;index++)
  {
    int bf = 0;
    int n; scanf("%d",&n);
    int tot, mn;
    mn = 100000000;
    tot = 0;
    for(int i = 0; i < n; i ++ )
    {
      int a;
      scanf("%d",&a);
      bf ^= a;
      tot += a;
      if( mn > a ) mn = a;
    }
    printf("Case #%d: ", index+1);
    if( bf == 0 )
    {
      printf("%d\n",tot-mn);
    } else printf("NO\n");
  }
  return 0;
}
