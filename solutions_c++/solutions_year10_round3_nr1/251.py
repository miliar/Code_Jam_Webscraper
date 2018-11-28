#include <cstdio>

int a[1111], b[1111];

int main(void)
{
  int test, tests;
  int i, j, n, res = 0;
  freopen ("alarge.in", "rt", stdin);
  freopen ("alarge.out", "wt", stdout);

  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    res = 0;
    scanf ("%d", &n);
    for (i = 0; i < n; i++)
    {
      scanf ("%d %d", &a[i], &b[i]);
      for (j = 0; j < i; j++)
      if ((a[i] - a[j]) * (b[i] - b[j]) < 0)
        res++;
    }
    printf ("Case #%d: %d\n", test + 1, res);
  }
  
  return 0;
}
