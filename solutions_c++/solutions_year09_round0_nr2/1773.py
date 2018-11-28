/**********************************************************************
Author: hanshuai
Created Time:  2009-09-03 16:30:08
File Name: 2.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long int64;
const int maxint = 0x7FFFFFFF;
const int64 maxint64 = 0x7FFFFFFFFFFFFFFFLL;
const int maxn = 105;
int a[maxn][maxn], vis[maxn][maxn], deg[maxn][maxn], xc[30];
const int dx[]={-1, 0, 0, 1};
const int dy[]={0, -1, 1, 0};
vector<pair<int,int> > vt, vec[maxn][maxn];
int h, w;
inline bool out(int x, int y){
    return x < 0 || x >= h || y < 0 || y >= w;
}
void dfs(int x, int y, int id){
//    if(vis[x][y] == -1) while(1);
    vis[x][y] = id;
    for(int i = 0; i < (int)vec[x][y].size(); i ++){
        dfs(vec[x][y][i].first, vec[x][y][i].second, id);
    }
}
int main() {
    freopen("2.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for(int cas = 1; cas <= test; cas ++){
        scanf("%d%d", &h, &w);
        for(int i = 0; i < h; i ++){
            for(int j = 0; j < w; j ++){
                scanf("%d", &a[i][j]);
                vec[i][j].clear();
            }
        }
        vt.clear();
        int x, y;
        for(int i = 0; i < h; i ++){
            for(int j = 0; j < w; j ++){
                int mmin = a[i][j], idx = -1, idy = -1;
                for(int k = 0; k < 4; k ++){
                    x = i + dx[k]; y = j + dy[k];
                    if(out(x, y)) continue;
                    if(a[x][y] < mmin){
                        idx = x; idy = y;
                        mmin = a[x][y];
                    }
                }
                if(idx == -1) vt.push_back(make_pair(i, j));
                else vec[idx][idy].push_back(make_pair(i, j));
            }
        }
        if(vt.size() > 26) while(1);
        memset(vis, -1, sizeof(vis));
        for(int i = 0; i < (int)vt.size(); i ++){
            dfs(vt[i].first, vt[i].second, i);
        }
        
        int cnt = 0;
        memset(xc, -1, sizeof(xc));
        printf("Case #%d:\n", cas);
        for(int i = 0; i < h; i ++){
            for(int j = 0; j < w; j ++){
                if(vis[i][j] == -1) while(1);
                if(xc[vis[i][j]] == -1) xc[vis[i][j]] = cnt ++;
                printf("%c", xc[vis[i][j]] + 'a');
                if(j != w - 1) printf(" ");
                else printf("\n");
            }
        }
        
    }
    return 0;
}

