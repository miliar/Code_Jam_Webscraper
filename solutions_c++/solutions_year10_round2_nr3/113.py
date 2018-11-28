#include <cstdio>

const int MAX = 510;
const int MOD = 100003;

int f[MAX][MAX]={};
int ans[MAX]={};
    //已经取了i个数,然后需要第j个有效
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.out","w",stdout);
    f[0][1] = 1;
    for (int n = 2; n < MAX; ++n)
        for (int i = n-1; i >= 0; --i)
            for (int j = MAX-1; j > i; --j){
                if (!f[i][j]) continue;
                if (i+1 == j){
                    f[i+1][n] = (f[i+1][n]+f[i][j])%MOD;
                    ans[n] = (ans[n]+f[i][j])%MOD;
                }
                else f[i+1][j] = (f[i+1][j]+f[i][j])%MOD;
            }
    int n, t, cas = 0;
    scanf("%d", &t);
    while (t--){
        scanf("%d", &n);
        printf("Case #%d: %d\n", ++cas, ans[n]);
    }
    return 0;
}
