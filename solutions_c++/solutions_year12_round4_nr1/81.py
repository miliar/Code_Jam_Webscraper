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

int d [MaxN], l [MaxN], g [MaxN];
int D, n;

int main (void)
{
 int test, tests;
 int i, j, x;
 bool ok;

 scanf (" %d ", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  for (i = 0; i < n; i++)
   scanf (" %d %d", &d[i], &l[i]);
  scanf (" %d", &D);
  x = 0;
  memset (g, NA, sizeof (g));
  g[0] = d[0];
  ok = false;
  for (i = 0; i < n && !ok; i++)
  {
   if (g[i] == NA)
    break;
   x = d[i] + g[i];
   if (x >= D)
    ok = true;
   for (j = i + 1; j < n && !ok; j++)
   {
    if (x < d[j])
     break;
    g[j] = max (g[j], min (l[j], d[j] - d[i]));
   }
  }
  printf ("Case #%d: %s\n", test, ok ? "YES" : "NO");
 }

 return 0;
}
