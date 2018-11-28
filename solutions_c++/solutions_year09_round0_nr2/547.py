/*************************************************************************
Author: aMR
Created Time: 2009-9-3 14:40:10
File Name: b.cpp
Description: 
************************************************************************/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <queue>
using namespace std;
const int inf=0x7fffffff;
const int maxn = 110;
int n, m, cnt;

const int fx[4] = { -1, 0, 0, 1};
const int fy[4] = { 0, -1, 1, 0};

bool out(int x, int y) {
    return x<0 || x>=n || y<0 || y>=m;
}

int d[maxn][maxn];
int mark[maxn][maxn];
int tmp[32];

int dfs(int x, int y) {
    if(mark[x][y]) return mark[x][y];
    int t = -1, mx = d[x][y];
    for(int i=0; i<4; ++i) {
        int tx = x + fx[i];
        int ty = y + fy[i];
        if(out(tx, ty)) continue;
        if(d[tx][ty] < mx) {
            mx = d[tx][ty];
            t = i;
        }
    }
    if(-1 == t)
        return mark[x][y] = cnt++;
    int tx = x + fx[t];
    int ty = y + fy[t];
    return mark[x][y] = dfs(tx, ty);
}

int main()
{
    freopen("b.txt", "w", stdout);
    int ca = 0, z;
    scanf("%d", &z);
    while(z--) {
        scanf("%d%d", &n, &m);
        cnt = 1;
        for(int i=0; i<n; ++i) {
            for(int j=0; j<m; ++j) {
                scanf("%d", &d[i][j]);
            }
        }
        memset(mark, 0, sizeof(mark));
        for(int i=0; i<n; ++i) {
            for(int j=0; j<m; ++j) {
                if(mark[i][j]) continue;
                dfs(i, j);
            }
        }
        memset(tmp, 0, sizeof(tmp));
        cnt = 1;
        printf("Case #%d:\n", ++ca);
        for(int i=0; i<n; ++i) {
            for(int j=0; j<m; ++j) {
                if(j) putchar(' ');
                if(!tmp[mark[i][j]]) {
                    tmp[mark[i][j]] = cnt ++;
                }
                putchar('a' + tmp[mark[i][j]] - 1);
            }
            puts("");
        }
    }
    return 0;
}

