#include <stdio.h>
#include <algorithm>
using namespace std;

const int N = 101;
const int M = 101;

int h[N][M], n, m, mark[26];
int visit[N][M], sink;
int d[4][2] = {-1, 0, 0, -1,  0, 1, 1, 0};

void dfs(int x, int y)
{
     int i, j, xx, yy, low = h[x][y];
     int dx, dy;
     for (i = 0; i < 4; i++)
     {
         xx = x + d[i][0];
         yy = y + d[i][1];
//             printf("i = %d x = %d y = %d xx = %d yy = %d low = %d\n", i, x, y, xx, yy, low);
         if (xx < 0 || xx >= n) continue;
         if (yy < 0 || yy >= m) continue;
         if (h[xx][yy] < low)
         {
             low = h[xx][yy];
             dx = xx;
             dy = yy;
         }
     }
//     printf("low = %d dx = %d dy = %d\n", low, dx, dy);
     if (h[x][y] == low)
     {
         visit[x][y] = sink++;
         return;
     }
     if (visit[dx][dy] < 0)
         dfs(dx, dy);
     visit[x][y] = visit[dx][dy];
//     printf("visit[%d][%d] = %d\n", x, y, visit[x][y]);
}

int main()
{
    int ncase, testcase;
    int i, j;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    scanf("%d", &ncase);
    for (testcase = 1; testcase <= ncase; testcase++)
    {
          scanf("%d%d", &n, &m);
          for (i = 0; i < n; i++)
              for (j = 0; j < m; j++)
              scanf("%d", &(h[i][j]));
          memset(visit, 0xff, sizeof(visit));
          sink = 0;
          for (i = 0; i < n; i++)
              for (j = 0; j < m; j++)
              if (visit[i][j] < 0)
                  dfs(i, j);
                  
          printf("Case #%d:\n", testcase);
          int cnt = 0;
          memset(mark, 0xff, sizeof(mark));
          for (i = 0; i < n; i++)
          {
              for (j = 0; j < m; j++)
              {
                  if (mark[visit[i][j]] < 0)
                      mark[visit[i][j]] = cnt++;
                  printf("%c", mark[visit[i][j]] + 'a');
                  if (j < m - 1)
                      printf(" ");
              }
              printf("\n");
          }
    }
    return 0;
}
