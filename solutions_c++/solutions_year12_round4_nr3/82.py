#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef long double real;

#ifdef WIN32
#define INT64 "%I64d"
#define UINT64 "%I64u"
#else
#define INT64 "%lld"
#define UINT64 "%llu"
#endif

#ifdef DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif

const int MaxN = 100005, MaxC = 0x3F3F3F3F, NA = -1;

int x [MaxN];
int y [MaxN];
int n;

bool solve (int lo, int hi, int slope)
{
 eprintf ("%d %d %d %d\n", lo, hi, x[lo], slope);
 if (lo >= hi)
  return true;

 y[lo] = y[hi] - slope * (hi - lo);
 if (x[lo] <= lo || x[lo] > hi)
  return false;
 y[x[lo]] = y[hi] - slope * (hi - x[lo]);
 return solve (lo + 1, x[lo], slope + 1) &&
        solve (x[lo], hi, slope);
}

int main (void)
{
 int test, tests;
 int i;
 bool ok;

 scanf (" %d ", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  for (i = 1; i <= n - 1; i++)
   scanf (" %d", &x[i]);
  y[n] = 1 << 25;
  ok = solve (1, n, 0);
  printf ("Case #%d:", test);
  if (ok)
   for (i = 1; i <= n; i++)
    printf (" %d", y[i]);
  else
   printf (" Impossible");
  printf ("\n");
 }

 return 0;
}
