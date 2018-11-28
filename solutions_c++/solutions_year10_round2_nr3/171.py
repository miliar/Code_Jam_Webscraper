#include <stdio.h>
long long a[510][510];
long long ans[510];
int f[510];
long long c[510][510];
int main(){
    int rep, ri, n, i, j, k;
    freopen("aaa.in", "r", stdin);
    freopen("aaa.txt", "w", stdout);
    a[1][0] = 1;
    for (i = 1; i < 501; i++){
        for (j = 1; j < 100003; j++){
            if ((i * j) % 100003 == 1){
                f[i] = j;
                break;
            }
        }
    }
    c[0][0] = 1;
    for (i = 1; i < 510; i++){
        c[i][0] = 1;
        for (j = 1; j <= i; j++){
            c[i][j] = ((c[i][j - 1] * (i - j + 1)) % 100003 * f[j]) % 100003;
        }
    }
    for (i = 1; i < 510; i++){
        a[i][1] = 1;
    }
    for (i = 2; i < 501; i++){
        for (j = 2; j < i; j++){
            k = 2 * j - i;
            if (k < 0){
                k = 0;
            }
            for (; k < j; k++){
                a[i][j] = (a[i][j] + (a[j][k] * c[i - j - 1][j - k - 1]) % 100003) % 100003;
            }
        }
    }
    for (i = 1; i < 501; i++){
        for (j = 0; j <= i; j++){
            ans[i] = (ans[i] + a[i][j]) % 100003;
        }
    }
    scanf("%d", &rep);
    for (ri = 1; ri <= rep; ri++){
        scanf("%d", &n);
        printf("Case #%d: %d\n", ri, ans[n]);
    }
    return 0;
}
