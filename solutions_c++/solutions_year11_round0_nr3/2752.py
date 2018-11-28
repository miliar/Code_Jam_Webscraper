#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxsize = 1 << 21;
const int maxn = 1005;
int f[maxsize],g[maxsize],q[maxsize],b[maxsize];
int c[maxn];

int main()
{
    freopen("C.in","r",stdin);
    //freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int casenum=1; casenum<=T; ++casenum){
        int n;
        scanf("%d",&n);
        int tmp = 0,sum = 0;
        for (int i=1; i<=n; ++i){
            scanf("%d",&c[i]);
            tmp = tmp ^ c[i];
            sum += c[i];
        }
        if (tmp){
            printf("Case #%d: NO\n",casenum);
            continue;
        }
        memset(f,0,sizeof(f));
        int num = 1;
        q[1] = 0;
        int ans = 0;
        for (int i=1; i<=n; ++i){
            int t = 0;
            memcpy(g,f,sizeof(f));
            for (int j=1; j<=num; ++j)
                if (f[q[j]] + c[i] > g[q[j] ^ c[i]]){
                    if (g[q[j] ^ c[i]] == 0)
                        b[++t] = q[j] ^ c[i];
                    g[q[j] ^ c[i]] = f[q[j]] + c[i];
                }
            for (int j=1; j<=t; ++j)
                q[++num] = b[j];
            memcpy(f,g,sizeof(g));
        }
        for (int i=1; i<=num; ++i)
            if (f[q[i]] > ans && f[q[i]] != sum) ans = f[q[i]];
        printf("Case #%d: %d\n",casenum,ans);
    }
    return 0;
}
