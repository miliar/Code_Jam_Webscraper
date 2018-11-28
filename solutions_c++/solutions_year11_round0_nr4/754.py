#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(){
    int t,n,i,j,k,tot,cont;
    int num[2000];
    int ok[2000];
    scanf("%d", &t);
    for( k = 1; k <=t; k++){
        scanf("%d", &n);
        memset( ok,0,sizeof(ok));        
        for( i =1; i <=n; i++){
            scanf("%d", &num[i]);
            if( i == num[i] ) ok[i] = 1;
        }   
        tot = 0;

        for( i =1; i <= n; i++){
            
            if( !ok[i] ){
                cont = 1;
                j = num[i];
                ok[i] = 1;
                while( j != i ){
                    ok[j] = 1;
                    cont++;
                    j = num[j];
                }
                tot +=cont;
            }
        
        }
        printf("Case #%d: %d.000000\n",k, tot);
        
        
        
        
        
        
    }
}
