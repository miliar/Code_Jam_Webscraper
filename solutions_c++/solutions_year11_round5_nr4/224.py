#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const double eps = 1e-9;

int n;
long long ans, t;
char s[130];

void gen (long long num, int len)
{
  if (len == n)
  {
    t = (long long) (sqrt (num) + eps);
    if (t * t == num)
      ans = num;
    return;      
  }
  if (s[len] == '?')
  {
    gen (num * 2 + 1, len + 1);
    gen (num * 2, len + 1);
  }
  else
    gen (num * 2 + s[len] - '0', len + 1);
}


int main (void)
{
  int test, tests, i, j;
  freopen ("d.in", "rt", stdin);
  freopen ("d.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    ans = 0;
    scanf (" %s", s);
    n = strlen(s);
    gen (0, 0); 
    for (i = 0; i < n; i++)
      s[i] = (ans >> (n - i - 1) & 1) + '0';
    printf ("Case #%d: %s\n", test +1, s);
  }
  return 0;
}
