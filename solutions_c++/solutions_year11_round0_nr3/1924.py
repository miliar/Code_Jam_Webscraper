//we need two piles with the same xor.
//it's possible iff total xor == 0
//than we can give one smallest candy to little brother
//and keep the rest.

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main (void)
{
  int test, tests, i, n, s, txor, mn, a;
  freopen ("c.in", "rt", stdin);
  freopen ("c.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    scanf ("%d", &n);
    mn = 1e9; txor = 0; s = 0;
    for (i = 0; i < n; i++)
    {
      scanf ("%d", &a);
      s += a;
      txor ^= a;
      if (mn > a)
        mn = a;
    }
    if (txor == 0)
      printf ("Case #%d: %d\n", test + 1, s - mn);
    else
      printf ("Case #%d: NO\n", test + 1);

  }
  return 0;
}
