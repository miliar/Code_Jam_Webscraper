/**********************************************************************
Author: Sherlock
Created Time:  2009/9/27 1:35:55
File Name: C.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int   maxint  =   0x7FFFFFFF;

int         n, ans;
int         a[110][110], s[110][110], len[110];
bool        board[110][110];

void            init()
{
    int m;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i ++)
    {
        for (int j = 0; j < m; j ++)
            scanf("%d", &a[i][j]);
        for (int j = 0; j < i; j ++)
        {
            board[i][j] = true;
            for (int k = 1; k < m; k ++)
            {
                if ((long long)(a[i][k] - a[j][k]) * (long long)(a[i][k - 1] - a[j][k - 1]) <= 0)
                {
                    board[i][j] = false;
                    break;
                }
            }
            board[j][i] = board[i][j];
        }
    }
}

void            make(int now, int tot)
{
    if (tot >= ans)
        return ;
    if (now == n)
    {
        ans = tot;
        return ;
    }
    for (int i = 0; i < tot; i ++)
    {
        bool flag = true;
        for (int j = 0; j < len[i]; j ++)
            if (! board[now][s[i][j]])
            {
                flag = false;
                break;
            }
        if (flag)
        {
            s[i][len[i] ++] = now;
            make(now + 1, tot);
            len[i] --;
        }
    }
    s[tot][0] = now;
    len[tot] = 1;
    make(now + 1, tot + 1);
}

void            solve()
{
    ans = n + 1;
    make(0, 0);
    printf("%d\n", ans);
}

int             main()
{
    freopen("C.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
    {
        printf("Case #%d: ", i);
        init();
        solve();
    }
    return 0;
}

