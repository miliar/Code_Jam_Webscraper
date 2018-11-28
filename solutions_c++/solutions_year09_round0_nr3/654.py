#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

const int MaxN = 102, MaxL = 512, MaxK = 25, MOD = 10000;
const char p [] = "welcome to code jam";

int f [MaxL] [MaxK];
char a [MaxL];
int k, n;

int main (void)
{
 int test, tests;
 int i, j;
 scanf (" %d", &tests);
 fgets (a, MaxL, stdin);
 k = strlen (p);
 for (test = 1; test <= tests; test++)
 {
  fgets (a, MaxL, stdin);
  n = strlen (a);
  memset (f, 0, sizeof (f));
  f[0][0] = 1;
  for (i = 0; i <= n; i++)
   for (j = 0; j <= k; j++)
   {
    f[i + 1][j] += f[i][j];
    if (f[i + 1][j] >= MOD)
     f[i + 1][j] -= MOD;
    if (a[i] == p[j])
    {
     f[i + 1][j + 1] += f[i][j];
     if (f[i + 1][j + 1] >= MOD)
      f[i + 1][j + 1] -= MOD;
    }
   }
  printf ("Case #%d: %04d\n", test, f[n][k]);
 }
 return 0;
}
