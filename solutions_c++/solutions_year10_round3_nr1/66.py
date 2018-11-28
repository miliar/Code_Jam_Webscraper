/**********************************************************************
Author: Sherlock
Created Time:  2010/5/23 17:05:27
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
const int   maxSize =   1000 + 10;

int         n;
int         tree[200000];

pair    <int, int>  que[maxSize];

void            init()
{
    int a, b;
    scanf("%d", &n);
    for (int i = 0; i < n; i ++)
    {
        scanf("%d%d", &a, &b);
        que[i] = make_pair(a, b);
    }
    sort(que, que + n);
}

void            init_tree(int p, int l, int r)
{
    tree[p] = 0;
    if (l == r)
        return ;
    int mid = (l + r) / 2;
    init_tree(p * 2, l, mid);
    init_tree(p * 2 + 1, mid + 1, r);
}

void            insert_tree(int p, int l, int r, int x)
{
    tree[p] ++;
    if (l == r)
        return ;
    int mid = (l + r) / 2;
    if (x <= mid)
        insert_tree(p * 2, l, mid, x);
    else
        insert_tree(p * 2 + 1, mid + 1, r, x);
}

int             count_tree(int p, int l, int r, int x, int y)
{
    if (l == x && r == y)
        return tree[p];
    int mid = (l + r) / 2;
    if (y <= mid)
        return count_tree(p * 2, l, mid, x, y);
    else
        if (x > mid)
            return count_tree(p * 2 + 1, mid + 1, r, x, y);
        else
            return count_tree(p * 2, l, mid, x, mid) + count_tree(p * 2 + 1, mid + 1, r, mid + 1, y);
}

void            solve()
{
    int ans = 0;
    init_tree(1, 1, 10000);
    for (int i = 0; i < n; i ++)
    {
        ans += count_tree(1, 1, 10000, que[i].second, 10000);
        insert_tree(1, 1, 10000, que[i].second);
    }
    printf("%d\n", ans);
}

int             main()
{
    freopen("A_large.in", "r", stdin);
    freopen("A_large.out", "w", stdout);
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

