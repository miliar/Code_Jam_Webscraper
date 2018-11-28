// vim:set ts=8 sw=2 et smarttab:

#include <cstdio>

int n, c;

double solve();
double combi(int n, int k);

int main()
{
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc)
  {
    scanf("%d%d", &n, &c);
    double ans = solve();
    printf("Case #%d: %.7lf\n", tc, ans);
  }
}

double solve()
{
  double table[41];
  table[n] = 0.0;
  for (int i = n - 1; i >= 0; --i)
  {
    double a = 0;
    for (int j = 0; j < c; ++j)
    {
      if (j > i || c - j > n - i)
        continue;
      a += table[i + c - j] * combi(i, j) * combi(n - i, c - j) / combi(n, c);
    }
    double p = combi(i, c) / combi(n, c);
    table[i] = 1.0;
    double pp = 1;
    while (true)
    {
      table[i] += pp * a;
      if (pp < 1.0e-9)
        break;
      pp *= p;
      table[i] += 1.0 * pp;
    }
  }
  return table[0];
}

double combi(int n, int k)
{
  static double table[41][41];
  if (k < 0 || k > n)
    return 0.0;
  if (k == 0 || k == n)
    return 1.0;
  if (table[n][k] != 0.0)
    return table[n][k];
  return table[n][k] = combi(n - 1, k - 1) + combi(n - 1, k);
}
