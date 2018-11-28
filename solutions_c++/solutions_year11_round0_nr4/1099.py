#include <algorithm>
#include <cassert>
#include <cstdio>

using namespace std;

const int MaxN = 10004;

int a [MaxN];
int n;

int main (void)
{
 int test, tests;
 int i, s;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  s = 0;
  for (i = 1; i <= n; i++)
  {
   scanf (" %d", &a[i]);
   if (a[i] != i)
    s++;
  }
  printf ("Case #%d: %.10lf\n", test, (double) s);
 }
 return 0;
}
