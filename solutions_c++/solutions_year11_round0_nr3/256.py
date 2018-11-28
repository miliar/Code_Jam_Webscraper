#include <stdio.h>
#include <string.h>
int a[1<<20][2];
int b[1<<20][2];
int main(){
    int T, n, i, p, x, s, ri = 1;
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d", &T);
    while (T--){
        memset(a, -1, sizeof(a));
        a[0][0] = 0;
        memset(b, -1, sizeof(b));
        b[0][0] = 0;
        scanf("%d", &n);
        p = s = 0;
        while (n--){
            scanf("%d", &x);
            p ^= x;
            s += x;
            for (i = 0; i < (1<<20); ++i){
                if (a[i][0] >= 0 && b[i ^ x][0] < a[i][0] + x){
                    b[i ^ x][1] = b[i ^ x][0];
                    b[i ^ x][0] = a[i][0] + x;
                }
                else if (a[i][0] >= 0 && b[i ^ x][1] < a[i][0] + x){
                    b[i ^ x][1] = a[i][0] + x;
                }
                if (a[i][1] >= 0 && b[i ^ x][0] < a[i][1] + x){
                    b[i ^ x][1] = b[i ^ x][0];
                    b[i ^ x][0] = a[i][1] + x;
                }
                else if (a[i][1] >= 0 && b[i ^ x][1] < a[i][1] + x){
                    b[i ^ x][1] = a[i][1] + x;
                }
            }
            for (i = 0; i < (1<<20); ++i){
                a[i][0] = b[i][0];
                a[i][1] = b[i][1];
            }
        }
        x = -1;
        for (i = 0; i < (1<<20); ++i){
            if (i == (p ^ i) && (a[i][0] > x && a[i][0] < s)){
                x = a[i][0];
            }
            else if (i == (p ^ i) && (a[i][1] > x && a[i][1] < s)){
                x = a[i][1];
            }
        }
        printf("Case #%d: ", ri++);
        if (x < 0){
            printf("NO\n");
        }
        else{
            printf("%d\n", x);
        }
    }
    return 0;
}
