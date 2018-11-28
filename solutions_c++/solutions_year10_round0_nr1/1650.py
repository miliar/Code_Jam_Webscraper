#include <stdio.h>
int main(){
    int rep, ri, n, k;
    freopen("123.in", "r", stdin);
    freopen("123.out", "w", stdout);
    scanf("%d", &rep);
    for (ri = 1; ri <= rep; ri++){
        scanf("%d%d", &n, &k);
        printf("Case #%d: ", ri);
        if ((k + 1) % (1<<n) == 0){
            printf("ON\n");
        }
        else{
            printf("OFF\n");
        }
    }
    return 0;
}
