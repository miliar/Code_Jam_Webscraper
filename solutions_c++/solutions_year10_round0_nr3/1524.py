/**********************************************************************
Author: Sherlock
Created Time:  2010/5/8 10:57:56
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
const int   maxSize     =   1100;

int         n, m, k;
int         que[maxSize], pre[maxSize], s[maxSize];
long long   f[maxSize], g[maxSize];

void            init()
{
    scanf("%d%d%d", &k, &m, &n);
    for (int i = 0; i < n; i ++)
        scanf("%d", &que[i]);
    for (int i = 0; i < n; i ++)
    {
        g[i] = 0;
        for (int j = i, cnt = 0; cnt < n; j = (j + 1) % n, cnt ++)
        {
            g[i] += que[j];    
            if (g[i] > m)
            {
                g[i] -= que[j];
                break;
            }
        }
    }
}

long long       solve()
{
    memset(pre, -1, sizeof(pre));
    int last = 0;
    f[0] = 0;
    pre[0] = 0;
    s[0] = 0;
    int now = 0;
    long long cost = 0;
    while (true)
    {
        now ++;
        long long sum = 0;
        int cnt = 0;
        for (int i = last; ; i = (i + 1) % n)
        {
            cnt ++;
            sum += que[i];
            if (sum > m || cnt > n)
            {
                sum -= que[i];
                last = i;
                break;
            }
        }
        cost += sum;
        if (pre[last] != -1)
            break;
        f[last] = cost;
        pre[last] = now;
        s[now] = last;
    }
    
    if (pre[last] >= k)
    {
        for (int i = 0; i < n; i ++)
            if (pre[i] == k)
                return f[i];
    }
    else
    {
        long long ans = f[last];
        int l = now - pre[last];
        cost -= f[last];
        k -= pre[last];
        ans += cost * (k / l);
        for (int i = 0; i < k % l; i ++)
        {
//            printf("%d\n", g[s[now - l + i]]);
            ans += g[s[now - l + i]];
        }
//        printf("%d %d %I64d %d %I64d\n", last, l, f[last], pre[last], cost);
        return ans;
    }
}

long long       force()
{
    int now = 0;
    long long ans = 0;
    for (int i = 0; i < k; i ++)    
    {
        int cnt = 0;
        int last = now;
        int sum = 0;
        while (cnt < n)
        {
            sum += que[now];
            if (sum > m)
            {
                sum -= que[now];
                break;
            }
            now = (now + 1) % n;
            cnt ++;
        }
        ans += sum;
//        printf("%d -> %d : %d\n", last, now, sum);
    }
    return ans;
}

int             main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
    {
        init();
        printf("Case #%d: %I64d\n", i, solve());
    }
    return 0;
}

