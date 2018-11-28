#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
#define maxn 200
vector<int>g[maxn];
int xx[maxn],yy[maxn],vv[maxn];
bool path(int p)
{
    for(int i=0,q;i<g[p].size();i++) if(!vv[q=g[p][i]]){ vv[q]=1;
        if(yy[q]==-1||path(yy[q])) { yy[q]=p; xx[p]=q; return 1; }
    }return 0;
} 
int match(int n)
{
    int ans=0; memset(xx,-1,sizeof(xx)); memset(yy,-1,sizeof(yy));
    for(int i=0;i<n;i++) if(xx[i]==-1){ memset(vv,0,sizeof(vv)); ans+=path(i); }
    return ans;
}
int p[100][25];
int main() {
  //  freopen("c.in", "r",stdin);
    int t;
    scanf("%d", &t);
    for (int kase = 1; kase <= t; ++kase) {
        int n, k,i;
        scanf("%d%d", &n, &k);
        for ( i = 0; i < n; ++i) {
            for (int j = 0; j < k; ++j) {
                scanf("%d", &p[i][j]);
            }
            g[i].clear();
        }
        for ( i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                bool ok = true;
                for (int u = 0; u < k; ++u) {
                    if (p[i][u] >= p[j][u]) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    g[i].push_back(j);
                }
            }
        }
        int ans = n-match(n);
        printf("Case #%d: %d\n", kase, ans);
    }
    return 0;
}
