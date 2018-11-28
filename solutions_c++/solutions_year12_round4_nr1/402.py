#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 11111;

int d[MaxN], l[MaxN], dp[MaxN];

int main (void)
{
  int test, tests;
  char res[2][10] = {"NO", "YES"};
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int N, i, j, D, nres; 
    memset (dp, -1, sizeof (dp));
    dp[1] = 0;
    scanf ("%d", &N);
    for (i = 1 ;i <= N; i++)
      scanf ("%d %d", &d[i], &l[i]);
    scanf ("%d", &D);
    d[0] = 0;
    d[N+1] = D;
    for (i = 2; i <= N + 1; i++)
    {
      for (j = 1; j < i; j++)
      {
//        printf ("i=%d j=%d dp[j]=%d d[i]=%d d[j]=%d l[j]=%d\n", i, j, dp[j], d[i], d[j], l[j]);
        if (dp[j] != -1)
          if (d[i] - d[j] <= l[j])
            if (d[i] - d[j] <= d[j] - d[dp[j]])
            {
              dp[i] = j;
              break;
            }
      }
    }
    if (dp[N+1] == -1)
      nres = 0;
    else
      nres = 1;
//    for (i = 0; i <= N+1; i++)
//      printf ("%d ", dp[i]);

    printf ("Case #%d: %s\n", test + 1, res[nres]);
  }
  return 0;
}
