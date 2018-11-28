#include <stdio.h>
long long a[1010];
int u[1010];
long long s[1010];
int main(){
    int rep, ri, i, n, t, p, l;
    long long r, k, x;
    freopen("123.in", "r", stdin);
    freopen("123.out", "w", stdout);
    scanf("%d", &rep);
    for (ri = 1; ri <= rep; ri++){
        scanf("%lld%lld%d", &r, &k, &n);
        t = 0;
        for (i = 0; i < n; i++){
            scanf("%lld", &a[i]);
            s[i] = 0;
            u[i] = -1;
        }
        p = 0;
        while (1){
            if (u[p] >= 0){
                break;
            }
            u[p] = t;
            l = p;
            x = k;
            if (x >= a[p]){
                x -= a[p];
                s[t] += a[p];
                p = (p + 1) % n;
            }
            while (x >= a[p] && p != l){
                x -= a[p];
                s[t] += a[p];
                p = (p + 1) % n;
            }
            t++;
        }
        x = 0;
        if (r > t){
            for (i = u[p]; i < t; i++){
                x += s[i];
            }
            x *= (r - u[p]) / (t - u[p]);
            r = (r - u[p]) % (t - u[p]);
            for (i = 0; i < r; i++){
                x += s[i + u[p]];
            }
            for (i = 0; i < u[p]; i++){
                x += s[i];
            }
        }
        else{
            for (i = 0; i < r; i++){
                x += s[i];
            }
        }
        printf("Case #%d: %lld\n", ri, x);
    }
    return 0;
}
