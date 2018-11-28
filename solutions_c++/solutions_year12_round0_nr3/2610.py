#include <cstdio>

int powlog10(unsigned int v)
{
  return  (v >= 1000000000) ? 1000000000 : (v >= 100000000) ? 100000000 : (v >= 10000000) ? 10000000 : 
          (v >= 1000000) ? 1000000 : (v >= 100000) ? 100000 : (v >= 10000) ? 10000 : 
          (v >= 1000) ? 1000 : (v >= 100) ? 100 : (v >= 10) ? 10 : 1;
}

int turn(int n, int thesize)
{
  int p = n / 10;
  int r = n % 10;
  return p + r * thesize;
}

int main()
{
  int t;
  scanf("%d", &t);

  for ( int i = 1; i <= t; ++i )
  {
    int a, b;
    int nb = 0;
    scanf("%d %d", &a, &b);
    // A and B have the same number of digits
    int thesize = powlog10(a);
    
    for ( int j = a; j <= b; ++j )
    {
      int turned = turn(j, thesize);
      while ( turned != j )
      {
        if ( j < turned && turned <= b )
        {
          nb++;
        }
        turned = turn(turned, thesize);
      }
    }
    printf("Case #%d: %d\n", i, nb);
  }
  return 0;
}
