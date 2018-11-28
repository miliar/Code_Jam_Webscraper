#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#define f(i, n) for(int i = 0; i < n; i++)
#define s(n) scanf("%d", &n)
#define sc(n) scanf("%s", &n)
#define fill(a, v) memset(a, v, sizeof a)
#define inf (int)1e9
using namespace std;

int w, h, a[101][101];
char ch[101][101], cur;
int vis[101][101], id;
int dx[] = {-1, 0, 0, 1}, dy[] = {0, -1, 1, 0};

char dfs(int x, int y)
{
     //cout << x << " " << y << endl;
     if(vis[x][y] == id) return ch[x][y];
     vis[x][y] = id;
     
     int cx, cy, px, py, m = a[x][y];
     bool bb = false;
     
     f(i, 4)
     {
          cx = x + dx[i];
          cy = y + dy[i];
          if(cx < 0 || cy < 0 || cx >= h || cy >= w) continue;
          if(a[cx][cy] < m)
          {
               bb = true;
               m = a[cx][cy];
               px = cx;
               py = cy;
          }
     }
     
     if(bb)
     {
           //printf("from (%d %d), goto  (%d %d)\n", x, y, px, py);
           return ch[x][y] = dfs(px, py);
     }
     //printf("from (%d %d), cant go newer\n", x, y);
     return ch[x][y] = cur++;
}

main()
{
	int t;
	s(t);
	for(int zz = 1; zz <= t; zz++)
	{
         id++;
         cur = 'a';
         s(h); s(w);
         f(i, h) f(j, w) s(a[i][j]);
         f(i, h)
              f(j, w)
                   if(vis[i][j] != id) dfs(i, j);
                   
         printf("Case #%d:\n", zz);
         f(i, h)
         {
              //printf("%s\n", ch[i]);
              f(j, w) printf("%c ", ch[i][j]);
              printf("\n");
         }
    }
}
