/**********************************************************************
Author: Sherlock
Created Time:  2009/9/26 23:33:09
File Name: C.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

const int   maxint  =   0x7FFFFFFF;

int         n;
int         a[5];

struct      node
{
    int     x, y, r;
}   que[10];

void            init()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++)
    {
        scanf("%d%d%d", &que[i].x, &que[i].y, &que[i].r);
    }
}

double          dist(int a, int b, int c, int d)
{
    return sqrt((a - c) * (a - c) + (b - d) * (b - d) + 0.0);
}

double          make(int a, int b)
{
    if (que[a].r < que[b].r)
        swap(a, b);
    if (dist(que[a].x, que[a].y, que[b].x, que[b].y) + que[b].r < que[a].r)
    {
        return que[a].r;
    }
    return (dist(que[a].x, que[a].y, que[b].x, que[b].y) + que[a].r + que[b].r) / 2;
}

void            solve()
{
    if (n == 1)
    {
        printf("%.6lf\n", que[0].r + 0.0);
        return ;
    }
    if (n == 2)
    {
        printf("%.6lf\n", max(que[0].r, que[1].r) + 0.0);
        return ;
    }
    for (int i = 0; i < 3; i ++)
        a[i] = i;
    double ans = 1e20;
    do 
    {
        ans = min(ans, max(make(a[0], a[1]), que[a[2]].r + 0.0));
    }   while (next_permutation(a, a + 3));
    printf("%.6lf\n", ans);
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

