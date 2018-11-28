/**********************************************************************
Author: Sherlock
Created Time:  2010/5/23 18:09:44
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
const int   maxSize =   520;

int         n, m;
char        buf[maxSize];
int         f[maxSize][maxSize], board[maxSize][maxSize], num[maxSize];
bool        done[maxSize][maxSize];

void            init()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i ++)
    {
        scanf("%s", buf);
        for (int j = 0; j < m / 4; j ++)
        {
            int x;
            if (buf[j] >= '0' && buf[j] <= '9')    
                x = buf[j] - '0';
            else
                x = 10 + (buf[j] - 'A');
            for (int k = 4 * j + 3; k >= 4 * j; k --)
            {
                board[i][k] = x % 2;
                x /= 2;
            }
        }
//        for (int j = 0; j < m; j ++)
//            printf("%d", board[i][j]);
//        printf("\n");
    }
}

void            solve()
{
    int left = n * m;
    memset(done, false, sizeof(done));
    memset(num, 0, sizeof(num));
    while (left > 0)
    {
        for (int i = 0; i < n; i ++)
        {
            if (done[i][m - 1])
                f[i][m - 1] = 0;
            else
                f[i][m - 1] = 1;
            for (int j = m - 2; j >= 0; j --)
            {
                if (done[i][j])
                {
                    f[i][j] = 0;
                    continue;
                }
                if (board[i][j] != board[i][j + 1])
                    f[i][j] = f[i][j + 1] + 1;
                else
                    f[i][j] = 1;
            }
        }
        int best = 1, x, y;
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
            {
                if (done[i][j] || f[i][j] == 1)
                    continue;
                int s = 1, h = f[i][j];
                for (int k = i + 1; k < n; k ++)
                {
                    if (board[k][j] == board[k - 1][j])
                        break;
                    if (f[k][j] < s)
                        break;
                    s ++;
                    h = min(f[k][j], h);
                    if (s > h)
                        break;
                    if (f[k][j] == s)
                        break;
                }
                s = min(s, h);
                if (s > best)
                {
                    best = s;
                    x = i;
                    y = j; 
                }
            }
        if (best > 1)
        {
            num[best] ++;
            for (int i = 0; i < best; i ++)
                for (int j = 0; j < best; j ++)
                    done[x + i][y + j] = true;
            left -= best * best;
        }
        else
            break;
    }
    
    int cnt = 0;
    num[1] = left;
    for (int i = 1; i <= min(n, m); i ++)
        if (num[i] > 0)
            cnt ++;
    printf("%d\n", cnt);
    for (int i = min(n, m); i > 0; i --)
        if (num[i] > 0)
            printf("%d %d\n", i, num[i]);
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

