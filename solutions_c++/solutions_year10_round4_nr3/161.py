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

const int MaxN = 1003, MaxL = 102, MaxC = 0x3F3F3F3F, NA = -1;

bool a [MaxL + 1] [MaxL + 1];
int xa [MaxN], ya [MaxN], xb [MaxN], yb [MaxN];
int n;

int main (void)
{
 int test, tests;
 int i, j, k, res;
 bool ok;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  memset (a, 0, sizeof (a));
  for (i = 0; i < n; i++)
  {
   scanf (" %d %d %d %d", &xa[i], &ya[i], &xb[i], &yb[i]);
   for (j = xa[i]; j <= xb[i]; j++)
    for (k = ya[i]; k <= yb[i]; k++)
     a[j][k] = true;
  }

  for (res = -1, ok = true; ok; res++)
  {
/*
   for (j = 1; j <= MaxL; j++)
   {
    for (k = 1; k <= MaxL; k++)
     putchar (a[j][k] + '0');
    putchar ('\n');
   }
   putchar ('\n');
*/
   ok = false;
   for (j = MaxL; j > 0; j--)
    for (k = MaxL; k > 0; k--)
    {
     ok |= a[j][k];
     if (a[j][k - 1] && a[j - 1][k])
      a[j][k] = true;
     if (!a[j][k - 1] && !a[j - 1][k])
      a[j][k] = false;
    }
  }
  printf ("Case #%d: %d\n", test, res);
  fflush (stdout);
 }
 return 0;
}
