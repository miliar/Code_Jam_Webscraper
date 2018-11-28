#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
  if (argc < 2)
    return 1;
  ifstream in(argv[1]);
  int tt;
  in >> tt;
  for (int i = 0; i < tt; ++i)
  {
    long long l, t, n, c;
    in >> l >> t >> n >> c;
    long long a[n];
    for (int j = 0; j < c; ++j)
    {
      long long aa;
      in >> aa;
      for (int k = j; k < n; k += c)
        a[k] = aa;
    }
    long long s = 0, m = 0;
    for (; m < n && s < t; ++m)
    {
      if (s + 2 * a[m] > t)
      {
        long long d = t - s;
        a[m] -= d / 2;
        s = t;
        --m;
      } else
      {
        s += 2 * a[m];
      }
    }
    sort(a + m, a + n);
    for (; m < n; ++m)
    {
      s += a[m];
      if (m < n - l)
        s += a[m];
    }
    cout << "Case #" << 1 + i << ": " << s << "\n";
  }
  return 0;
}

