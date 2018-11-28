#include <stdio.h>
#include <math.h>
char c[100];
long long b[100];
long long x, t, s;
bool pd(long long l, long long r, long long s){
    if (l + 1 == r){
        return l * l == s;
    }
    long long z = (l + r) / 2;
    if (z * z > s){
        return pd(l, z, s);
    }
    return pd(z, r, s);
}
int main(){
    int T, ri = 1, i, j, n, l;
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%s", c);
        x = 0;
        n = 0;
        for (i = 0; c[i]; i++){
            if (c[i] == '?'){
                b[n++] = i;
                x *= 2;
            }
            else{
                x = x * 2 + c[i] - '0';
            }
        }
        l = i;
        for (i = 0; i < n; i++){
            b[i] = 1LL<<(l - b[i] - 1);
        }
        for (i = 0; i < (1<<n); i++){
            t = x;
            for (j = 0; j < n; j++){
                if (i & (1<<j)){
                    t += b[j];
                }
            }
            if (pd(0, 1LL<<31, t)){
                break;
            }
        }
        for (i = l - 1; i >= 0; i--){
            c[i] = t % 2 + '0';
            t /= 2;
        }
        printf("Case #%d: %s\n", ri++, c);
    }
    return 0;
}
