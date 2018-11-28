#include <stdio.h>
#include <algorithm>

int tc, a1, a2, b2, b1;

int check (int a, int b)
{
  if (a == b)
    return 0;
  if (a > b)
    std::swap (a, b);
  if (b / a > 1)
    return 1;
  return 1 - check (b - a, a);
}

int main ()
{
  scanf ("%d", &tc);
  for (int tt = 1; tt <= tc; tt++)
  {
    scanf ("%d%d%d%d", &a1, &a2, &b1, &b2);
    int ans = 0;
    for (int a = a1; a <= a2; a++)
    {
      for (int b = b1; b <= b2; b++)
      {
        ans += check (a, b);
      }
    }
    printf ("Case #%d: %d\n", tt, ans);
  }
}
