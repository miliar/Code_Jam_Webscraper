#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int MaxN = 222, MaxV = 1234567;

int main (void)
{
  int test, tests, i, j, k;
  long long res;
  int c, d, p[MaxN], qv;
  long long l, r;
  long long v[MaxV], tv[MaxV];
//  freopen ("b.in", "rt", stdin);
  freopen ("b.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    qv = 1;
    v[0] = tv[0] = - 1e15;
    scanf ("%d %d", &c, &d);
    d *= 2;
    for (i = 0 ; i < c; i++)
    {
      scanf (" %d %d", &p[i], &k);
      for (j = 0; j < k; j++)
        v[qv++] = p[i] * 2;
    }
    l = 0; r = 1e13;
    while (l < r)
    {
      res = (l + r)/2;

      for (i = 1; i < qv; i++)
      {
        if (v[i] - res >= tv[i - 1] + d)
          tv[i] = v[i] - res;
        else if (abs(v[i] - (tv[i - 1] + d)) <= res)
          tv[i] = tv[i - 1] + d;
        else
          break;
      }

      if (i == qv)
        r = res;
      else
        l = res + 1;
    }
    printf ("Case #%d: %.2lf\n", test + 1, l * 0.5);
//    for (i = 0; i < qv; i++)
//      cout << tv[i] << ' ';
//    cout << endl;
  }
  return 0;
}
