#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

char b[123][123];

int main (void)
{
  int test, tests, i, j, n;
  long double wp[123], owp[123], oowp[123];
  int k[123];
  freopen ("a.in", "rt", stdin);
  freopen ("a.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    scanf ("%d", &n);
    for (i = 0 ; i < n; i++)
      for (j = 0; j < n; j++)
        scanf (" %c", &b[i][j]);
    for (i = 0 ; i < n; i++)
    {
      wp[i] = 0;
      k[i] = 0;
      for (j = 0; j < n; j++)
        wp[i] += (b[i][j] == '1'), 
        k[i] += (b[i][j] != '.');
      wp[i] = wp[i] / k[i];
    }

    for (i = 0; i < n; i++)
    {
      owp[i] = 0;
      
      for (j = 0; j < n; j++)
        if (b[i][j] != '.')
          owp[i] += (wp[j] * k[j] - (b[j][i] - '0'))/(k[j] - 1);
      owp[i] = owp[i] / k[i];          
    }

    for (i = 0 ; i < n; i++)
    {
      oowp[i] = 0;
      
      for (j = 0; j < n; j++)
        if (b[i][j] != '.')
          oowp[i] += owp[j];
      oowp[i] = oowp[i] / k[i];          
    }

   

    printf ("Case #%d:\n", test + 1);
    for (i = 0 ;i < n; i++)
      printf ("%.12lf\n", (double) (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]));
//    for (i = 0 ;i < n; i++)
//      printf ("%lf %lf %lf\n", (double)wp[i], (double)owp[i], (double)oowp[i]);
  }
  return 0;
}
