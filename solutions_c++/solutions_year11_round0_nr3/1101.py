#include <algorithm>
#include <cassert>
#include <cstdio>

using namespace std;

const int MaxN = 10004, MaxC = 0x3F3F3F3F;

int a [MaxN];
int s, m, x, n;

int main (void)
{
 int test, tests;
 int i;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  s = 0;
  x = 0;
  m = MaxC;
  for (i = 0; i < n; i++)
  {
   scanf (" %d", &a[i]);
   s += a[i];
   x ^= a[i];
   m = min (m, a[i]);
  }
  printf ("Case #%d: ", test);
  if (x == 0)
   printf ("%d\n", s - m);
  else
   printf ("NO\n");
 }
 return 0;
}
