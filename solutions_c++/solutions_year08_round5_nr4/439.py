#include <cstdio>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
const int maxn = 110;
const int M = 10007;
int g[maxn][maxn];
int f[maxn][maxn];
int i,j,m,n,x,y,k;

bool ok(int i,int j)
{
    if (i > 0 && i <= n && j > 0 && j <= m)
        return true;
    return false;
}

void work()
{
    memset(f,0,sizeof(f));
    f[1][1] = 1;
    for (i = 1; i <= n; ++i)
        for (j = 1; j <= m; ++j)
            if (!g[i][j])
            {
                if (ok(i-1,j-2) && !g[i-1][j-2])
                    f[i][j] = f[i-1][j-2] % M;
                if (ok(i-2,j-1) && !g[i-2][j-1])
                    f[i][j] = (f[i][j] + f[i-2][j-1]) % M;
                 //   printf("%d %d %d\n",i,j,f[i][j]);
            }
}

int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int Test;
    scanf("%d",&Test);
    for (int T = 1; T <= Test; ++T)
    {
        memset(g,0,sizeof(g));
        scanf("%d%d%d",&n,&m,&k);
        for (int i = 1; i <= k; ++i)
        {
            scanf("%d%d",&x,&y);
            g[x][y] = true;
        }
        work();
        printf("Case #%d: %d\n",T,f[n][m]);
    }    
    return 0;
}
