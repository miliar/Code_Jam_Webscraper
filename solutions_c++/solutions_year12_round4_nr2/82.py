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
typedef double real;

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

/* START RNG */
const unsigned LCG_MULT = 1664525, LCG_ADD = 1013904223;
const real RANDMULT = 1.0 / 65536.0 / 65536.0;
unsigned currand;
inline void initrand (int seed) {currand = seed;}
inline void nextrand (void) {currand = currand * LCG_MULT + LCG_ADD;}
inline real rndvalue (void) {nextrand (); return currand * RANDMULT;}
inline int rndvalue (int range) {return rndvalue () * range;}
/* END RNG */

const int MaxN = 100005, MaxC = 0x3F3F3F3F, NA = -1;

int64 r [MaxN];
int64 x [MaxN], y [MaxN];
int64 w, l;
int n;

int main (void)
{
 int test, tests;
 int i, j;

 initrand (12131433);
 scanf (" %d ", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d " INT64 " " INT64, &n, &w, &l);
  for (i = 0; i < n; i++)
   scanf (" " INT64, &r[i]);
  for (i = 0; i < n; i++)
  {
   do
   {
    x[i] = rndvalue (w + 1);
    y[i] = rndvalue (l + 1);
    for (j = 0; j < i; j++)
     if ((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]) <
         (r[i] + r[j]) * (r[i] + r[j]))
      break;
   }
   while (j < i);
  }
  printf ("Case #%d:", test);
  for (i = 0; i < n; i++)
   printf (" " INT64 " " INT64, x[i], y[i]);
  printf ("\n");
 }

 return 0;
}
