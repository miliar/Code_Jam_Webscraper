#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define sqr(o) ((o)*(o))

using namespace std;

const int MinN = 157, MedN = MinN << 1, MaxN = MedN << 1,
 MaxC = 0x3F3F3F3F, NA = -1;

int a [MaxN] [MaxN];
int n;

inline bool equal (int a, int b)
{
 return a == NA || b == NA || a == b;
}

inline bool check (int x, int y)
{
// printf ("%d %d\n", x, y);
 int i, j;
 for (i = 0; i <= MinN; i++)
  for (j = 0; j <= MinN; j++)
   if (!equal (a[MedN + x + i][MedN + y + j], a[MedN + x - i][MedN + y + j]) ||
       !equal (a[MedN + x + i][MedN + y + j], a[MedN + x + i][MedN + y - j]) ||
       !equal (a[MedN + x + i][MedN + y + j], a[MedN + x - i][MedN + y - j]) ||
       !equal (a[MedN + x - i][MedN + y + j], a[MedN + x + i][MedN + y - j]) ||
       !equal (a[MedN + x - i][MedN + y + j], a[MedN + x - i][MedN + y - j]) ||
       !equal (a[MedN + x + i][MedN + y - j], a[MedN + x - i][MedN + y - j]))
    return false;
// printf ("OK\n");
 return true;
}

int main (void)
{
 int test, tests;
 int i, j, res;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  memset (a, NA, sizeof (a));
  scanf (" %d", &n);
  for (i = 2; i <= n + n; i++)
   for (j = max (1, i - n); j <= min (i - 1, n); j++)
//    printf ("%d %d\n", i - 1 - n, j + j - i),
    scanf (" %d", &a[MedN + i - 1 - n][MedN + j + j - i]);
  res = MaxC;
  for (i = -(n + n); i <= +(n + n) && res > 0; i++)
   for (j = -(n + n); j <= +(n + n) && res > 0; j++)
    if (abs (i) + abs (j) <= (n + n))
     if (res > sqr (abs (i) + abs (j) + n) - sqr (n))
      if (check (i, j))
       res = sqr (abs (i) + abs (j) + n) - sqr (n);
  printf ("Case #%d: %d\n", test, res);
  fflush (stdout);
 }
 return 0;
}
