#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 2000;
const int maxp = 15;
const int inf = 2147483647/2;
int cost[maxn*2],m[maxn*2];
int f[maxn*2][maxp];

int main()
{
    freopen("B.in","r",stdin); freopen("B.out","w",stdout);
    int t; scanf("%d",&t);
    for (int casenum=1; casenum<=t; ++casenum){
        int p; scanf("%d",&p);
        int n = 1 << p;
        for (int i=0; i<n; ++i)
            scanf("%d",&m[i]);
        for (int i=p-1; i>=0; --i){
            int st = 1 << i; st--;
            int m = 1 << i;
            for (int j=st; j< st + m; ++j)
                scanf("%d",&cost[j]);
        }
        int total = 1 << p; total--;
        for (int i=maxn*2-1; i>=0; --i)
            for (int j=0; j<maxp; ++j)
                f[i][j] = inf;
        for (int i=0; i<n; ++i){
            int k = (1 << p) - 1 + i;
            for (int j=p; j> m[i]; --j)
                f[k][j] = inf;
            for (int j=m[i]; j>=0; --j)
                f[k][j] = 0;
        }
       /* for (int j=n-2; j>=0; --j)
            printf("%d ",cost[j]); */
        for (int i=n-2; i>=0; --i)
            for (int j=0; j<=p; ++j){
                f[i][j] = inf;
                int lch = i*2+1, rch = i*2+2;
                if (j + 1 <= p && f[lch][j+1] != inf && f[rch][j+1] != inf)
                    f[i][j] = min(f[i][j], f[lch][j+1] + f[rch][j+1]);
                if (f[lch][j] != inf && f[rch][j] != inf)
                    f[i][j] = min(f[i][j], f[lch][j] + f[rch][j] + cost[i]);
            }
        int ans = inf;
        for (int j=0; j<=p; ++j)
            ans = min(ans,f[0][j]);
        printf("Case #%d: %d\n",casenum,ans);
    }
    return 0;
}
