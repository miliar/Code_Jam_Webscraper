#include <cstdio>
int main(){
    int casos, cX, cO, cT, cP, swX, swO;
    char mapa[5][5];
    scanf("%d",&casos);
    for( int i=1; i<=casos; i++){
        //lectura y filas
        cP = swX = swO = 0;
        for(int j=0;j<4;j++){
            scanf("%s", mapa[j]);
            cX=cO=cT=0;
            for(int k=0;k<4;k++){
                if( mapa[j][k]== 'X' ) cX++;
                if( mapa[j][k]== 'O' ) cO++;
                if( mapa[j][k]== 'T' ) cT++;
                if( mapa[j][k]== '.' ) cP++;
            }
            if(cX == 4 || cX+cT == 4) swX = 1;
            if(cO == 4 || cO+cT == 4) swO = 1;
        }
        if(swX || swO){
            if(swX) printf("Case #%d: X won\n", i);
            else printf("Case #%d: O won\n", i);
        }else{
            //columnas
            for(int j=0;j<4;j++){
                cX=cO=cT=0;
                for(int k=0;k<4;k++){
                    if( mapa[k][j]== 'X')cX++;
                    if( mapa[k][j]== 'O')cO++;
                    if( mapa[k][j]== 'T')cT++;
                }
                if(cX == 4 || cX+cT == 4) swX = 1;
                if(cO == 4 || cO+cT == 4) swO = 1;
            }
            if(swX || swO){
                if(swX)printf("Case #%d: X won\n", i);
                else printf("Case #%d: O won\n", i);
            }else{
                //diagonal principal
                cX=cO=cT=0;
                for(int k=0;k<4;k++){
                    if( mapa[k][k]== 'X')cX++;
                    if( mapa[k][k]== 'O')cO++;
                    if( mapa[k][k]== 'T')cT++;
                }
                if(cX == 4 || cX+cT == 4) swX = 1;
                if(cO == 4 || cO+cT == 4) swO = 1;
                if(swX || swO){
                    if(swX)printf("Case #%d: X won\n", i);
                    else printf("Case #%d: O won\n", i);
                }else{
                    //diagonal secundaria
                    cX=cO=cT=0;
                    for(int k=0;k<4;k++){
                        if( mapa[k][3-k]== 'X')cX++;
                        if( mapa[k][3-k]== 'O')cO++;
                        if( mapa[k][3-k]== 'T')cT++;
                    }
                    if(cX == 4 || cX+cT == 4) swX = 1;
                    if(cO == 4 || cO+cT == 4) swO = 1;
    
                    if(swX || swO){
                        if(swX)printf("Case #%d: X won\n", i);
                        else printf("Case #%d: O won\n", i);
                    }else{
                        if(cP == 0)printf("Case #%d: Draw\n", i);
                        else printf("Case #%d: Game has not completed\n", i);                    
                    }
                }
            }
        }
    }
    return 0;
}
