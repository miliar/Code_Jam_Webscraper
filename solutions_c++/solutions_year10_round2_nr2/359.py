#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

int C;

int n, k, b, t;

int x[110];
int v[110];

int y[110];

int main()
{
  scanf("%d", &C);
  for (int c = 0; c < C; ++c)
  {
    scanf("%d %d %d %d", &n, &k, &b, &t);
    for (int i = 0; i < n; ++i)
      scanf("%d", &x[i]);
    for (int i = 0; i < n; ++i)
      scanf("%d", &v[i]);
    for (int i = 0; i < n; ++i)
    {
      y[i] = (b - x[i]) / v[i] + (((b - x[i]) % v[i]) != 0);
    }
    int r = 0;
    int res = 0;
    int s = 0;
    for (int i = n-1; i >= 0 && r < k; --i)
    {
      if (y[i] <= t)
      {
        ++r;
        res += s;
      }
      else
        ++s;
    }
    if (r < k)
    {
      printf("Case #%d: IMPOSSIBLE\n", c+1);
    }
    else
      printf("Case #%d: %d\n", c+1, res);
  }
  return 0;
}