#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

const int INF = 100000000;

const int TABLE_I[] = {-1, 0, 0, 1};
const int TABLE_J[] = {0, -1, 1, 0};
const int MAXW = 100;
const int MAXH = MAXW;

bool mark[MAXW][MAXH];
char color[MAXW][MAXH];

char c;
pair<int, int> t[MAXW][MAXH];
vector< pair<int, int> > tab[MAXW][MAXH];

void paint(int i, int j)
{
   mark[i][j] = true;
   color[i][j] = c;
   for (int r = 0; r < tab[i][j].size(); r++)
   {
      if (!mark[tab[i][j][r].first][tab[i][j][r].second])
      {
         paint(tab[i][j][r].first, tab[i][j][r].second);
      }
   }
}

int main()
{
   freopen("watersheds.in", "r", stdin);
   freopen("watersheds.out", "w", stdout);
   int n;
   scanf("%d", &n);
   for (int z = 0; z < n; z++)
   {
   c = 'a';
   printf("Case #%d:\n", z + 1);
   int w,h;
   scanf("%d%d", &w, &h);
   int a[w][h], f[w][h];
   for (int i = 0; i < w; i++)
   {
      for (int j = 0; j < h; j++)
      {
         tab[i][j].clear();
         scanf("%d", &a[i][j]);
         f[i][j] = a[i][j];
         t[i][j] = pair<int, int>(i, j);
         mark[i][j] = false;
      }
   }
   for (int i = 0; i < w; i++)
   {
      for (int j = 0; j < h; j++)
      {
         for (int q = 0; q < 4; q++)
         {
            int x = i + TABLE_I[q], y = j + TABLE_J[q];
            if (x >= 0 && y >= 0 && x < w && y < h)
            {
               if (a[x][y] < f[i][j])
               {
                  f[i][j] = a[x][y];
                  t[i][j] = pair<int, int>(x, y);
               }
            }
         }
      }
   }
   for (int i = 0; i < w; i++)
   {
      for (int j = 0; j < h; j++)
      {
         tab[t[i][j].first][t[i][j].second].push_back(pair<int, int>(i, j));
         tab[i][j].push_back(t[i][j]);
      }
   }
   for (int i = 0; i < w; i++)
   {
      for (int j = 0; j < h; j++)
      {
         if (!mark[i][j])
         {
            paint(i, j);
            c++;
         }
      }
   }
   for (int i = 0; i < w; i++)
   {
      for (int j = 0; j < h; j++)
      {
         if (j != h - 1)
         {
            printf("%c ", color[i][j]);
         }
         else
         {
            printf("%c", color[i][j]);
         }
      }

      printf("\n");
   }
   }

   return 0;
}
