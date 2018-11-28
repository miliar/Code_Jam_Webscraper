#include <cstdio>
#include <cstring>
#include <vector>

const int maxr = 110;

int dy[4] = {-1, 0, 0, 1};
int dx[4] = {0, -1, 1, 0};
int testN, h, w;
int a[maxr][maxr];
int sink[maxr][maxr], c[maxr][maxr];
std::vector <int> go[maxr][maxr];

bool ok( int y, int x )
{
  return 0 <= y && y < h && 0 <= x && x < w;
}

void dfs( int i, int j, int color )
{
  c[i][j] = color;
  for (int k = 0; k < (int)go[i][j].size(); k++)
  {
    int ii = i + dy[go[i][j][k]];
    int jj = j + dx[go[i][j][k]];
    if (c[ii][jj] == 0)
      dfs(ii, jj, color);
  }
}

int main()
{
  scanf("%d", &testN);
  for (int test = 1; test <= testN; test++)
  {
    scanf("%d%d", &h, &w);
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
        scanf("%d", &a[i][j]);
    memset(sink, -1, sizeof(sink));
    int t = 'a';
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
      {
        int g = -1;
        for (int dd = 0; dd < 4; dd++)
        {
          if (!ok(i + dy[dd], j + dx[dd]) || a[i][j] <= a[i + dy[dd]][j + dx[dd]])
            continue;
          if (g == -1 || a[i + dy[g]][j + dx[g]] > a[i + dy[dd]][j + dx[dd]])
            g = dd;
        }
        if (g == -1)
          sink[i][j] = t++;
        else
          go[i + dy[g]][j + dx[g]].push_back(g ^ 3);
      }
    memset(c, 0, sizeof(c));
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
        if (sink[i][j] != -1)
        {
//          fprintf(stderr, "go(%d,%d)\n", i, j);
          dfs(i, j, sink[i][j]);
        }
    static int col[26];
    memset(col, -1, sizeof(col));
    int kk = 'a';
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
        if (col[c[i][j] - 'a'] == -1)
          col[c[i][j] - 'a'] = kk++;
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
        go[i][j].clear();
    printf("Case #%d:\n", test);
    for (int i = 0; i < h; i++)
      for (int j = 0; j < w; j++)
        printf("%c%c", col[c[i][j] - 'a'], "\n "[j < w - 1]);
  }
  return 0;
}

