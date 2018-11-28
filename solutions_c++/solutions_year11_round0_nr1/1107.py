#include <algorithm>
#include <cassert>
#include <cstdio>

using namespace std;

const int MaxN = 10004;

char c [MaxN];
int a [MaxN];
int n;

int main (void)
{
 int test, tests;
 int i, ol, oh, bl, bh, d, t;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  ol = oh = bl = bh = 1;
  t = 0;
  for (i = 0; i < n; i++)
  {
   scanf (" %c %d", &c[i], &a[i]);
   if (c[i] == 'O')
   {
    if (a[i] < ol) d = ol - a[i];
    else if (oh < a[i]) d = a[i] - oh;
    else d = 0;
    ol = oh = a[i];
    d++;
    bl -= d;
    bh += d;
    t += d;
   }
   else
   {
    if (a[i] < bl) d = bl - a[i];
    else if (bh < a[i]) d = a[i] - bh;
    else d = 0;
    bl = bh = a[i];
    d++;
    ol -= d;
    oh += d;
    t += d;
   }
  }
  printf ("Case #%d: %d\n", test, t);
 }
 return 0;
}
