// vim:set ts=8 sw=2 et:

#include <cstdio>
#include <climits>
#include <cassert>
#include <algorithm>
#include <utility>

const int maxn = 100, maxm = 100;
int n, m;
int map[maxn][maxm];
int table[maxn][maxm];
char ans[maxn][maxm];
char convert[26];

void solve();

int main()
{
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc)
  {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
        scanf("%d", &map[i][j]);
    solve();
    printf("Case #%d:\n", tc);
    for (int i = 0; i < n; ++i)
    {
      for (int j = 0; j < m; ++j)
      {
        if (j > 0)
          printf(" ");
        printf("%c", ans[i][j]);
      }
      printf("\n");
    }
  }
}

void solve()
{
  typedef std::pair<int, int> pi;
  typedef std::pair<int, pi> ppi;
  static ppi array[maxn * maxm];
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      array[m * i + j] = ppi(map[i][j], pi(i, j));
  std::sort(array, array + n * m);
  std::fill(table[0], table[n], -1);
  int v = 0;
  for (int k = 0; k < n * m; ++k)
  {
    int i = array[k].second.first;
    int j = array[k].second.second;
    const int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
    int min, mini, minj;
    min = INT_MAX;
    for (int d = 0; d < 4; ++d)
    {
      int ni = i + dir[d][0];
      int nj = j + dir[d][1];
      if (ni < 0 || ni >= n || nj < 0 || nj >= m)
        continue;
      if (map[ni][nj] < min)
        min = map[ni][nj], mini = ni, minj = nj;
    }
    if (min < map[i][j])
    {
      assert(table[mini][minj] != -1);
      table[i][j] = table[mini][minj];
    }
    else
      table[i][j] = v++;
  }
  std::fill(convert, convert + v, '\0');
  char c = 'a';
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      if (convert[table[i][j]] == '\0')
      {
        convert[table[i][j]] = c;
        ans[i][j] = c;
        ++c;
      }
      else
        ans[i][j] = convert[table[i][j]];
}
