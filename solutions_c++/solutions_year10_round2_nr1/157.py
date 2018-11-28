#include <stdio.h>
#include <string.h>
char c[210][10010];
int main(){
    int rep, ri, n, m, i, j, k, t, l, ans;
    freopen("aaa.in", "r", stdin);
    freopen("aaa.txt", "w", stdout);
    scanf("%d", &rep);
    for (ri = 1; ri <= rep; ri++){
        ans = 0;
        scanf("%d%d", &n, &m);
        for (i = 0; i < n; i++){
            scanf("%s", c[i]);
            l = strlen(c[i]);
            c[i][l] = '/';
            c[i][l + 1] = 0;
        }
        for (j = n; j < m + n; j++){
            scanf("%s", c[j]);
            l = strlen(c[j]);
            c[j][l] = '/';
            c[j][l + 1] = 0;
            l = 1;
            for (i = 0; i < j; i++){
                t = 0;
                for (k = 0; c[i][k] && c[j][k]; k++){
                    if (c[i][k] != c[j][k]){
                        break;
                    }
                    if (c[i][k] == '/'){
                        t++;
                    }
                }
                if (t > l){
                    l = t;
                }
            }
            t = 0;
            for (k = 0; c[j][k]; k++){
                if (c[j][k] == '/'){
                    t++;
                }
            }
            ans += t - l;
        }
        printf("Case #%d: %d\n", ri, ans);
    }
    return 0;
}
