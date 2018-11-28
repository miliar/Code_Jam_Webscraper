#include<iostream>
using namespace std;
typedef long long LL;
int N, R, k;
int g[1024];
int vis[1024];
LL sum[1024];
LL Solve()
{
    int i, j, t, p;
    LL res = 0;
    memset(vis, -1, sizeof(vis));
    int s = 0;
    for(i = 0; i < N; ++i) s += g[i];
    if(s <= k) return (LL)s * R;
    
    i = 0;
    vis[0] = 0;
    sum[0] = 0;
    int ctr = 0;
    LL loop = 0;
    while(1)
    {
        ctr++;
        t = k;
        for(j = i; t >= g[j]; t -= g[j], res += g[j], j = (j + 1) % N);
        if(vis[j] != -1) break;
        else
        {
             vis[j] =  ctr;
             sum[j] = res;
             i = j;
        }
    }
    int mod = ctr - vis[j];
    loop = res - sum[j];
    //printf("%d  %lld\n", mod, res);
    
    res = 0;
    int NL = vis[j];
    for(p = 0, j = 0; p < NL; ++p)
    {
        t = k;
        for(; t >= g[j]; t -= g[j], res += g[j], j = (j + 1) % N);
    }
    R -= NL;
    
    res += (LL)(R / mod) * loop;
    
    NL = R % mod;
    for(p = 0; p < NL; ++p)
    {
        t = k;
        for(; t >= g[j]; t -= g[j], res += g[j], j = (j + 1) % N);
    }
    return res;
    
}
int main()
{
    int t, cs = 0;
    int i, j;
    freopen("C_S.in", "r", stdin);
    freopen("C_S.out", "w", stdout);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d", &R, &k, &N);
        for(i = 0; i < N; ++i)
            scanf("%d", g + i);
        printf("Case #%d: %lld\n", ++cs, Solve());
    }
}
/*
20
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3

1 6 4
1 4 2 1
2 6 4
1 4 2 1
3 6 4
1 4 2 1
4 6 4
1 4 2 1
5 6 4
1 4 2 1
6 6 4
1 4 2 1
7 6 4
1 4 2 1
*/
