#include <cstdio>
#include <cstring>

int main (void)
{
  int test, tests, n, k;
  freopen ("alarge.in", "rt", stdin);
  freopen ("alarge.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    scanf ("%d %d", &n, &k);
    k++;
    if (k % (1 << n))
      printf ("Case #%d: OFF\n", test + 1);
    else
      printf ("Case #%d: ON\n", test + 1);
  }
  return 0;
}
