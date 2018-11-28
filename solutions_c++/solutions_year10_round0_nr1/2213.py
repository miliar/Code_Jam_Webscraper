#include <stdio.h>

int main()
{
  int num, n, k, c = 0, p;
  scanf("%d", &num);
  while (num)
  {
    c++;
    num--;
    scanf("%d %d", &n, &k);
    p = 1;
    p = p << n;
    if (k%p == p-1)
    {
      printf("Case #%d: ON\n", c);
    }
    else
    {
      printf("Case #%d: OFF\n", c);
    }
  }
  return 0;
}
