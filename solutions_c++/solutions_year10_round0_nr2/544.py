#include <stdio.h>
#include <algorithm>

int tc, ans, g, n;
int a[10], b[10], c[10];

int gcd (int a, int b)
{
  while (b != 0)
  {
    int r = a % b;
    a = b; b = r;
  }
  return a;
}

int main ()
{
  scanf ("%d", &tc);
  for (int tt = 1; tt <= tc; tt++)
  {
    scanf ("%d", &n);
    for (int i = 0; i < n; i++)
    {
      scanf ("%d", &a[i]);
    }
    for (int i = 1; i < n; i++)
    {
      b[i] = abs(a[i - 1] - a[i]);
    }
    int g = b[1];
    for (int i = 2; i < n; i++)
    {
      if (b[i] != 0)
      {
        if (g == 0) g = b[i];
        else g = gcd (g, b[i]);
      }
    }
    fprintf (stderr, "gcd: %d\n", g);
    int ans = 0;
    if (g != 0)
    {
      ans = (g - (a[0] % g)) % g;
    }
    printf ("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
