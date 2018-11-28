#include<stdio.h>
#include<string.h>
#include<math.h>
double const eps = 1e-12;
int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int C, N, M, A;
    scanf("%d", &C);
    for ( int nc = 1 ; nc <= C ; ++nc ) {
        scanf("%d%d%d", &N, &M, &A);
        
        
        // output
        printf("Case #%d: ", nc);
        // ......
        //printf("%d %d %d\n", N, M, A);
        int flag = 0;
        for ( int ax = 0 ; ax <= N && flag==0; ++ax ) for ( int ay = 0 ; ay <= M&& flag==0 ; ++ay ) {
            for ( int bx = 0 ; bx <= N&& flag==0 ; ++bx ) for ( int by = 0 ; by <= M&& flag==0 ; ++by ) {
                double l1 = sqrt((ax-bx)*(ax-bx)+(ay-by)*(ay-by));
                double l2 = sqrt(ax*ax+ay*ay);
                double l3 = sqrt(bx*bx+by*by);
                double h = (l1+l2+l3)*0.5;
                double s = sqrt(h*(h-l1)*(h-l2)*(h-l3));
                double e = s - A*0.5;
                if ( e < eps && e > -eps ) {
                    flag = 1;
                    printf("%d %d %d %d %d %d\n", 0, 0, ax, ay, bx, by);
                }
            }
        }
        
        if ( flag == 0 ) {
            printf("IMPOSSIBLE\n");
        }
        
    }
}

