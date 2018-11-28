#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <cstdlib>

using namespace std;

#define pb push_back
#define all(x) x.begin(), x.end()
#define mp make_pair

const int inf = (1 << 30) - 1;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef long long int64;
typedef set < int > si;

void calc (int64 ii)
{
      int64 n, m, a;
      cin >> n >> m >> a;
      int64 y2;
      for (int64 x1 = 1; x1 <= n; x1 ++)
        for (int64 y1 = 0; y1 <= m; y1 ++)
          for (int64 x2 = x1; x2 <= n; x2 ++)
            {
              if ((a + x2 * y1) % x1 == 0)
                {
                  y2 = (a + x2 * y1) / x1;
                  if ((y2 <= m) && (y2 >= 0))
                    {
                      printf ("Case #%d: %d %d %d %d 0 0\n", (int) ii, (int) x1, (int)y1, (int)x2, (int)y2);
                      return;
                    }
                }
              if ((-a + x2 * y1) % x1 == 0)
                {
                  y2 = (-a + x2 * y1) / x1;
                  if ((y2 <= m) && (y2 >= 0))
                    {
                      printf ("Case #%d: %d %d %d %d 0 0\n", (int) ii, (int) x1, (int)y1, (int)x2, (int)y2);
                      return;
                    }
                }
            }
  printf ("Case #%d: IMPOSSIBLE\n", ii);
}

int main ()
{
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
  int nn, ii;
  scanf ("%d", &nn);
  for (ii = 1; ii <= nn; ii ++)
    { 
      calc (ii);
    }
}
