#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3fffffff
#define LL long long
#define N 1005
double x[N], y[N];
int n, w, l, dp[N][N], pre[N][N], sumr[N];
struct Node
{
    int r, idx;
    bool operator < (const Node cur)const
    {
        if(r != cur.r)   return r < cur.r;
        else             return idx < cur.idx;
    }
};
Node ra[N];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cas = 1, i, j, k;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d", &n, &w, &l);
        for(i = 1; i <= n; i++)
        {
            scanf("%d", &ra[i].r);
            ra[i].idx = i;
        }
        sort(ra + 1, ra + 1 + n);
        for(i = 1, sumr[0] = 0; i <= n; i++)
        {
            sumr[i] = sumr[i - 1] + ra[i].r;
        }
        for(i = 0; i <= n; i++)
        {
            for(j = 0; j <= n; j++)
            {
                dp[i][j] = INF;
                pre[i][j] = -1;
            }
        }
        int tl = -ra[1].r;
        for(i = 1; i <= n; i++)
        {
            if(tl + ra[i].r <= w)
                dp[1][i] = ra[i].r;
            else
                break;
            tl += 2 * ra[i].r;
        }
        for(i = 2; i <= n; i++)
        {
            for(j = i; j <= n; j++)
            {
                for(k = i - 1; k < j; k++)
                {
                    int tl = 2 * (sumr[j] - sumr[k]) - ra[j].r - ra[k + 1].r;
                    int ht = dp[i - 1][k] + ra[j].r;
                    if(tl <= w &&  ht <= l && ht + ra[j].r <= dp[i][j])
                    {
                        dp[i][j] = ht + ra[j].r;
                        pre[i][j] = k;
                    }
                }
            }
        }
        if(dp[1][n] - ra[n].r <= l)
        {
            int offset = -ra[1].r;
            for(i = 1; i <= n; i++)
            {
                offset += ra[i].r;
                y[ra[i].idx] = 0, x[ra[i].idx] = offset;
                offset += ra[i].r;
            }
        }
        else
        {
            for(i = 2; i <= n; i++)
            {
                if(dp[i][n] - ra[n].r <= l)
                {
                    int lev = i, ed = n;
                    while(lev)
                    {
                        int offset = -ra[pre[lev][ed] + 1].r;
                        for(j = pre[lev][ed] + 1; j <= ed; j++)
                        {
                            offset += ra[j].r;
                            y[ra[j].idx] = dp[lev][ed] - ra[ed].r;
                            x[ra[j].idx] = offset;
                            offset += ra[j].r;
                        }
                        ed = pre[lev][ed];
                        lev--;
                    }
                }
            }
        }
        printf("Case #%d:", cas++);
        for(i = 1; i <= n; i++)
        {
            printf(" %.3lf %.3lf", x[i], y[i]);
        }
        printf("\n");
    }
    return 0;
}
