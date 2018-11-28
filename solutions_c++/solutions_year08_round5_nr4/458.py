#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <numeric>
#include "MyLib.h"

using namespace std;

double eps = 1e-08;
long long Inf = 1 << 30;
int mod = 10007;


//----------------------------------------

long long n, m, r, h, w;
int bad[100][2];
int table[200][200];

long long getans(int x, int y)
{
  long long ans, i, q;

  if (table[x][y] != -1)
    return table[x][y];

  if (x == h && y == w)
    return 1;

  if (x > h || y > w)
    return 0;

  q = 0;
  for (i = 0; i < r; i++)
    if (bad[i][0] == x && bad[i][1] == y)
    {
      q = 1;
      break;
    }

  if (q == 1)
  {
    ans = 0;
  }
  else
  {
    ans = getans(x + 2, y + 1) + getans(x + 1, y + 2);
    ans %= mod;
  }

  table[x][y] = ans;
  return ans;
}

int main()
{
  long long i, j, t_count, test, tmp, ans;

  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);

  cin >> t_count;
  for (test = 0; test < t_count; test++)
  {
    cout << "Case #" << test + 1 << ": ";

    cin >> h >> w >> r;

    memset(table, 255, sizeof(table));

    for (i = 0; i < r; i++)
      cin >> bad[i][0] >> bad[i][1];

    cout << getans(1, 1);

    cout << endl;
  }

  return 0;
}