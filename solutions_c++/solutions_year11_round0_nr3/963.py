#include<stdio.h>

int main()
{
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; i++)
  {
    int c;
    scanf("%d", &c);
    int x = 0;
    int min = 1000000000;
    int sum = 0;
    for(int j = 0; j < c; j++)
    {
      int candie;
      scanf("%d", &candie);
      x ^= candie;
      min = (min < candie) ? min : candie;
      sum += candie;
    }
    if(x != 0)
      printf("Case #%d: NO\n", i);
    else
      printf("Case #%d: %d\n", i, sum - min);
  }
  return 0;
}
