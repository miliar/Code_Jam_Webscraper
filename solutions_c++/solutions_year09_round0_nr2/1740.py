#include<stdio.h>
#include<string.h>
#include<stdlib.h>

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

int map[109][109], d[109][109], h, w, i, j, t, tot, tt;

int dfs(int x, int y)
{
    int dd, nx = -1, ny;
    if (map[x][y]) return map[x][y];
    
    dd = d[x][y];
    if (x>0 && d[x-1][y]<dd){
        dd = d[x-1][y];
        nx = x - 1;
        ny = y;
    }
    
    if (y>0 && d[x][y-1]<dd){
        dd = d[x][y-1];
        nx = x;
        ny = y - 1;
    }
    
    if (y+1<w && d[x][y+1]<dd){
        dd = d[x][y+1];
        nx = x;
        ny = y + 1;
    }
    
    if (x+1<h && d[x+1][y]<dd){
        dd = d[x+1][y];
        nx = x + 1;
        ny = y;
    }
    
    if (nx == -1){
        map[x][y] = tot;
        tot ++;
    }else{
        map[x][y] = dfs(nx, ny);
    }
    return map[x][y];
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    scanf("%d", &t);
    for (tt=1;tt<=t;tt++){
        scanf("%d%d", &h, &w);
        for (i=0;i<h;i++)
            for (j=0;j<w;j++)
                scanf("%d", &d[i][j]);
        memset(map, 0, sizeof(map));
        tot = 1;
        for (i=0;i<h;i++)
            for (j=0;j<w;j++)
                dfs(i, j);
        printf("Case #%d:\n", tt);
        for (i=0;i<h;i++){
            for (j=0;j<w;j++)
                printf("%c%c", map[i][j]+'a' - 1, j==w-1?'\n':' ');
        }
    }
    return 0;
}
