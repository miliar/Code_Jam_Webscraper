/**********************************************************************
Author: Sherlock
Created Time:  2009-9-3 14:31:19
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int   maxint      =   0x7FFFFFFF;
const int   maxSize     =   100 + 10;
const int   move[4][2]  =   {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int         n, m, color, total;
int         board[maxSize][maxSize], ans[maxSize][maxSize], hash[30];

struct      node
{
    int     x, y, k;
}   que[maxSize * maxSize];

bool            cmp(node a, node b)
{
    if (a.k != b.k)
        return a.k > b.k;
    return ((a.x < b.x) || (a.x == b.x && a.y < b.y));
}

void            init()
{
    scanf("%d%d", &n, &m);
    int now = 0;
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
        {
            scanf("%d", &board[i][j]);
            que[now].k = board[i][j];
            que[now].x = i;
            que[now].y = j;
            now ++;
        }
    sort(que, que + now, cmp);
}

void            make(int x, int y)
{
    int c, d, l = board[x][y];
    for (int i = 0; i < 4; i ++)
    {
        int a = x + move[i][0];
        int b = y + move[i][1];
        if (a < 0 || a >= n || b < 0 || b >= m)
            continue;
        if (board[a][b] < l)
        {
            l = board[a][b];
            c = a;
            d = b;
        }
    }
    if (l == board[x][y])
    {
        color = total;
        ans[x][y] = color;
        total ++;
        return ;
    }
    else
    {
        if (ans[c][d] != -1)
        {
            color = ans[c][d];
            ans[x][y] = color;
            return ;
        }
        make(c, d);
        ans[x][y] = color;
    }
}

void            solve()
{
    total = 0;
    memset(ans, -1, sizeof(ans));
    for (int i = 0; i < n * m; i ++)
        if (ans[que[i].x][que[i].y] == -1)
            make(que[i].x, que[i].y);
    memset(hash, -1, sizeof(hash));
    int now = 0;
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < m; j ++)
        {
            if (hash[ans[i][j]] == -1)
                hash[ans[i][j]] = now ++;
            ans[i][j] = hash[ans[i][j]];
        }
    for (int i = 0; i < n; i ++)
    {
        for (int j = 0; j < m - 1; j ++)
            printf("%c ", 'a' + ans[i][j]);
        printf("%c\n", 'a' + ans[i][m - 1]);
    }
}

int             main()
{
    freopen("B_large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int cnt = 0;
    while (T > 0)
    {
        T --;
        printf("Case #%d:\n", ++ cnt);
        init();
        solve();
    }
    return 0;
}

