#include <stdio.h>

using namespace std;

char mapa[10][10];
int t;

int main(){
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        bool termina=false;
        bool chosto=false;
        printf("Case #%d: ",i);
        for(int j=1;j<5;j++){
            for(int k=1;k<5;k++){
                scanf(" %c",&mapa[j][k]);
                if(mapa[j][k]=='.')
                    termina=true;
            }
        }
        for(int j=1;j<=4;j++){
            if((mapa[j][1]=='X'||mapa[j][1]=='T')&&(mapa[j][2]=='X'||mapa[j][2]=='T')&&(mapa[j][3]=='X'||mapa[j][3]=='T')&&(mapa[j][4]=='X'||mapa[j][4]=='T')){
                printf("X won\n");
                chosto=true;
                break;
            }
            if((mapa[j][1]=='O'||mapa[j][1]=='T')&&(mapa[j][2]=='O'||mapa[j][2]=='T')&&(mapa[j][3]=='O'||mapa[j][3]=='T')&&(mapa[j][4]=='O'||mapa[j][4]=='T')){
                printf("O won\n");
                chosto=true;
                break;
            }
            if((mapa[1][j]=='X'||mapa[1][j]=='T')&&(mapa[2][j]=='X'||mapa[2][j]=='T')&&(mapa[3][j]=='X'||mapa[3][j]=='T')&&(mapa[4][j]=='X'||mapa[4][j]=='T')){
                printf("X won\n");
                chosto=true;
                break;
            }
            if((mapa[1][j]=='O'||mapa[1][j]=='T')&&(mapa[2][j]=='O'||mapa[2][j]=='T')&&(mapa[3][j]=='O'||mapa[3][j]=='T')&&(mapa[4][j]=='O'||mapa[4][j]=='T')){
                printf("O won\n");
                chosto=true;
                break;
            }
        }
        if(!chosto){
            if((mapa[1][1]=='X'||mapa[1][1]=='T')&&(mapa[2][2]=='X'||mapa[2][2]=='T')&&(mapa[3][3]=='X'||mapa[3][3]=='T')&&(mapa[4][4]=='X'||mapa[4][4]=='T')){
                printf("X won\n");
                chosto=true;
            }
            if((mapa[1][1]=='O'||mapa[1][1]=='T')&&(mapa[2][2]=='O'||mapa[2][2]=='T')&&(mapa[3][3]=='O'||mapa[3][3]=='T')&&(mapa[4][4]=='O'||mapa[4][4]=='T')){
                printf("O won\n");
                chosto=true;
            }
            if((mapa[1][4]=='X'||mapa[1][4]=='T')&&(mapa[2][3]=='X'||mapa[2][3]=='T')&&(mapa[3][2]=='X'||mapa[3][2]=='T')&&(mapa[4][1]=='X'||mapa[4][1]=='T')){
                printf("X won\n");
                chosto=true;
            }
            if((mapa[1][4]=='O'||mapa[1][4]=='T')&&(mapa[2][3]=='O'||mapa[2][3]=='T')&&(mapa[3][2]=='O'||mapa[3][2]=='T')&&(mapa[4][1]=='O'||mapa[4][1]=='T')){
                printf("O won\n");
                chosto=true;
            }
        }
            if(!chosto){
                if(!termina){
                    printf("Draw\n");
                }else{
                    printf("Game has not completed\n");
                }
            }
    }
    return 0;
}
