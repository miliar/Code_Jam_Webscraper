#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

int main(){
    int b[1200];
    int o[1200];
    int g[3000];
    char c[1200];
    int i,j,k,t,m,n,oo,bb,gg,po, pb,ggg,bbb,ooo;
    int qtt;
    char aux;
    
    scanf("%d", &t);
    int cas = 1;
    while(t--){
        memset(b,0,sizeof(b));
        memset(o,0,sizeof(o));        
        qtt = oo = bb = gg = 0;
        pb =  po = 1;
        scanf("%d", &n);
        for( i =0; i <n; i++ ){
            scanf(" %c %d", &aux, &k);
            if( aux == 'O' ) {
                o[oo++] = k;
            } else {
                b[bb++] = k;
            }
            c[gg] = aux;
            g[gg++] = k;
        }
        qtt = 0;
        ooo = bbb = ggg = 0;
        int ok;
        while( ggg != n ){
            ok = 0;
            //printf("%d %d %d\n", pb,po,ggg);
            qtt++;
            if( pb > b[bbb] ) pb--;
            else if( pb < b[bbb] ) pb++;
            else if( c[ggg] == 'B' && b[bbb] == g[ggg] ) {
                ggg++;
                bbb++;
                ok= 1;
            }
            if( po > o[ooo] ) po--;
            else if( po < o[ooo] ) po++;
            else if( ok == 0 && c[ggg] == 'O' && o[ooo] == g[ggg] ) {
                ggg++;
                ooo++;
            }
        }
        printf("Case #%d: %d\n", cas++, qtt);
    }
    
    
    
}
