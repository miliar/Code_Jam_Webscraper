#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int s[1234567];
long long p[123456];

int main (void)
{
  int test, tests, i, j;
  long long t, n;
  int res;
  int k = 0;
  freopen ("c.in", "rt", stdin);
  freopen ("c.out", "wt", stdout);
  memset (s, 0, sizeof(s));
  s[0] = s[1] = 1;
  for (i = 2; i * i < 1234567; i++)
  {
    if (s[i] == 0)
      for (j = i * i; j < 1234567; j += i)
        s[j] = 1;
  }

  for (i = 0; i < 1234567; i++)
    if (s[i] == 0)
      p[k++] = i;
//  cout << k << '\n';

  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    res = 0;
    scanf ("%I64d", &n);
    if (n > 1)
      res++;
    for (i = 0; p[i] * p[i] <= n; i++)
    {
      t = p[i]; k = 0;
      while (t * p[i] <= n)
        t = t * p[i], k++;
      res += k;
    }
    printf ("Case #%d: %d\n", test + 1, res);
  }
  return 0;
}
