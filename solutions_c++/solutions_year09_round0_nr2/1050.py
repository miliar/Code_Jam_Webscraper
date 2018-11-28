#include <iostream>

using namespace std;

int map[101][101];
int flow[101][101];
char color[101][101];
int dirs[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int inv[4] = {3,2,1,0};
char curcolor;
int h, w;

void go (int i, int j)
{
  color[i][j] = curcolor;
  for (int k = 0; k < 4; k++)
  {
    int ni = i + dirs[k][0];
    int nj = j + dirs[k][1];
    if (ni < 0 || ni >= h || nj < 0 || nj >= w)
      continue;
    if (color[ni][nj] > 0)
      continue;
    if (flow[i][j] == k || flow[ni][nj] == inv[k])
    {
      go(ni,nj);
    }
  }
}

int main ()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);  
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": " << endl;
    cin >> h >> w;
    for (int i = 0; i < h; i++)
    {
      for (int j = 0; j < w; j++)
      {
        cin >> map[i][j];
      }
    }
    for (int i = 0; i < h; i++)
    {
      for (int j = 0; j < w; j++)
      {
        int bdir = -1;
        int mina;
        for (int k = 0; k < 4; k++)
        {
          int ni = i + dirs[k][0];
          int nj = j + dirs[k][1];
          if (ni < 0 || ni >= h || nj < 0 || nj >= w)
            continue;
          if (map[ni][nj] >= map[i][j])
            continue;
          if (bdir < 0 || map[ni][nj] < mina)
          {
            bdir = k;
            mina = map[ni][nj];
          }
        }
        flow[i][j] = bdir;
      }
    }
    memset(color,0,sizeof(color));
    curcolor = 'a';
    for (int i = 0; i < h; i++)
    {
      for (int j = 0; j < w; j++)
      {
        if (!color[i][j])
        {
          go(i,j);
          curcolor++;
        }
      }
    }
    for (int i = 0; i < h; i++)
    {
      for (int j = 0; j < w; j++)
      {
        cout << color[i][j] << ' ';
      }
      cout << endl;
    }
  }
  return 0;
}