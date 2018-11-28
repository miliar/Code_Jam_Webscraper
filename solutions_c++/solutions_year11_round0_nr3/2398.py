#include<cstdio>

int c[1005];

int main() {
    int ntc;
    scanf("%d", &ntc);
    for( int TC = 1; TC <= ntc; TC++ ) {
        int N, nxor = 0, sum = 0, nmin = 10000000;
        scanf("%d", &N);
        for( int i=0, x; i<N; i++ ) {
            scanf("%d", &x);
            nxor = nxor ^ x;
            sum = sum + x;
            nmin = ( nmin > x ) ? x : nmin;
        }
        printf("Case #%d: ", TC);
        if ( nxor == 0 ) printf("%d\n", sum - nmin );
        else printf("NO\n");
    }
    return 0;
}
