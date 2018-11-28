#include <stdio.h>
#include <stdlib.h>

int n, m, a, x1, y1, x2, y2, x3, y3;

int Area(){
    return  abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2);
}

int solve(){
    for ( x1 = 0; x1 <= n; ++ x1 ){
            for ( y1 = 0; y1 <= m; ++ y1 ){
                for ( x2 = x1; x2 <= n; ++ x2 ){
                    for ( y2 = 0; y2 <= m; ++ y2 ){
                        if ( x1 == x2 && y1 == y2 ){
                            continue;
                        }
                        for ( x3 = x2; x3 <= n; ++ x3 ){
                            for ( y3 = 0; y3 <= m; ++ y3 ){
                                if ( (x1 == x3 && y1 == y3) || (x2 == x3 && y2 == y3) ){
                                    continue;
                                }
                                if ( Area() == a ){
                                    printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
                                    return 1;
                                }
                            }
                        }
                    }
                }
            }
    }
    return 0;
}

int main(){
    int t, ti;
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &t);
    for ( ti = 1; ti <= t ; ++ ti ){
        scanf("%d%d%d", &n, &m, &a);
        
        printf("Case #%d: ", ti);
        if ( n * m < a ){
            printf("IMPOSSIBLE\n");
            continue;
        }
        if ( !solve() ){
            printf("IMPOSSIBLE\n");
        }
        
    }
    return 0;
}
