#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <numeric>
#include "MyLib.h"

using namespace std;

int v[100010], c[100010], leaf[100010];
int n;
int table[100010][2];

int getans(int x, int b)
{
  int ans;
  int a1, a2;

  if (table[x][b] != -1)
    return table[x][b];

  if (x >= (n + 1) / 2)
    if (leaf[x] == b)
      return 0;
    else
      return 1000000;

/*  if (v[i] == 1)
  {
    a1 = getans(2 * x, 1);
    a2 = getans(2 * x + 1, 1);

    if (b == 0)
    {
      if (c[i] == 0)
      {  
        if (getans(2 * x, 1) == -2 || getans(2 * x + 1, 1) == -2)
          ans = -2;
        else
          ans = getans(2 * x, 1) + getans(2 * x + 1, 1);
      }
      else
      {
        if (a1 == -2 && a2 == -2)
          ans = -2;
        else 
        if (a1 == -2)
          ans = a2 + 1;
      }
    }
  }*/

  if (b == 1)
  {
    a1 = getans(2 * x, 1);
    a2 = getans(2 * x + 1, 1);

    if (v[x] == 0)
    {
      ans = min(a1, a2);
    }
    else
    {
      ans = a1 + a2;
      if (c[x] == 1 && 1 + min(a1, a2) < ans)
        ans = 1 + min(a1, a2);
    }    
  }
  else
  {
    a1 = getans(2 * x, 0);
    a2 = getans(2 * x + 1, 0);

    if (v[x] == 1)
    {
      ans = min(a1, a2);
    }
    else
    {
      ans = a1 + a2;
      if (c[x] == 1 && 1 + min(a1, a2) < ans)
        ans = 1 + min(a1, a2);
    }    
  }

  table[x][b] = ans;
  return ans;
}

int main()
{
  long long i, j, ans, t_count, test, tmp, w;

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> t_count;
  for (test = 0; test < t_count; test++)
  {
    cout << "Case #" << test + 1 << ": ";

    cin >> n >> w;

    for (i = 1; i <= n / 2; i++)
      cin >> v[i] >> c[i];

    for (i = (n + 1) / 2; i <= n; i++)
      cin >> leaf[i];

    memset(table, -1, sizeof(table));
    
    ans = getans(1,w);
    if (ans >= 500000)
      cout << "IMPOSSIBLE";
    else
      cout << getans(1, w);

    cout << endl;
  }

  return 0;
}