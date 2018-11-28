#include <stdio.h>

int main() {
    freopen("out.txt", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for(int v=1; v<=ca; v++) {
        int n,k;
        scanf("%d%d", &n, &k);
        n = (1<<n);
        if((k+1)%n == 0) printf("Case #%d: ON\n", v);
        else printf("Case #%d: OFF\n", v);
    }
    return 0;
}
