#include <stdio.h>
#include <string.h>
using namespace std;

int f[1000][100];
char s[110];
char se[100][110];
int n, m;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int cases;  scanf("%d", &cases);
    for (int tc = 1; tc <= cases; tc++){
        scanf("%d", &n); getchar();
        for (int i = 0; i < n; i++) gets(se[i]);
        scanf("%d", &m); getchar();
        if (m == 0){ printf("Case #%d: %d\n", tc, 0); continue; }
        gets(s);
        for (int j = 0; j < n; j++)
            if (!strcmp(s, se[j])) f[0][j] = 10000; else f[0][j] = 0;
        for (int i = 1; i < m; i++){
            gets(s);   
            for (int j = 0; j < n; j++){
                f[i][j] = 10000;
                if (!strcmp(s, se[j])) continue;
                f[i][j] = f[i-1][j];
                for (int k = 0; k < n; k++) if (k != j)
                    if (f[i-1][k] + 1 < f[i][j]) f[i][j] = f[i-1][k] + 1;
            }
        }
        int ans = 10000;
        for (int j = 0; j < n; j++)
            if (f[m-1][j] < ans) ans = f[m-1][j];
        printf("Case #%d: %d\n", tc, ans);
    }
    
    return 0;   
}
