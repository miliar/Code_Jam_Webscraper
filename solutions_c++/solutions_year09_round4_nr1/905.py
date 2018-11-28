// vim:set ts=8 sw=2 et smarttab:

#include <cstdio>
#include <cassert>
#include <algorithm>

int n, mat[42];

void move(int dest, int src)
{
  assert(src >= dest);
  for (int i = src - 1; i >= dest; --i)
    std::swap(mat[i], mat[i + 1]);
}

int solve()
{
  int ret = 0;
  for (int i = 0; i < n; ++i)
  {
    for (int j = i; j < n; ++j)
      if (mat[j] < i + 1)
      {
        move(i, j);
        ret += j - i;
        break;
      }
  }
  return ret;
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc)
  {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
    {
      char line[42];
      scanf("%s", line);
      mat[i] = 0;
      for (int j = n - 1; j >= 0; --j)
        if (line[j] == '1')
        {
          mat[i] = j;
          break;
        }
    }
    int ans = solve();
    printf("Case #%d: %d\n", tc, ans);
  }
}
