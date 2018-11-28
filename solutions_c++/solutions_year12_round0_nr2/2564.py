#include <cstdio>

int main()
{
  int t;

  scanf("%d", &t);

  for ( int i = 0; i < t; ++i )
  {
    int n, s, p;
    int surprising = 0;
    int nb = 0;
    scanf("%d %d %d", &n, &s, &p);
    for ( int j = 0; j < n; ++j )
    {
      int tot;
      scanf("%d", &tot);
      if ( (tot + 2) / 3 >= p )
      {
        nb++;
      }
      else if ( (tot + 4) / 3 >= p && surprising < s && tot >= 2)
      {
        nb++;
        surprising++;
      }
    }
    printf("Case #%d: %d\n", i + 1, nb);
  }

  return 0;
}
