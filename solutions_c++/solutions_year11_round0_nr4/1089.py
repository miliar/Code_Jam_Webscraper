#include <stdio.h>
int main(){
    int nt;
    int aux;
    scanf("%d",&nt);
    for(int i=1;i<=nt;i++){
        int d;
        scanf("%d",&d);
        int cont;
        cont = 0;
        for(int j =1;j<=d;j++){
            scanf("%d",&aux);
            if( aux!= j){
                cont++;
            }
        }
        
        printf("Case #%d: %d.000000\n",i,cont);
    }
    return 0;
}
