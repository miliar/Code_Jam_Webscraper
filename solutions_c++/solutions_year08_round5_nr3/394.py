#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <numeric>
#include "MyLib.h"

using namespace std;

double eps = 1e-08;
long long Inf = 1 << 30;


//----------------------------------------

long long n, m;
int matr[200][200];
int table[2200][2200], dd[1000];
char s[1000];

int getans(int x, int q)
{
  int i, ans, d = (1 << n), best = 0, t, j;

  if (table[x][q] != -1)
    return table[x][q];


//  q = (q & dd[x]);

  for (i = 0; i < d; i++)
  {
    ans = 0;

    t = (1 << n) - 1;
    for (j = 0; j < n; j++)
    {
      if ((i & (1 << j)) != 0)
      if ((q & (1 << j)) != 0)
      if ((dd[x] & (1 << j)) != 0)
      {
        ans += matr[j][x];

        if ((t & (1 << j)) != 0)
          t -= (1 << j);

        if (j > 0)
        {
          if ((t & (1 << (j - 1))) != 0)
            t -= (1 << (j - 1));
        }

        if (j < n - 1)
        {
          if ((t & (1 << (j + 1))) != 0)
            t -= (1 << (j + 1));
        }
      }
//      cout << "ans = " << ans;
    }

    if (x < m - 1)
      ans += getans(x + 1, t);

    if (ans > best)
      best = ans;

//    cout << i << ' ' << ans << endl;
  }

  table[x][q] = best;
  return best;
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

    cin >> n >> m;
    gets(s);

    for (i = n - 1; i >= 0; i--)
    {
      gets(s);
      for (j = 0; j < m; j++)
        if (s[j] == '.')
          matr[i][j] = 1;
        else
          matr[i][j] = 0;
    }

    memset(table, 255, sizeof(table));

    for (int e = 0; e < m; e++)
    {
    tmp = (1 << n) - 1;
    for (i = 0; i < n; i++)
      if (matr[i][e] == 0)
        tmp -= (1 << i);

      dd[e] = tmp;
    }

//    cout << tmp << endl;
    cout << getans(0, dd[0]);

//   cout << endl;
//    for (i = 0; i < n; i++)
//      Print(matr[i], m);

    cout << endl;
  }

  return 0;
}