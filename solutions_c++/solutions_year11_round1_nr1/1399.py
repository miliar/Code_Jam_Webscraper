#include <stdio.h>

int main(){

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, n, pd, pg, i;
    scanf("%d", &t);
    for(int k=1; k<=t; k++){
        scanf("%d %d %d", &n, &pd, &pg);
        for(i=1; i<=n; i++)
            if((pd*i)%100==0) break;
        if(i>n || (pd>0 && pg==0) || (pd<100 && pg==100))
            printf("Case #%d: Broken\n", k);
        else printf("Case #%d: Possible\n", k);
    }
    return 0;
}
