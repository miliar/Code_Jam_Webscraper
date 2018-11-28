#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>

using namespace std;

const int MaxN = 1111;

int r[MaxN], x[MaxN], y[MaxN], p[MaxN];

int gt (int i, int j)
{
  return r[i] > r[j];
}

int main (void)
{
  int test, tests;
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int N, W, L, h, w, i;
    scanf ("%d %d %d", &N, &W, &L);
    for (i = 0 ;i < N; i++)
    {
      scanf ("%d", &r[i]); 
      p[i] = i;
    }


    sort (p, p + N, gt);

    x[p[0]] = y[p[0]] = 0;
    h = r[p[0]];
    for (i = 1; i < N; i++)
    {
      int tx = x[p[i-1]] + r[p[i]] + r[p[i-1]], ty = y[p[i-1]];
      if (tx <= W)
        x[p[i]] = tx, y[p[i]] = ty;
      else
      {
        x[p[i]] = 0, y[p[i]] = h + r[p[i]];
        if (y[p[i]] > L)
          break;
        h += 2*r[p[i]];
      }
    }

    /*plan B */
    if (i != N)
    {
//      printf ("Plan B!\n");
      w = r[p[0]];
      for (i = 1; i < N; i++)
      {
        int ty = y[p[i-1]] + r[p[i]] + r[p[i-1]], tx = x[p[i-1]];
        if (ty <= L)
          x[p[i]] = tx, y[p[i]] = ty;
        else
        {
          y[p[i]] = 0, x[p[i]] = w + r[p[i]];
          if (x[p[i]] > W)
            break;
          w += 2*r[p[i-1]];
        }
      }

    }
    assert (i == N);
    /*check*/

/*    for (i = 0; i < N; i++)
      for (int j = 0; j < N; j++) if (i != j)
        if (abs(x[i] - x[j]) < r[i] + r[j] &&
            abs(y[i] - y[j]) < r[i] + r[j])
           printf ("\n!!! %d (%d) and %d (%d) intersect !!!\n", i, p[i], j, p[j]);
*/    printf ("Case #%d: ", test + 1);
    for (i = 0 ;i < N; i++)
      printf ("%d %d%c", x[i], y[i], (i == N-1)?'\n':' ');
  }
  return 0;
}
