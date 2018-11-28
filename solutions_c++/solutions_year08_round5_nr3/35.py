#include <cstdio>
#include <vector>

using namespace std;

#define maxn 100

int id( int x, int y )
{
  return x * maxn + y;
}

char a[maxn][maxn];

vector <int> ne[maxn * maxn];
int px[maxn * maxn], py[maxn * maxn], wasx[maxn * maxn], wasy[maxn * maxn];
int dx[] = {1, 1, -1, -1, -1, 1},
    dy[] = {0, 1, 1, 0, -1, -1};

int dfs( int v )
{
  wasx[v] = 1;
  for (int i = 0; i < ne[v].size(); i++)
  {
    if (py[ne[v][i]] != v)
    {
      wasy[ne[v][i]] = 1;
    }
    if (py[ne[v][i]] == -1 || !wasx[py[ne[v][i]]] && dfs(py[ne[v][i]]))
    {
      py[ne[v][i]] = v;
      px[v] = ne[v][i];
      return 1;
    }
  }
  return 0;
}

int main( void )
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);
    int w, h;
    scanf("%d%d", &h, &w);
    for (int i = 0; i < h; i++)
      scanf("%s", a[i]);
    memset(px, -1, sizeof(px));
    memset(py, -1, sizeof(px));
    for (int i = 0; i < maxn * maxn; i++)
      ne[i].clear();
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
        if ((j & 1) && a[i][j] == '.')
        {
          for (int t = 0; t < 6; t++)
            if (i + dy[t] >= 0 && i + dy[t] < h && j + dx[t] >= 0 && j + dx[t] < w && 
                a[i + dy[t]][j + dx[t]] == '.')
              ne[id(i, j)].push_back(id(i + dy[t], j + dx[t]));
        }
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
        if ((j & 1) && a[i][j] == '.')
        {
          memset(wasx, 0, sizeof(wasx));
          memset(wasy, 0, sizeof(wasy));
          dfs(id(i, j));
        }
    memset(wasx, 0, sizeof(wasx));
    memset(wasy, 0, sizeof(wasy));
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
        if ((j & 1) && a[i][j] == '.' && !wasx[id(i, j)] && px[id(i, j)] == -1)
          dfs(id(i, j));
    int res = 0;
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
        if (a[i][j] == '.')
        {
          if ((j & 1))
            res += wasx[id(i, j)];
          else
            res += !wasy[id(i, j)];
        }
    printf("%d\n", res);


  }

  return 0;
}