#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

const int MaxN = 10, MaxL = 1 << MaxN, MaxC = 0x3F3F3F3F, NA = -1;

int p [MaxL << 1];
int s [MaxL << 1];
int f [MaxL << 1] [MaxN + 1];
int m, n;

int main (void)
{
 int test, tests;
 int i, j;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  m = 1 << n;
  memset (s, 0, sizeof (s));
  memset (p, 0, sizeof (p));
  for (i = m + m - 1; i >= m; i--)
   scanf (" %d", &s[i]);
  for (i = m - 1; i >= 1; i--)
   scanf (" %d", &p[i]);
  memset (f, MaxC, sizeof (f));
  for (i = m + m - 1; i >= m; i--)
   for (j = n - s[i]; j <= n; j++)
    f[i][j] = 0;
  for (i = m - 1; i >= 1; i--)
   for (j = 0; j <= n; j++)
   {
    if (j > 0)
     f[i][j] = min (f[i][j], f[i][j - 1]);
    f[i][j] = min (f[i][j],
     f[(i << 1) + 0][j] + f[(i << 1) + 1][j]);
    f[i][j] = min (f[i][j],
     p[i] + f[(i << 1) + 0][j + 1] + f[(i << 1) + 1][j + 1]);
//    printf ("f[%d][%d] = %d\n", i, j, f[i][j]);
   }
  printf ("Case #%d: %d\n", test, f[1][0]);
 }
 return 0;
}
