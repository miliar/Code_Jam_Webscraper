/**********************************************************************
Author: Sherlock
Created Time:  2010/6/5 22:20:54
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
const int   maxSize =   1 << 11;

int         n, m;
int         que[maxSize], cost[maxSize], father[maxSize], f[maxSize][15], left[maxSize], right[maxSize];
bool        done[maxSize];

void            init()
{
    scanf("%d", &m);
    n = 1 << m;
    for (int i = 0; i < n; i ++)
    {
        scanf("%d", &que[i]);
        que[i] = m - que[i];
    }
    int t = n / 2;
    for (int i = 0; i < n - 1; i ++)
    {
        scanf("%d", &cost[i]);
        if (i == n - 2)
            break;
        father[i] = t;
        if (i % 2 == 0)
            left[t] = i;
        else
        {
            right[t] = i;
            t ++;
        }
    }
}

int             min(int a, int b)
{
    if (a == -1 || b < a)
        return b;
    else
        return a;
}

void            solve()
{
    memset(f, -1, sizeof(f));
    for (int i = 0; i < n / 2; i ++)
        f[i][max(que[i * 2], que[i * 2 + 1])] = 0;
    for (int i = 0; i < n - 2; i += 2)
    {
        for (int j = 0; j <= m; j ++)
        {
            if (f[i][j] == -1)
                continue;
            for (int k = 0; k <= m; k ++)
            {
                if (f[i + 1][k] == -1)
                    continue;
                int t = father[i];
                f[t][max(j, k)] = min(f[t][max(j, k)], f[i][j] + f[i + 1][k]);
                if (j > 0)
                    f[t][max(j - 1, k)] = min(f[t][max(j - 1, k)], f[i][j] + f[i + 1][k] + cost[i]);
                if (k > 0)
                    f[t][max(j, k - 1)] = min(f[t][max(j, k - 1)], f[i][j] + f[i + 1][k] + cost[i + 1]);
                if (j > 0 && k > 0)
                    f[t][max(j, k) - 1] = min(f[t][max(j, k) - 1], f[i][j] + f[i + 1][k] + cost[i] + cost[i + 1]);
            }
        }
    }
    
    int ans;
    if (f[n - 2][0] != -1)
        ans = f[n - 2][0];
    if (f[n - 2][1] != -1)
        ans = min(ans, f[n - 2][1] + cost[n - 2]);
    printf("%d\n", ans);
}

int             main()
{
    //freopen("B_large.in", "r", stdin);
    freopen("B_large.out", "w", stdout);
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

