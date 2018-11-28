#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef long long int64;
typedef double real;

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif

const int MaxN = 507, MaxC = 0x3F3F3F3F, NA = -1;

int64 a [MaxN] [MaxN];
int d, m, n;

int main (void)
{
 int test, tests;
 scanf (" %d", &tests);
 int i, j, k, l, p, q;
 int64 sx, sy;
 bool ok;
 char ch;
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d %d %d", &m, &n, &d);
  for (i = 0; i < m; i++)
   for (j = 0; j < n; j++)
   {
    scanf (" %c", &ch);
    a[i][j] = d + (ch - '0');
   }
  ok = false;
  for (k = MaxN; !ok && k >= 3; k--)
   if (k & 1)
   {
    l = k >> 1;
    for (i = l; !ok && i + l < m; i++)
     for (j = l; !ok && j + l < n; j++)
     {
      sx = 0;
      sy = 0;
      for (p = -l; p <= l; p++)
       for (q = -l; q <= l; q++)
        if (abs (p) != l || abs (q) != l)
        {
         sx += a[i + p][j + q] * p;
         sy += a[i + p][j + q] * q;
        }
//      printf ("%d %d %d: " INT64 " " INT64 "\n", k, i, j, sx, sy);
      if (sx == 0 && sy == 0)
       ok = true;
     }
   }
   else
   {
    l = k >> 1;
    for (i = l; !ok && i + l <= m; i++)
     for (j = l; !ok && j + l <= n; j++)
     {
      sx = 0;
      sy = 0;
      for (p = -l; p < l; p++)
       for (q = -l; q < l; q++)
        if ((p != -l && p != l - 1) || (q != -l && q != l - 1))
        {
         sx += a[i + p][j + q] * (p * 2 + 1);
         sy += a[i + p][j + q] * (q * 2 + 1);
        }
//      printf ("%d %d %d: " INT64 " " INT64 "\n", k, i, j, sx, sy);
      if (sx == 0 && sy == 0)
       ok = true;
     }
   }
  printf ("Case #%d: ", test);
  if (!ok)
   printf ("IMPOSSIBLE\n");
  else
   printf ("%d\n", k + 1);
 }
 return 0;
}
