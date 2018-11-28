#include <stdio.h>

int main() {
    int tt,TT,n,i,x,s;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d",&n);
        s = 0;
        for( i=1; i<=n; i++ ) {
            scanf("%d",&x);
            if(x!=i) s++;
        }
        printf("Case #%d: %.6f\n",tt+1,(double)s);
    }
    return 0;
}
