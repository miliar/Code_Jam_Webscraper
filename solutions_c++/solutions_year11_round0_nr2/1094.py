#include <stdio.h>
char cadena[1000];
int pos;
int icad;
char comb[100][3];
int C;
char dead[100][2];
int D;

int main(){
    int ntest;
    scanf("%d",&ntest);
    char aux;
    for(int t=1;t<=ntest;t++){
        printf("Case #%d: [",t);
        scanf("%d",&C);
        for(int i=0;i<C;i++){
            scanf(" %c %c %c",&comb[i][0],&comb[i][1],&comb[i][2]);
            comb[i+C][0] = comb[i][1];
            comb[i+C][1] = comb[i][0];
            comb[i+C][2] = comb[i][2];
        }
        C += C;
        scanf("%d",&D);
        for(int i=0;i<D;i++){
            scanf(" %c %c",&dead[i][0],&dead[i][1]);
            dead[i+D][0] = dead[i][1];
            dead[i+D][1] = dead[i][0];
        }
        D += D;
        scanf("%d",&icad);
        pos = 0;
        for(int i=0;i<icad;i++){
            scanf(" %c",&aux);
            cadena[pos] = aux;
            pos++;
            cadena[pos] = 0;
            if(pos >= 2){
                for(int j=0;j<C;j++){
                    if( comb[j][0] == cadena[pos-1] &&
                        comb[j][1] == cadena[pos-2]){
                        cadena[pos-2] = comb[j][2];
                        pos--;
                        cadena[pos] = 0;
                    }
                }
                for(int j=0;j<D;j++){
                    int paux = 0;
                    while( paux < pos && cadena[paux] != dead[j][0]){
                        paux++;
                    }
                    if( paux < pos){
                        paux++;
                    }
                    while( paux < pos && cadena[paux] != dead[j][1]){
                        paux++;
                    }
                    if( paux < pos){
                        pos = 0;
                        cadena[0] = 0;
                    }
                    
                }
            }
        }
        if(pos > 0){
            printf("%c",cadena[0]);
            for(int j=1;j<pos;j++){
                printf(", %c",cadena[j]);
            }
        }
        printf("]\n");
    }
    return 0;
}
