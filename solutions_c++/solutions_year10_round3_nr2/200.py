#include <cstdio>

int main(void)
{
  int test, tests;
  long long l, p;
  int c, res, res2;
  freopen ("blarge.in", "rt", stdin);
  freopen ("blarge.out", "wt", stdout);

  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    res2 = res = 0;
    scanf ("%I64d %I64d %d", &l, &p, &c);
    while (l < p)
      l *= c, res2++;
    res2--;
    while (res2 > 0)
      res++, res2 /= 2;
    printf ("Case #%d: %d\n", test + 1, res);
  }
  
  return 0;
}
