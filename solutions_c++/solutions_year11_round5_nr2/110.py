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

const int MaxN = 10004, MaxC = 0x3F3F3F3F, NA = -1;

int a [MaxN], b [MaxN], c [MaxN];
int n;

bool go (int v)
{
 int i, j;
 memmove (c, a, sizeof (c));
 memset (b, 0, sizeof (b));
// printf ("%d\n", v);
 for (i = 1; i < MaxN; i++)
 {
/*
  if (c[i] > 0 || b[i] > 0)
   printf ("%d: %d %d\n", i, c[i], b[i]);
*/
  while (c[i] > 0 && b[i] > 0)
  {
   c[i]--;
   b[i]--;
   b[i + 1]++;
  }
  while (c[i] > 0)
  {
   for (j = 0; j < v; j++)
    if (c[i + j] > 0)
     c[i + j]--;
    else
     return false;
   b[i + v]++;
  }
 }
 return true;
}

int main (void)
{
 int test, tests;
 int i, j, lo;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  memset (a, 0, sizeof (a));
  for (i = 0; i < n; i++)
  {
   scanf (" %d", &j);
   a[j]++;
  }
  for (lo = n; lo > 0; lo--)
   if (go (lo))
    break;
  printf ("Case #%d: %d\n", test, lo);
 }
 return 0;
}
