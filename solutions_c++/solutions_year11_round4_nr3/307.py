#include <stdio.h>
int a[1010];
int p[1010], pn;
int f(int x, int p){
    int t = 0;
    while (x >= p){
        x /= p;
        t++;
    }
    return t;
}
int main(){
    int T, ri = 1, n, i, j, ans;
    freopen("C-small-attempt0 (2).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    for (i = 2; i < 1010; i++){
        if (a[i] == 0){
            p[pn++] = i;
            for (j = i; j * i < 1010; j++){
                a[i * j] = 1;
            }
        }
    }
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        printf("Case #%d: ", ri++);
        if (n == 1){
            printf("0\n");
            continue;
        }
        ans = 1;
        for (i = 0; p[i] <= n; i++){
            ans += f(n, p[i]) - 1;
        }
        printf("%d\n", ans);
    }
    return 0;
}
