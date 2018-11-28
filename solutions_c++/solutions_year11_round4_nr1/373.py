#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int b[1234], e[1234], w[1234], s[123];

int main (void)
{
  int test, tests, i, n;
  double res, dt, ti, sr;
  int X, S, R, t;
  freopen ("a.in", "rt", stdin);
  freopen ("a.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    res = 0;
    memset (s, 0, sizeof (s));
    scanf ("%d %d %d %d %d", &X, &S, &R, &t, &n);
    dt = t;
    b[0] = e[0] = 0;
    for (i = 1; i <= n; i++)
    {
      scanf (" %d %d %d", &b[i], &e[i], &w[i]);
      s[0] += b[i] - e[i-1];
      s[w[i]] += e[i] - b[i];
    }
    s[0] += X - e[n];
    for (i = 0; i < 123; i++)
    {
      sr = min (s[i] * 1.0, (i + R) * dt);
      dt -= sr / (i + R);
      ti = sr / (i + R) + (s[i] - sr) / (i + S); 
      res += ti;
    }

    printf ("Case #%d: %.9lf\n", test + 1, res);
  }
  return 0;
}
