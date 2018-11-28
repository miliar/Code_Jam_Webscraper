#include <cstdio>
#include <cstring>
#define MAXN 1001

int T , N;
int f[MAXN][MAXN];
int g[MAXN][MAXN];
bool h[MAXN][MAXN];

int main () {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
    int i , j , k;
    scanf("%d\n",&T);
    for (int p = 1;p <= T;p++) {
        printf("Case #%d: ",p);
        memset(f,0,sizeof(f));
        memset(g,0,sizeof(g));
        memset(h,0,sizeof(h));
        scanf("%d\n",&N);
        for (i = 0;i < N;i++) {
            scanf("%d\n",&g[i][0]);
            for (j = 1;j <= g[i][0];j++) {
                scanf("%d\n",&g[i][j]);
                h[i][g[i][j]-1] = true;
                f[i][g[i][j]-1] = 1;
            }
        }
        bool flag = true;
        for (k = 0;k < N && flag;k++)
          for (i = 0;i < N && flag;i++)
            if (k != i && f[i][k])
              for (j = 0;j < N && flag;j++)
                if (i != j && j != k && f[i][k] && f[k][j]) {
                    f[i][j] ++;
                    if (f[i][j] >= 2) flag = false;
                }
        if (flag) printf("No\n");
          else printf("Yes\n");
    }
    return 0;
}
