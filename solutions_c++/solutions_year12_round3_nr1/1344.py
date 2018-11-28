#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int maxn = 1009;
const double esp = 1e-6;
int to[maxn][maxn], m[maxn], vis[maxn];
int n, ans;

void dfs(int nn)
{
    vis[nn]++;
    if(vis[nn]>=2) {ans=1; return;}
    int i, j;
    for(i=1; i<=m[nn]; i++)
    {
        dfs(to[nn][i]);
        if(ans==1) return;
    }
}

int main()
{
    freopen("C:\\Users\\Administrator\\Downloads\\A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    int t, tt, nn, mm, i;
    scanf("%d", &t);
    for(tt=1; tt<=t; tt++)
    {
        ans = 0;
        scanf("%d", &n);
        for(nn=1; nn<=n; nn++)
        {
            scanf("%d", &m[nn]);
            for(mm=1; mm<=m[nn]; mm++)
            {
                scanf("%d", &to[nn][mm]);
            }
        }
        for(nn=1; nn<=n; nn++)
        {
            memset(vis, 0, sizeof(vis));
            dfs(nn);
            if(ans==1) break;
        }
        printf("Case #%d: %s\n", tt, ans?"Yes":"No");
    }
	return 0;
}
