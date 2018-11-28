/**********************************************************************
Author: Sherlock
Created Time:  2010/6/5 22:36:47
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int   maxint  =   0x7FFFFFFF;

int         n, m;
int         board[110][110], next[110][110];

void            init()
{
    n = 0;
    memset(board, 0, sizeof(board));
    scanf("%d", &m);
    for (int i = 0; i < m; i ++)
    {
        int x1, x2, y1, y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        x1 --;
        y1 --;
        n = max(n, max(x2, y2));
        for (int a = x1; a < x2; a ++)
            for (int b = y1; b < y2; b ++)
                board[a][b] = 1;
    }
}

int             solve()
{
    int cnt = 0;
    while (true)
    {
        bool flag = true;
        for (int i = 0; i < n && flag; i ++)
            for (int j = 0; j < n; j ++)
                if (board[i][j] == 1)
                {
                    flag = false;
                    break;
                }
        if (flag)
            break;
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < n; j ++)
            {
                next[i][j] = board[i][j];
                if (board[i][j] == 1)
                {
                    if (i - 1 < 0 || j - 1 < 0 || (board[i - 1][j] == 0 && board[i][j - 1] == 0))
                        next[i][j] = 0;
                }
                else
                {
                    if (i - 1 >= 0 && j - 1 >= 0 && board[i - 1][j] == 1 && board[i][j - 1] == 1)
                        next[i][j] = 1;
                }
            }
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < n; j ++)
                board[i][j] = next[i][j];
        cnt ++;
    }
    return cnt;
}

int             main()
{
    freopen("C_small.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
    {
        init();
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}

