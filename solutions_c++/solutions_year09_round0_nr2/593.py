/**********************************************************************
Author: Jun
Created Time:  2009/9/3 15:25:32
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int maxint = 0x7FFFFFFF;
const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};
const int maxn = 100 + 10;

struct node 
{
    int h, x, y;
};

bool cmp(node a, node b)
{
    return a.h < b.h;
}

int ans[maxn][maxn], h[maxn][maxn];
bool ok[maxn][maxn][4];
node p[maxn * maxn];
int n, m, tot, l;

void doit(int x, int y)
{
    int minh = maxint, from = -1;
    for (int i = 0; i < 4; i ++)
    {
        int w = x + dx[i];
        int u = y + dy[i];
        if (w < 0 || w >= n || u < 0 || u >= m || ans[w][u] != -1 || h[w][u] >= h[x][y]) continue;
        if (h[w][u] < minh)
        {
            minh = h[w][u];
            from = i;
        }
    }
    if (from == -1) return;
    ok[x + dx[from]][y + dy[from]][from] = true;
}

void dfs(int x, int y)
{
    ans[x][y] = tot;
    for (int i = 0; i < 4; i ++)
    {
        if (!ok[x][y][i]) continue;
        if (ans[x - dx[i]][y - dy[i]] == -1)
            dfs(x - dx[i], y - dy[i]);
    }
}

void work()
{
    scanf("%d%d", &n, &m);
    l = 0;
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
        {
            scanf("%d", &h[i][j]);
            p[l].h = h[i][j];
            p[l].x = i;
            p[l].y = j;
            l ++;
        }
    sort(p, p + l, cmp);
    tot = 0;
    memset(ans, -1, sizeof(ans));
    memset(ok, 0, sizeof(ok));
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
            doit(i, j);
    for (int i = 0; i < l; i ++)
            if (ans[p[i].x][p[i].y] == -1)
            {
                dfs(p[i].x, p[i].y);
                tot ++;
            }
    int a[30];
    memset(a, -1, sizeof(a));
    tot = 0;
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
            if (a[ans[i][j]] == - 1)
            {
                a[ans[i][j]] = tot;        
                tot ++;
            }
    for (int i = 0; i < n; i ++)
    {
        for (int j = 0; j < m; j ++)
            if (j != m - 1)
                printf("%c ", a[ans[i][j]] + 'a');
            else printf("%c\n", a[ans[i][j]] + 'a');
    }
}

int main()
{
    freopen("b.out", "w", stdout);
    int case_num;
    scanf("%d", &case_num);
    for (int i = 0; i < case_num; i ++)
    {
        printf("Case #%d:\n", i + 1);
        work();
    }
    
    return 0;
}

