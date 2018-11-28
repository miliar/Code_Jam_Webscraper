#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};
int t;
int h, w;
int g[128][128];
char b[128][128];

char dfs(int x, int y, char flag)
{
     if(x < 0 || x >= h || y < 0 || y >= w)
     return 0;
     if(b[x][y] != 0)
     return b[x][y];
     //printf("%d %d %c\n", x, y, flag);
     b[x][y] = flag;
     int Min = 1000000, sx = -1, sy = -1;
     for(int i = 0; i < 4; i++)
     {
             int xx = x + dx[i];
             int yy = y + dy[i];
             if(xx >= 0 && xx < h && yy >= 0 && yy < w)
             {
                   if(g[xx][yy] < Min)
                     Min = g[xx][yy], sx = xx, sy = yy;
             }
            
     } if(Min < g[x][y])
             {
                 char tmp = 0;
                 if((tmp = dfs(sx, sy, flag)))
                 return tmp;
             }
     return 0;
 }
 
void Solve()
{
     memset(b, 0, sizeof(b));
     int i, j, k, q;
     char f = 'a';
     for(i = 0; i < h; i++)
     {
           for(j = 0; j < w; j++)
               if(!b[i][j])
               {
                   char r = dfs(i, j, f);
                   if(r)
                   {
                        
                        for(k = 0; k < h; k++)
                        for(q = 0; q < w; q++)
                        if(b[k][q] == f)
                        b[k][q] = r;
                        
                    }else f++;
               }
     }
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &t);
    int i, j, k;
    for(int tt = 1; tt <= t; tt++)
    {
            scanf("%d%d", &h, &w);
            for(i = 0; i < h; i++)
              for(j = 0; j < w; j++)
                scanf("%d", &g[i][j]);
           
           Solve();                 
            printf("Case #%d:\n", tt);
            for(i = 0; i < h; i++)
            {
                  putchar(b[i][0]);
                  for(j = 1; j < w; j++)
                    printf(" %c", b[i][j]);
                  puts("");
            }
     } 
    return 0;
} 
