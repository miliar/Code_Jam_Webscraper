#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif

typedef long long int64;
typedef double real;

const int MaxN = 102, MaxC = 0x3F3F3F3F, NA = -1;

int a [MaxN] [MaxN];
int b [MaxN] [MaxN];
real wp [MaxN], wq [MaxN];
real owp [MaxN], owq [MaxN];
real oowp [MaxN], oowq [MaxN];
int n;

int main (void)
{
 int test, tests;
 int i, j;
 char ch;

 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  memset (a, 0, sizeof (a));
  memset (b, 0, sizeof (b));
  for (i = 0; i < n; i++)
   for (j = 0; j < n; j++)
   {
    scanf (" %c", &ch);
    if (ch == '0' || ch == '1')
    {
     a[i][j] = ch - '0';
     b[i][j] = 1;
    }
   }

  for (i = 0; i < n; i++)
  {
   wp[i] = wq[i] = 0;
   for (j = 0; j < n; j++)
    if (b[i][j])
    {
     wp[i] += a[i][j];
     wq[i] += b[i][j];
    }
   assert (wq[i] != 0);
   wp[i] /= wq[i];
  }

  for (i = 0; i < n; i++)
  {
   owp[i] = owq[i] = 0;
   for (j = 0; j < n; j++)
    if (b[i][j])
    {
     owp[i] += ((wp[j] * wq[j]) - a[j][i]) / (wq[j] - 1);
     owq[i] += b[i][j];
    }
   assert (owq[i] != 0);
   owp[i] /= owq[i];
  }
  
  for (i = 0; i < n; i++)
  {
   oowp[i] = oowq[i] = 0;
   for (j = 0; j < n; j++)
    if (b[i][j])
    {
     oowp[i] += owp[j];
     oowq[i] += b[i][j];
    }
   assert (oowq[i] != 0);
   oowp[i] /= oowq[i];
  }
  
  printf ("Case #%d:\n", test);
  for (i = 0; i < n; i++)
   printf ("%.16lf\n",
    (double) (wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25));
 }

 return 0;
}
