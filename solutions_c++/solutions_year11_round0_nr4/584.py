#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long LL;
const int MaxN = 1005;
bool vst[MaxN];
int a[MaxN];
int dfs(int u)
{
    vst[u] = 1;
    if(vst[a[u]])return 1;
    return dfs(a[u])+1;
}

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T,cas = 0;
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        for(int i = 1; i <= n; i++)scanf("%d",&a[i]);
        memset(vst, 0, sizeof(vst));
        double ret = 0;
        for(int i = 1; i <= n; i++)
            if(!vst[i])
            {
                int x = dfs(i);
                if(x>1)ret += x;
            }
        printf("Case #%d: %.6f\n",++cas,ret);
    }

    return 0;
}
