#include <stdio.h>

int c[10000];

int main() {
    int tt,TT,X,d,s,n,i;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d",&n);
        X = 0;
        d = 100000000;
        s = 0;
        for( i=0; i<n; i++ ) {
            scanf("%d",&c[i]);
            X^=c[i];
            if(c[i]<d) d = c[i];
            s+=c[i];
        }
        if(X==0) {
            printf("Case #%d: %d\n",tt+1,s-d);
        }else {
            printf("Case #%d: NO\n",tt+1);
        }
    }
    return 0;
}
