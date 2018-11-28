#include<stdio.h>
#include<memory.h>
#define QSIZE 262143
long long one = 1;
struct Node
{
    int cx, cy;
    long long vis[4];
};
char map[20][20];
Node que[QSIZE + 1];
int R, C, front, rear, step;
int minT[20][20];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

bool inside(int y, int x)
{
     return y >= 0 && y < R && x >= 0 && x < C;
}
void CheckVis(Node& ne)
{
     int y2, x2, i, k;
     for(i = 0; i < 4; ++i)
     {
         y2 = ne.cy;
         x2 = ne.cx;
         while(inside(y2 + dy[i], x2 + dx[i]) && !( map[y2 + dy[i]][x2 + dx[i]] == '#'))
             y2 += dy[i],x2 += dx[i];
        // if(inside(y2, x2) && map[y2][x2] == 'X') continue; 
         k = (y2 * C + x2);
         ne.vis[k / 60] |= one << (k % 60);
     }
}
int BFS()
{
    memset(minT, 63, sizeof(minT));
    int i, j, re, k, ii, jj;
    Node cur, ne;
    front = rear = step = 0;
    for(i = 0; i < R; ++i)
        for(j = 0; j < C; ++j)
            if(map[i][j] == 'O') ii = i, jj = j;
    cur.cy = ii; cur.cx = jj; 
    memset(cur.vis, 0, sizeof(cur.vis));
    CheckVis(cur);
    
    minT[i][j] = 0;
    que[rear++] = cur;
    while(front != rear)
    {
       re = rear;
       ++step;
      while(front != re)
      {
        cur = que[front++];
        front &= QSIZE;
        //printf("%d %d %lld\n", cur.cy, cur.cx, cur.vis);
        for(i = 0; i < 4; ++i)
        {
            ne.cy = cur.cy + dy[i];
            ne.cx = cur.cx + dx[i];
            if(!inside(ne.cy, ne.cx) || map[ne.cy][ne.cx] == '#')
            {
                for(k = 0; k < R * C; ++k)
                   if(cur.vis[k / 60] & (one << (k % 60)))
                   {
                      // printf("K: %d\n", k);
                       ne.cy = k / C;
                       ne.cx = k % C;
                       //ne.vis1 = ne.vis2 = 0;
                       memset(ne.vis, 0, sizeof(ne.vis));
                       if(map[ne.cy][ne.cx] == 'X') return step;
                       if(minT[ne.cy][ne.cx] <= step) continue;
                       minT[ne.cy][ne.cx] = step;
                       CheckVis(ne);
                       que[rear++] = ne;
                       rear &= QSIZE;
                   }
                continue;
            }
            memcpy(ne.vis, cur.vis, sizeof(long long) * 4);
            //ne.vis1 = cur.vis1;
            //ne.vis2 = cur.vis2;
            CheckVis(ne);
            if(map[ne.cy][ne.cx] == 'X') return step;
                 if(minT[ne.cy][ne.cx] <= step) continue;
           minT[ne.cy][ne.cx] = step;
           que[rear++] = ne;
           rear &= QSIZE;
        }
     }
        
    }
    return -1;
}
int main()
{
    int t, ctr = 0, res, i, j;
    freopen("B_L.in", "r", stdin);
    freopen("B_L.out", "w", stdout);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &R, &C);
        for(i = 0; i < R; ++i)
           // for(j = 0; j < C; ++j)
                scanf("%s", map[i]);
        res = BFS();
        printf("Case #%d: ", ++ctr);
        if(res == -1)
            printf("THE CAKE IS A LIE\n");
        else printf("%d\n", res);
    }
}
