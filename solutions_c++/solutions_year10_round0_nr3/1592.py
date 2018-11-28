/**********************************************************************
Author: Jun
Created Time:  2010/5/8 13:20:13
File Name: b1.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxn = 1000 + 10;

long long g[maxn], totnum[maxn];
int idnum[maxn];
long long   r, k;
int case_num, n;

void work()
{
    scanf("%I64d %I64d %d", &r, &k, &n);
    for (int i = 0; i < n; i ++)
        scanf("%I64d", &g[i]);
    int id = 0;
    long long  aa = 0, ans = 0;
    memset(idnum, -1, sizeof(idnum));
    memset(totnum, 0, sizeof(totnum));
    for (int i = 1; i <= r; i ++)
    {
        long long tot = 0, t = 0;
        int start = id;
        idnum[start] = i;
        while (tot + g[id] <= k && t < n)
        {
            tot += g[id];
            id = (id + 1) % n;
            t ++;
        }
        aa += tot;
        totnum[i] = aa;
        if (idnum[id] != -1)
        {
            ans = (r - idnum[id] + 1) / (i + 1 - idnum[id]) * (aa - totnum[idnum[id] - 1]);
            int tmp = ((r - idnum[id] + 1) % (i + 1 - idnum[id]));
            ans += totnum[idnum[id] + tmp - 1] - totnum[idnum[id] - 1];
            ans += totnum[idnum[id] - 1];
            break;
        }
        if (i == r) ans = totnum[i];
    }
    printf("%I64d\n", ans);
}

int main()
{
    freopen("b.out", "w", stdout);
    scanf("%d", &case_num);
    for (int i = 0; i < case_num; i ++)
    {
        printf("Case #%d: ", i + 1);
        work();
    }
    return 0;
}

