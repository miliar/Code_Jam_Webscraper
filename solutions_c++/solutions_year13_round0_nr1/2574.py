#include <cstdio>
#include <cstring>

int t;
char matriz[5][5];
int contx,contt,conto;
int ganhou;

int main(void){

    freopen("A.in","r",stdin);

    freopen("A.out","w",stdout);

    scanf("%d",&t);

    for(int casos=1;casos<=t;casos++){

        for(int i=0;i<4;i++){
            scanf(" %s",matriz[i]);
        }
     //   scanf(" %*s");


        ganhou=-1;

        for(int i=0;i<4;i++){
            contx=0;
            contt=0;
            conto=0;
            for(int j=0;j<4;j++){
                if(matriz[i][j] == 'X') contx++;
                else if(matriz[i][j] == 'O') conto++;
                else if(matriz[i][j] == 'T') contt++;
            }
            if(contx +contt == 4){
                ganhou=1;
                break;
            }else if(conto + contt == 4){
                ganhou=0;
                break;
            }
        }

        if(ganhou == -1){
            for(int i=0;i<4;i++){
                contx=0;
                contt=0;
                conto=0;
                for(int j=0;j<4;j++){
                    if(matriz[j][i] == 'X') contx++;
                    else if(matriz[j][i] == 'O') conto++;
                    else if(matriz[j][i] == 'T') contt++;
                }
                if(contx +contt == 4){
                    ganhou=1;
                    break;
                }else if(conto + contt == 4){
                    ganhou=0;
                    break;
                }
            }
        }

        if(ganhou == -1){
                contx=0;
                contt=0;
                conto=0;
                for(int j=0;j<4;j++){
                    if(matriz[j][j] == 'X') contx++;
                    else if(matriz[j][j] == 'O') conto++;
                    else if(matriz[j][j] == 'T') contt++;
                }
                if(contx +contt == 4){
                    ganhou=1;
                }else if(conto + contt == 4){
                    ganhou=0;
                }
        }

            if(ganhou == -1){
                contx=0;
                contt=0;
                conto=0;
                for(int j=0;j<4;j++){
                    if(matriz[j][3-j] == 'X') contx++;
                    else if(matriz[j][3-j] == 'O') conto++;
                    else if(matriz[j][3-j] == 'T') contt++;
                }
                if(contx +contt == 4){
                    ganhou=1;
                }else if(conto + contt == 4){
                    ganhou=0;
                }
        }



        if(ganhou == -1){
            int cont=0;
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                    if(matriz[i][j] != '.') cont++;
                }
            }


            if(cont == 16) ganhou=2;
        }


        printf("Case #%d:",casos);
        if(ganhou == -1) printf(" Game has not completed\n");
        else if(ganhou == 2) printf(" Draw\n");
        else if(ganhou == 1) printf(" X won\n");
        else printf(" O won\n");
    }

    return 0;

}
