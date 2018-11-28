#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

const int MaxN = 102, MaxD = 4, MaxC = 0x3F3F3F3F;
const int dx [MaxD] = {-1,  0,  0,  1},
          dy [MaxD] = { 0, -1,  1,  0};

int a [MaxN] [MaxN];
char b [MaxN] [MaxN];
int h, w;
char c0;

char recur (int x, int y)
{
 if (b[x][y] != '#')
  return b[x][y];

 int d, m;
 m = MaxC;
 for (d = 0; d < MaxD; d++)
  if (m > a[x + dx[d]][y + dy[d]])
   m = a[x + dx[d]][y + dy[d]];
 if (m >= a[x][y])
 {
  b[x][y] = c0;
  return b[x][y];
 }

 char c;
 for (d = 0; d < MaxD; d++)
  if (m == a[x + dx[d]][y + dy[d]])
   break;
 assert (d < MaxD);
 c = recur (x + dx[d], y + dy[d]);
 b[x][y] = c;
 return c;
}

int main (void)
{
 int test, tests;
 int i, j;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d %d", &h, &w);
  memset (a, MaxC, sizeof (a));
  memset (b, '#', sizeof (b));
  for (i = 1; i <= h; i++)
   for (j = 1; j <= w; j++)
    scanf (" %d", &a[i][j]);
  c0 = 'a';
  for (i = 1; i <= h; i++)
   for (j = 1; j <= w; j++)
    if (b[i][j] == '#')
     if (recur (i, j) == c0)
      c0++;
  printf ("Case #%d:\n", test);
  for (i = 1; i <= h; i++)
   for (j = 1; j <= w; j++)
    printf ("%c%c", b[i][j], j < w ? ' ' : '\n');
 }
 return 0;
}
