#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>

using namespace std;

double solve(int mask, vector<int> const& x,
             vector<int> const& y, vector<int> const& r)
{
  int n = x.size();

  double x0 = 0, y0 = 0;
  int maskBits = 0;
  for (int i = 0; i < n; ++i)
    if (mask & (1 << i))
    {
      x0 += x[i];
      y0 += y[i];
      ++maskBits;
    }

  double res1 = -1;
  double res2 = -1;

  if (maskBits)
  {
    x0 /= maskBits;
    y0 /= maskBits;

    double radius = 0;
    for (int i = 0; i < n; ++i)
      if (mask & (1 << i))
      {
        double cur = sqrt(pow(x0 - x[i], 2.0) + pow(y0 - y[i], 2.0)) +
                             r[i];
        if (radius == -1 || radius < cur)
          radius = cur;
      }

    res1 = radius;
  }

  for (int i = 0; i < n; ++i)
    if (mask & (1 << i))
      for (int j = 0; j < n; ++j)
        if (i != j && (mask & (1 << j)))
        {
          double radius = sqrt(pow(x[i] - x[j], 2.0) + pow(y[i] - y[j], 2.0));
          radius += r[i] + r[j];
          if (res2 == -1 || res2 < radius / 2)
             res2 = radius / 2;
        }

  if (res1 == -1)
    res1 = 1e9;
  if (res2 == -1)
    res2 = 1e9;
  return min(res1, res2);
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int tests;
  cin >> tests;
  for (int t = 0; t < tests; ++t)
  {
    int n;
    cin >> n;
    
    vector<int> x(n), y(n), r(n);
    for (int i = 0; i < n; ++i)
      cin >> x[i] >> y[i] >> r[i];

    double res = 1e9;
    for (int i = 0; i < (1 << n); ++i)
    {
      res = min(res, max(solve(i, x, y, r), solve(~i, x, y, r)));
    }

    cout << "Case #" << t + 1 << ": " << fixed << setprecision(6) << res << "\n";
  }
  return 0;
}
