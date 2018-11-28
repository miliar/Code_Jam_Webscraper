#include <stdio.h>
#include <algorithm>
#include <set>

using namespace std;

int n, m;
char map[30][30];
int flag[30][30];
int best[30][30];
int best1[30][30];
int best2[30][30];
int px[30][30], py[30][30];
int qx[900], qy[900], qp;
int ans;

int bfs () {
    qp = 0;
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
            if (flag[i][j] && map[i][j] == 'T') {
                best[i][j] = 0;
                qx[qp] = i;
                qy[qp] = j;
                qp ++;
                }
            else
                best[i][j] = -1;
    for (int i = 0; i < qp; i ++) {
        int x = qx[i];
        int y = qy[i];
        
        if (x - 1 >= 0 && map[x - 1][y] != '.' && best[x-1][y] == -1) {
            best[x-1][y] = best[x][y] + 1;
            qx[qp] = x - 1;
            qy[qp] = y;
            qp ++;
            }
        if (x + 1 < n && map[x + 1][y] != '.' && best[x+1][y] == -1) {
            best[x+1][y] = best[x][y] + 1;
            qx[qp] = x + 1;
            qy[qp] = y;
            qp ++;
            }
        if (y - 1 >= 0 && map[x][y-1] != '.' && best[x][y-1] == -1) {
            best[x][y-1] = best[x][y] + 1;
            qx[qp] = x;
            qy[qp] = y-1;
            qp ++;
            }
        if (y + 1 < m && map[x][y+1] != '.' && best[x][y+1] == -1) {
            best[x][y+1] = best[x][y] + 1;
            qx[qp] = x;
            qy[qp] = y+1;
            qp ++;
            }
        }
    

    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
            best1[i][j] = best[i][j];


    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
            if (flag[i][j])
                best2[i][j] = 0;
            else
                best2[i][j] = -1;
    while (1) {
        int bx, by;
        
        bx = -1;
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                if (map[i][j] != '.' && best[i][j] != -1 && best2[i][j] != -1 && (bx == -1 || best2[i][j] < best2[bx][by])) {
                    bx = i;
                    by = j;
                    }
        
        if (bx == -1)
            break;
        
        best[bx][by] = -1;
        
        if (bx - 1 >= 0 && best[bx - 1][by] != -1 && (best2[bx-1][by] == -1 || best2[bx][by] + best[bx-1][by] < best2[bx-1][by])) {
            px[bx-1][by] = bx;
            py[bx-1][by] = by;
            best2[bx-1][by] = best2[bx][by] + best[bx-1][by];
            }
        if (bx + 1 < n && best[bx + 1][by] != -1 && (best2[bx+1][by] == -1 || best2[bx][by] + best[bx+1][by] < best2[bx+1][by])) {
            px[bx+1][by] = bx;
            py[bx+1][by] = by;
            best2[bx+1][by] = best2[bx][by] + best[bx+1][by];
            }
        if (by - 1 >= 0 && best[bx][by - 1] != -1 && (best2[bx][by-1] == -1 || best2[bx][by] + best[bx][by-1] < best2[bx][by-1])) {
            px[bx][by-1] = bx;
            py[bx][by-1] = by;
            best2[bx][by-1] = best2[bx][by] + best[bx][by-1];
            }
        if (by + 1 < m && best[bx][by + 1] != -1 && (best2[bx][by+1] == -1 || best2[bx][by] + best[bx][by+1] < best2[bx][by+1])) {
            px[bx][by+1] = bx;
            py[bx][by+1] = by;
            best2[bx][by+1] = best2[bx][by] + best[bx][by+1];
            }
        }
    
/*
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j ++)
            printf("%3d ",best1[i][j]);
        printf("\n");
        }
    printf("\n");
    printf("\n");
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j ++)
            printf("%3d ",best2[i][j]);
        printf("\n");
        }
    printf("\n");
    printf("\n");
*/

    int bx = -1, by;
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
            if (!flag[i][j] && map[i][j] == 'T' && (bx == -1 || best2[i][j] < best2[bx][by])) {
                bx = i;
                by = j;
                }
    if (bx == -1) {
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                if (!flag[i][j] && best1[i][j] != -1)
                    ans += best1[i][j];
        return 0;
        }
//    printf("bx = %d, by = %d\n",bx,by);
    while (!flag[bx][by]) {
        flag[bx][by] = 1;
        ans += best1[bx][by];
        int tx, ty;
        
        tx = px[bx][by];
        ty = py[bx][by];
        bx = tx;
        by = ty;
        }
    
    return 1;
    }

int main () {
    int ct = 0, t;
    
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    
    for (scanf("%d", &t); t > 0; t --) {
        
        scanf("%d%d",&n,&m);
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                do scanf("%c", map[i] + j);
                    while (map[i][j] <= ' ');
        
        //Greedily pick a path...
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                flag[i][j] = 0;
        flag[0][0] = 1;
        
        ans = 0;
        while (bfs());
        
        printf("Case #%d: %d\n", ++ct, ans);
        }
   
    return 0;
    }
