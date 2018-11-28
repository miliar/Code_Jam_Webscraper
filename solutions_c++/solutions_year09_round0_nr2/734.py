/**********************************************************************
Author: Xay
Created Time:  2009-9-3 15:00:36
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxn = 100 + 5;
const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

int n, m, cnt;
int a[maxn][maxn], flag[maxn][maxn];

int dfs(int x1, int x2) {
    if (flag[x1][x2] >= 0) return flag[x1][x2];
    int height = a[x1][x2], nx = -1, ny = -1;
    for (int i = 0; i < 4; ++i) {
        int tx = x1 + dx[i], ty = x2 + dy[i];
        if (tx < 0 || ty < 0 || tx >= n || ty >= m) continue;
        if (a[tx][ty] < height) {
            nx = tx;
            ny = ty;
            height = a[tx][ty];
        }
    }
    if (height == a[x1][x2]) return flag[x1][x2] = cnt++;
    return flag[x1][x2] = dfs(nx, ny);
}
int main()
{
    freopen("b.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ++ca) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                scanf("%d", &a[i][j]);
            }
        }
        printf("Case #%d:\n", ca);
        memset(flag, -1, sizeof(flag));
        cnt = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (j) putchar(' ');
                printf("%c", dfs(i, j) + 'a');
            }
            puts("");
        }
    }
    return 0;
}

