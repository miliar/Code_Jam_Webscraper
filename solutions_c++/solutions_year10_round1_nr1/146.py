#include <stdio.h>
#include <string.h>

const int maxn = 100;

char chs[] = "RB";

int fact[4][3] = {
  {1, 0, 0},                    // col
  {0, 1, 0},                    // row
  {1, 1, 0},                    // diag1
  {1, -1, 100},                 // diag2
};

const char *results[] = {
  "Neither", "Red", "Blue", "Both",
};

int tt, tc, i, j, n, m;
char a[maxn][maxn];
int cnts[3][6][maxn * 4];

int main ()
{
  scanf ("%d", &tc);
  for (int tt = 1; tt <= tc; tt++)
  {
    scanf ("%d%d", &n, &m);
    for (int i = 0; i < n; i++)
    {
      scanf ("%s", a[i]);
    }
    for (int i = 0; i < n; i++)
    {
      int k = n - 1;
      for (int j = n - 1; j >= 0; j--)
      {
        if (a[i][j] != '.')
        {
          if (j != k)
          {
            a[i][k] = a[i][j];
            a[i][j] = '.';
          }
          k--;
        }
      }
    }
    // for (int i = 0; i < n; i++)
    //   printf ("%s\n", a[i]);
    memset (cnts, 0, sizeof (cnts));
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < n; j++)
      {
        for (int k = 0; k < 2; k++)
        {
          for (int l = 0; l < 4; l++)
          {
            int idx = i * fact[l][0] + j * fact[l][1] + fact[l][2];
            if (a[i][j] == chs[k])
              cnts[k][l][idx]++;
            else
              cnts[k][l][idx] = 0;
            if (cnts[k][l][idx] >= m)
            {
              ans |= 1 << k;
            }
          }
        }
      }
    }
    printf ("Case #%d: %s\n", tt, results[ans]);
  }
  return 0;
}
