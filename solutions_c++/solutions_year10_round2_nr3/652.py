#include <cstdio>
#include <cstring>

const int Mod = 100003, MaxN = 555;

int c[MaxN][MaxN];
int f[MaxN][MaxN];
int res[MaxN];

int main(void)
{
  int i, j, k;
  int test, tests, n;
  memset (c, 0, sizeof(c));
  c[1][1] = 1;

  for (i = 2; i < MaxN; i++)
    for (j = 1; j < MaxN; j++)
      c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % Mod;

/*
  for (i = 0; i < 10; i++)
    for (j = 0; j < 10; j++)
      printf ("%5d%c", c[i][j], (j == 9)?'\n':' ');
*/

  printf ("\n");
  memset (f, 0, sizeof(f));
  for (j = 0; j < MaxN; j++)
    f[1][j] = 1;


  for (k = 1; k < MaxN; k++)
    for (j = 1; j < MaxN; j++)
      for (i = 1; i < k; i++)
        f[k][j] += (f[i][k] * c[k - i][j - k]) % Mod;

/*
  for (i = 0; i < 10; i++)
    for (j = 0; j < 10; j++)
      printf ("%5d%c", f[i][j], (j == 9)?'\n':' ');
*/
 
  memset (res, 0, sizeof(res));

  for (i = 0; i < MaxN; i++)
    res[i] = f[i][i+1] % Mod;


  for (i = 0; i < 10; i++)
      printf ("%3d%c", res[i], (i == 9)?'\n':' ');


  freopen ("csmall.in", "rt", stdin);
  freopen ("csmall.out", "wt", stdout);

  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    scanf ("%d", &n);
    printf ("Case #%d: %d\n", test + 1, res[n]);
  }

  return 0;
}
