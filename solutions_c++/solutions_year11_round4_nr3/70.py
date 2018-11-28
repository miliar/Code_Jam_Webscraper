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

const int64 MaxN = 1000006;

bool s [MaxN];

int main (void)
{
 int test, tests;
 int64 i, j, n, res;
 memset (s, 1, sizeof (s));
 s[0] = s[1] = false;
 for (i = 2; i < MaxN; i++)
  if (s[i])
  {
   for (j = i * i; j < MaxN; j += i)
    s[j] = false;
  }
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" " INT64, &n);
  res = 0;
  if (n > 1)
  {
   res++;
   for (i = 2; i * i <= n; i++)
    if (s[(int) i])
     for (j = i * i; j <= n; j *= i)
      res++;
  }
  printf ("Case #%d: " INT64 "\n", test, res);
 }
 return 0;
}
