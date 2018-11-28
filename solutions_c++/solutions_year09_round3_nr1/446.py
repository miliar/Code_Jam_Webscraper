#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

const int MaxN = 36, MaxL = 128;
int a [MaxN];
char s [MaxL];

typedef long long int64;

int main (void)
{
 int d, i, k, n;
 int64 ans;
 int test, tests;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf ("%s", s);
  n = strlen (s);
  memset (a, -1, sizeof (a));
  k = 0;
  for (i = 0; i < n; i++)
  {
   if (s[i] >= '0' && s[i] <= '9')
    d = s[i] - '0';
   else if (s[i] >= 'a' && s[i] <= 'z')
    d = s[i] - 'a' + 10;
   else assert (false);
   if (a[d] == -1)
   {
    if (k < 2)
     a[d] = 1 - k;
    else
     a[d] = k;
    k++;
   }
  }
  if (k < 2)
   k = 2;
  ans = 0;
  for (i = 0; i < n; i++)
  {
   if (s[i] >= '0' && s[i] <= '9')
    d = s[i] - '0';
   else if (s[i] >= 'a' && s[i] <= 'z')
    d = s[i] - 'a' + 10;
   else assert (false);
   assert (a[d] != -1);
   ans = ans * k + a[d];
  }
  printf ("Case #%d: %I64d\n", test, ans);
 }
 return 0;
}
