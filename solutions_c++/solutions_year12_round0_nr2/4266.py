#include <cstdio>
#include <cstdlib>

int main(){
    int t,a,b,c,i,k,tot,aux;
    
    scanf("%d", &t);
    for( k =1; k <= t; k++){
        scanf("%d %d %d", &a, &b, &c);
        tot = 0;
        for( i =0; i < a; i++){
            scanf("%d", &aux);
            if((aux >= (3*c) - 2)) tot++;
            else {
                if( aux >= ((3*c) - 4) && c != 1 && b){
                    tot++;
                    b--;
                }
            }
        }
        printf("Case #%d: %d\n", k, tot);
    }
}
