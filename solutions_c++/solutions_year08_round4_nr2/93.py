#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <numeric>
#include "MyLib.h"

using namespace std;

int main()
{
  long long i, j, ans, t_count, test, n, m, a, tmp, q, x1, y1, x2, y2;

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> t_count;
  for (test = 0; test < t_count; test++)
  {
    cout << "Case #" << test + 1 << ": ";

    cin >> n >> m >> a;

    q = 0;
    for (x1 = 0; x1 <= n; x1++)
      for (y1 = 0; y1 <= m; y1++)
        for (x2 = x1 + 1; x2 <= n; x2++)
          for (y2 = 0; y2 <= m; y2++)
          {
            if (q == 0)
            {
              if (abs(x2 * y1 - x1 * y2) == a)
              {
                cout << 0 << ' ' << 0 << ' ' << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2;
                q = 1;
              }
            }
          }

    if (q == 0)
      cout << "IMPOSSIBLE";

    cout << endl;
  }

  return 0;
}