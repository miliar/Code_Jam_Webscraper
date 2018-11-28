#include <algorithm>
using namespace std;

int f[10010][1010];
int n, m;
char s[1010][110];
char st[110];

int solve(){
    scanf("%d", &n); gets(st);
    for (int i = 1; i <= n; i++) gets(s[i]); 
    scanf("%d", &m); gets(st);
    if (m == 0) return 0;
    gets(st);
    
    for (int j = 1; j <= n; j++)
        if (!strcmp(st, s[j])) f[1][j] = 1; else f[1][j] = 0;
    for (int i = 2; i <= m; i++){
        gets(st);
        for (int j = 1; j <= n; j++){ 
            f[i][j] = 10000;
            if (strcmp(s[j], st))
                for (int k = 1; k <= n; k++){
                    if (k == j && f[i-1][k] < f[i][j]) f[i][j] = f[i-1][k];
                    if (k != j && f[i-1][k] + 1 < f[i][j]) f[i][j] = f[i-1][k] + 1;
                }
        }
    }
    int ret = 10000;
    for (int j = 1; j <= n; j++)
        if (f[m][j] < ret) ret = f[m][j];
    return ret;
}

int main(){
    freopen("Alarge.in", "r", stdin);
    freopen("Alarge.out", "w", stdout);
    int cases;  scanf("%d", &cases);
    for (int tc = 1; tc <= cases; tc++){    
        printf("Case #%d: %d\n", tc, solve());
    }
    return 0;   
}
