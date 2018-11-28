#include <algorithm>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <set>
#include <map>
#include <iostream>

using namespace std;

int main( void )
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;
  cin >> tn;
  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);

    int n, m, A;
    cin >> n >> m >> A;
    bool ok = false;

    for (int a = 0; a <= n; a++)
      for (int b = 0; b <= m; b++)
        for (int c = 0; c <= n && !ok; c++)
          if (c == 0 || (a * b - A) % c == 0)
          {
            int d = 0;
            if (c)
              d = (a * b - A) / c;
            else if (a * b != A)
              continue;
            if (d >= 0 && d <= m)
            {
//              assert(a * b - c * d);
              printf("0 0 %d %d %d %d\n", a, d, c, b);
              ok = true;
            }
          }

    if (!ok)
      printf("IMPOSSIBLE\n");

  }



  return 0;
}