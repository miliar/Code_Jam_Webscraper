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

const int MaxN = 405, MaxL = MaxN * MaxN, MaxC = 0x3F3F3F3F, NA = -1;

int a [MaxN] [MaxN];
int c [MaxN];
int d [MaxN] [MaxN];
int p [MaxL], q [MaxL];
int f [MaxN] [MaxN];
int m, n, t;

int main (void)
{
 int test, tests;
 int cur, i, j, k, len, size, u, v, w;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d %d", &n, &m);
  memset (a, MaxC, sizeof (a));
  for (i = 0; i < n; i++)
   a[i][i] = 0;
  for (i = 0; i < m; i++)
  {
   scanf (" %d, %d", &j, &k);
//   fprintf (stderr, "%d,%d\n", j, k);
   a[k][j] = a[j][k] = 1;
  }
  for (k = 0; k < n; k++)
   for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
     a[i][j] = min (a[i][j], a[i][k] + a[k][j]);
  memset (c, 0, sizeof (c));
  for (i = 0; i < n; i++)
   for (j = 0; j < n; j++)
    if (a[i][j] == 1)
     c[i]++;
  memset (d, 0, sizeof (d));
  for (i = 0; i < n; i++)
   for (j = 0; j < n; j++)
    for (k = 0; k < n; k++)
     if (k != i && a[i][k] != 1 && a[j][k] == 1)
      d[i][j]++;
  len = a[0][1];
  t = 0;
  memset (f, -MaxC, sizeof (f));
  for (k = 1; k < len; k++)
   for (i = 0; i < n; i++)
    if (a[0][i] == (k - 1) && a[i][1] == len - (k - 1))
    {
//     fprintf (stderr, "i = %d\n", i);
     for (j = 0; j < n; j++)
      if (a[i][j] == 1 && a[0][j] == k && a[j][1] == len - k)
      {
//       fprintf (stderr, "add %d %d\n", i, j);
       p[t] = i;
       q[t] = j;
       t++;
       if (k == 1)
       {
        f[i][j] = c[i] + d[i][j];
//        fprintf (stderr, "f[%d][%d] = %d\n", i, j, f[i][j]);
       }
      }
    }
//  fprintf (stderr, "%d\n", t);
  size = 0;
  for (k = 0; k < t; k++)
  {
//   fprintf (stderr, "k = %d\n", k);
   u = p[k];
   v = q[k];
//   fprintf (stderr, "%d %d\n", u, v);
   for (w = 0; w < n; w++)
    if (a[v][w] == 1 && a[v][w] + a[w][1] == a[v][1])
    {
//     fprintf (stderr, "%d %d %d\n", u, v, w);
     if (w == 1)
      size = max (size, f[u][v]);
     else
     {
      cur = f[u][v];
      for (i = 0; i < n; i++)
       if (a[w][i] == 1 && a[u][i] != 1 && a[v][i] != 1)
        cur++;
      f[v][w] = max (f[v][w], cur);
//      fprintf (stderr, "f[%d][%d] = %d\n", v, w, f[v][w]);
     }
    }
  }
  if (len == 1)
   size = c[0];
  len--;
  printf ("Case #%d: %d %d\n", test, len, size - len);
  fflush (stdout);
 }
 return 0;
}
