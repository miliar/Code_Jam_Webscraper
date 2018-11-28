#include <stdio.h>
long long x[60];
long long v[60];
int u[60], s[60];
int main(){
    int rep, ri, n, k, i, j, ans;
    long long b, t;
    freopen("aaa.in", "r", stdin);
    freopen("aaa.txt", "w", stdout);
    scanf("%d", &rep);
    for (ri = 1; ri <= rep; ri++){
        scanf("%d%d%lld%lld", &n, &k, &b, &t);
        for (i = 0; i < n; i++){
            scanf("%lld", &x[i]);
        }
        for (i = 0; i < n; i++){
            scanf("%lld", &v[i]);
            if (v[i] * t + x[i] >= b){
                u[i] = 0;
            }
            else{
                u[i] = 1;
            }
        }
        ans = 0;
        j = 0;
        s[n] = 0;
        for (i = n - 1; i >= 0; i--){
            s[i] = s[i + 1] + u[i];
            if (u[i] == 0){
                ans += s[i];
                j++;
                if (k == j){
                    break;
                }
            }
        }
        printf("Case #%d: ", ri);
        if (k == j){
            printf("%d\n", ans);
        }
        else{
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
