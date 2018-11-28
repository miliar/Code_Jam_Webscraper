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

const int MaxN = 205, NA = -1;
const int64 MaxC = (1000 * 1000 * 1000LL) * (1000 * 1000 * 1000LL) * 4LL;

int p [MaxN], v [MaxN];
int d, n;

bool check (int64 e)
{
 int64 pos;
 int i;
 pos = -MaxC;
 for (i = 0; i < n; i++)
 {
  pos = max (pos, p[i] - e);
  pos += d * (v[i] - 1);
  if (pos - p[i] > e)
   return false;
  pos += d;
 }
 return true;
}

int main (void)
{
 int test, tests;
 int64 lo, me, hi;
 int i;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d %d", &n, &d);
  d *= 2;
  for (i = 0; i < n; i++)
  {
   scanf (" %d %d", &p[i], &v[i]);
   p[i] *= 2;
  }
  lo = 0;
  hi = MaxC;
  while (lo < hi)
  {
   me = (lo + hi) >> 1;
//   printf (INT64 " " INT64 " " INT64 "\n", lo, me, hi);
   if (check (me))
    hi = me;
   else
    lo = me + 1;
  }
  printf ("Case #%d: %.10lf\n", test, lo * 0.5);
 }
 return 0;
}
