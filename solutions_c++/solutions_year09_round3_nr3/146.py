/**********************************************************************
Author: Jun
Created Time:  2009-9-13 17:25:23
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
const int maxn = 100 + 10;   

int n;
int que[maxn], f[maxn][maxn];

void init()
{
    int l;
    scanf("%d%d", &l, &n);
    for (int i = 1; i <= n; i ++)
        scanf("%d", &que[i]);
    que[0] = 0;
    que[n + 1] = l + 1;
    n += 2;
    sort(que, que + n);
}

int make(int l, int r)
{
    if (f[l][r] != -1)
        return f[l][r];
    if (r == l + 1)
    {
        f[l][r] = 0;
        return 0;
    }
    f[l][r] = maxint;
    for (int k = l + 1; k < r; k ++)
        f[l][r] = min(f[l][r], make(l, k) + make(k, r) + que[r] - que[l] - 2);
    return f[l][r];
}

void solve()
{
    memset(f, -1, sizeof(f));
    make(0, n - 1);
    printf("%d\n", f[0][n - 1]);
}

int main()
{
    freopen("C.out", "w", stdout);
    int case_num;
    scanf("%d", &case_num);
    for (int i = 0; i < case_num; i ++)
    {
        printf("Case #%d: ", i + 1);
        init();
        solve();
    }
    return 0;
}

