#include <stdio.h>
#include <algorithm>
using namespace std;
int c[10][10];
int a[10000], an;
int b[10000];
int x[10], y[10];
int p[10], u[10];
int n, ans;
void pd(int x, int m){
    int i, j;
    if (x > n){
        if (m <= ans){
            return;
        }
        for (i = 0; i < an; i++){
            x = 0;
            for (j = 1; j <= n; j++){
                if (a[i] & (1<<j)){
                    x |= 1<<p[j];
                }
            }
            if (x + 1 != 1<<m){
                return;
            }
        }
        ans = m;
        for (i = 1; i <= n; i++){
            u[i] = p[i] + 1;
        }
    }
    else{
        for (i = 0; i < m; i++){
            p[x] = i;
            pd(x + 1, m);
        }
        p[x] = m;
        pd(x + 1, m + 1);
    }
}
void dfs(int f, int x, int dfn){
    int i, j;
    u[x] = 1;
    p[dfn] = x;
    for (i = 1; i <= n; i++){
        if (c[x][i] && i != f){
            if (u[i]){
                a[an] = (1<<i);
                for (j = dfn; p[j] != i; j--){
                    a[an] |= (1<<p[j]);
                }
                for (j = 0; j < an; j++){
                    if (a[j] == a[an]){
                        break;
                    }
                }
                if (j == an){
                    b[an] = 1;
                    an++;
                }
            }
            else{
                dfs(x, i, dfn + 1);
            }
        }
    }
    u[x] = 0;
}
int main(){
    int T, m, i, j, ri = 1;
    freopen("C-small-attempt0 (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d", &n, &m);
        an = 0;
        for (i = 0; i < m; i++){
            scanf("%d", &x[i]);
        }
        for (i = 0; i < m; i++){
            scanf("%d", &y[i]);
        }
        for (i = 1; i <= n; i++){
            u[i] = 0;
            for (j = 1; j <= n; j++){
                c[i][j] = 0;
            }
        }
        for (i = 1; i < n; i++){
            c[i][i + 1] = 1;
            c[i + 1][i] = 1;
        }
        c[1][n] = c[n][1] = 1;
        for (i = 0; i < m; i++){
            c[x[i]][y[i]] = c[y[i]][x[i]] = 1;
        }
        dfs(-1, 1, 0);
        for (i = 0; i < an; i++){
            for (j = 0; j < an; j++){
                if (i != j && (a[i] | a[j]) == a[i]){
                    b[i] = 0;
                }
            }
        }
        for (i = 0; b[i] == 0; i++);
        a[0] = a[i];
        j = 1;
        for (i++; i < an; i++){
            if (b[i]){
                a[j++] = a[i];
            }
        }
        an = j;
        ans = 2;
        p[1] = 0;
        pd(2, 1);
        printf("Case #%d: %d\n", ri++, ans);
        for (i = 1; i < n; i++){
            printf("%d ", u[i]);
        }
        printf("%d\n", u[i]);
    }
    return 0;
}
