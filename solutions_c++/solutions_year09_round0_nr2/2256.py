#include<stdio.h>
#include<stdlib.h>
int H, W;
int alt[200][200];
char map[200][200];

int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};

char dfs(int sx, int sy, char mark) {
    if (sx < 0 || sx >= H || sy < 0 || sy >= W) return 0;
    if (map[sx][sy] != 0) return map[sx][sy];
    {
        int nx = sx, ny = sy;
        for (int i = 0 ; i < 4 ; ++i) {
            int tx = sx + dx[i];
            int ty = sy + dy[i];
            if (tx < 0 || tx >= H || ty < 0 || ty >= W) continue;
            if (alt[tx][ty] < alt[nx][ny]) {
                nx = tx; ny = ty;
            }
        }
        if (nx == sx && ny == sy) {
            return map[sx][sy] = mark;
        }
        char ret = dfs(nx,ny,mark);
        if (ret == mark) {
            return map[sx][sy] = mark;
        }
        else {
            return map[sx][sy] = ret;
        }
    }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large-res.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int TC = 1 ; TC <= T ; ++TC) {
        scanf("%d%d", &H, &W);
        for (int i = 0 ; i < H ; ++i) for (int j = 0 ; j < W ; ++j) scanf("%d", &alt[i][j]);
        for (int i = 0 ; i < H ; ++i) for (int j = 0 ; j < W ; ++j) map[i][j] = 0;
 
        char s = 'a';
        for (int i = 0 ; i < H ; ++i) for (int j = 0 ; j < W ; ++j) {
            if (map[i][j] != 0) continue;
            char ns = dfs(i,j,s);
            if (ns == s) ++s;
        }
        
        // output
        printf("Case #%d:\n", TC);
        for (int i = 0 ; i < H ; ++i) {
            for (int j = 0 ; j < W ; ++j) {
                if (j > 0) printf(" ");
                printf("%c", map[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
