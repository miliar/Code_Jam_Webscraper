#include<cstring>
#include<cstdio>
#include<iostream>

using namespace std;

int main(){
    int T;
    scanf("%d\n",&T);
    for(int n=1; n<=T; n++){
        char tableOL[4][5],tableOC[4][5],tableXL[4][5],tableXC[4][5],dX[2][5],dO[2][5];
        bool vazio = false;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                char c;
                scanf("%c",&c);
                if(c=='T'){
                    tableOL[i][j] = 'O';
                    tableXL[i][j] = 'X';
                    tableOC[j][i] = 'O';
                    tableXC[j][i] = 'X';
                }
                else tableOL[i][j] = tableXL[i][j] = tableOC[j][i] = tableXC[j][i] = c;
                if(c=='.') vazio = true;

                if(i==3) tableOC[j][4] = tableXC[j][4] = '\0';

                if(i==j){
                    dO[0][i] = tableOL[i][j];
                    dX[0][i] = tableXL[i][j];
                }
                if((i+j)==3){
                    dO[1][i] = tableOL[i][j];
                    dX[1][i] = tableXL[i][j];
                }
            }
            tableOL[i][4] = tableXL[i][4] = '\0';

            scanf("\n");
        }
        dO[0][4] = dO[1][4] = dX[0][4] = dX[1][4] = '\0';
        scanf("\n");

        int winner=-1;
        if(!strcmp(dO[0],"OOOO") || !strcmp(dO[1],"OOOO")) winner = 1;
        if(!strcmp(dX[0],"XXXX") || !strcmp(dX[1],"XXXX")) winner = 2;

        for(int i=0; i<4 && winner<0; i++){
            if(!strcmp(tableOL[i],"OOOO") || !strcmp(tableOC[i],"OOOO"))
                winner = 1;
            if(!strcmp(tableXL[i],"XXXX") || !strcmp(tableXC[i],"XXXX"))
                winner = 2;
        }
        printf("Case #%d: ",n);
        if(winner > 0){
            printf("%c won\n",(winner==1)? 'O':'X');
        }
        else{
            if(vazio){
                printf("Game has not completed\n");
            }
            else{
                printf("Draw\n");
            }
        }
//        for(int i=0; i<4; i++) printf("%s\n",tableXL[i]); printf("\n");
//        for(int i=0; i<4; i++) printf("%s\n",tableXC[i]); printf("\n");
    }
    return 0;
}
