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

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef long long int64;
typedef set < int > si;

const int inf = (1 << 30) - 1;
const int p = 10007;

bool a[101][101];
int t[101][101];
int w, h, q, x, y;

int main ()
{
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
  int nn;
  cin >> nn;
  for (int ii = 1; ii <= nn; ii ++)
    {
      memset (a, 0, sizeof (a));
      cin >> w >> h >> q;
      for (int i = 0; i < q; i ++)
        {
          cin >> x >> y;
          a[x][y] = 1;
        }
      memset (t, 0, sizeof (t));
      t[1][1] = 1;
      if (a[1][1])
        t[1][1] = 0;
      for (int i = 1; i <= w; i ++)
        for (int j = 1; j <= h; j ++)
          if (i + j > 2)
            {
              if (a[i][j])
                t[i][j] = 0;
               else
                {
                  t[i][j] = 0;
                  if (i > 2 && j > 1)
                    t[i][j] += t[i-2][j-1];
                  if (i > 1 && j > 2)
                    t[i][j] += t[i-1][j-2];
                  t[i][j] = t[i][j] % p;
                }
            }
      printf ("Case #%d: %d\n", ii, t[w][h]);
    }
}
