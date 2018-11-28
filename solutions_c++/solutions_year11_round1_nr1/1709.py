#include <cstdio>
#include <cstdlib>

int main(){
    int i,k,aux;
    int n,m,d,g,t;
    
    scanf("%d", &t);
    for( k =1; k <=t; k++){
        scanf("%d %d %d", &n, &d, &g);
        if( d == 0 ){
            if( g != 100 ) printf("Case #%d: Possible\n", k);
            else printf("Case #%d: Broken\n", k);
        }else {
            if( g == 0 ) printf("Case #%d: Broken\n", k);
            else {
                if( d != 100 && g == 100 ) {
                    printf("Case #%d: Broken\n", k);
                }else {
                    aux = 100;
                    for( i = 2; i <= 100; i++){
                        while( ((aux)%i) == 0 && ((d)%i) == 0 ){
                            aux/=i;
                            d/=i;
                        }
                    }
                    if( aux <= n ) printf("Case #%d: Possible\n", k);
                    else printf("Case #%d: Broken\n", k);
                }
            }
        }
    }
}
