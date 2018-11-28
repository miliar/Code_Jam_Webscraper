#include<stdio.h>

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    int c, k, n, cc;
    
    scanf("%d", &cc);
    
    for(c=1; c<=cc; c++){
        scanf("%d%d", &n, &k);
        if(k%(1<<n)==(1<<n)-1) printf("Case #%d: ON\n", c);
        else printf("Case #%d: OFF\n", c);
    }
    
    return 0;    
}
