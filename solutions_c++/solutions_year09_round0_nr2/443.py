#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>
#include <string>
#include <cstring>
using namespace std;
#define sz(x) (int)x.size()
int H, W;
int M[110][110];
bool vis[110][110];
int fa[10010];
int ans[10010];
int dir[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };
int h;
int Find(int u)  {
    if(fa[u] == u)  return u;
    int fu = Find(fa[u]);
    return fa[u] = fu;
}
void Union(int u, int v)  {
    u = Find(u);
    v = Find(v);
    fa[v] = u;
    //if(u == 2)  cout << v << endl;
}
void dfs(int r, int c)  {
    vis[r][c] = 1;
    int minh = 10010, ux, uy;
    for(int k = 0; k < 4; k++)  {
        int x = r + dir[k][0];
        int y = c + dir[k][1];
        if(x >= 0 && x < H && y >= 0 && y < W && M[x][y] < M[r][c] && M[x][y] < minh)  {
            minh = M[x][y];
            ux = x, uy = y;
        }
    }
    if(minh == 10010)  {
        ans[r * W + c] = h++;
        
    }
    else  {
        //cout << r << ' ' << c << ' ' << ux << ' ' << uy << ' ' << endl;
        //if(Find(ux * W + uy) == 6)  cout << ux << ' ' << uy << ' ' << r << ' ' << c << ' ' << minh << endl;
        Union(ux * W + uy, r * W + c);
        if(vis[ux][uy] == 0)  dfs(ux, uy);
    }
}
int main() {
    freopen("Bbig.out", "w", stdout);
	int t;
    cin >> t;
    int Case = 1;
    while(t--)  {
        cin >> H >> W;
        for(int i = 0; i < H; i++)  {
            for(int j = 0; j < W; j++)  scanf("%d", &M[i][j]);
        }
        for(int i = 0; i < H * W; i++)  fa[i] = i;
        memset(vis, 0, sizeof(vis));
        h = 0;
        for(int i = 0; i < H; i++)  {
            for(int j = 0; j < W; j++)  {
                if(vis[i][j] == 0)   dfs(i, j);
            }
        }
        //cout << ans[2] << endl;
        //cout << Find(2) << endl;
        printf("Case #%d:\n", Case++);        
        for(int i = 0; i < H; i++)  {
            int tmp = Find(i * W);
            printf("%c", 'a' + ans[tmp]);
            for(int j = 1; j < W; j++)  {
                tmp = Find(i * W + j);
                //cout << tmp / W << ' ' << tmp % W << endl;
                printf(" %c", 'a' + ans[tmp]);
            }
            printf("\n");
        }
    }
    return 0;
}
                    
                 
        
        
