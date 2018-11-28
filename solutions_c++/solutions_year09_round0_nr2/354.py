#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

const int maxn = 100 + 10;

int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int g[maxn][maxn], v[maxn][maxn], c[maxn][maxn], now, h, w;

int dfs(int x, int y)
{
    if (c[x][y] != -1)
        return c[x][y];
        
    //printf ("%d %d\n", x, y);
    
    int minh = g[x][y];
    int diri = -1;
    
    for (int i = 0; i < 4; ++i) {
        int nx = x + dir[i][0];
        int ny = y + dir[i][1];
        if (nx >= 0 && ny >= 0 && nx < h && ny < w) {
            if (g[nx][ny] < minh) {
                minh = g[nx][ny];
                diri = i;
            }
        }
    }
    if (diri == -1)
        return c[x][y] = now++;
    v[x][y] = 1;
    return c[x][y] = dfs(x + dir[diri][0], y + dir[diri][1]);
}

int main()
{
    int testcase;
    
    //freopen ("F:/B-large.in", "r", stdin);
    //freopen ("B-large.out", "w", stdout);
    
    scanf ("%d", &testcase);
    
    for (int Case = 1; Case <= testcase; ++Case) {
        scanf ("%d%d", &h, &w);
        for (int i = 0; i < h; ++i) 
            for (int j = 0; j < w; ++j)
                scanf ("%d", &g[i][j]);
                
        memset (c, -1, sizeof(c));
        memset (v, 0, sizeof(v));
        now = 0;
        for (int i = 0; i < h; ++i) 
            for (int j = 0; j < w; ++j)
                if (!v[i][j])
                    dfs(i, j);
                    
        printf ("Case #%d:\n",Case);

        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                if (j) printf (" ");
                printf ("%c", (char)('a' + c[i][j]));
            }
            printf ("\n");
        }
    }
    
    //while (1);
    
    return 0;
}
