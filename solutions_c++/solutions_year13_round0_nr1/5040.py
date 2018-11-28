#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

char m[100][100];

int main(void){

    int T;
    scanf("%d",&T);

    for(int r = 0;r < T;++r){
        bool xWon = false;
        bool oWon = false;
        bool orGameEnd = true;

        for(int row = 0;row<4;++row){
            scanf("%s",m[row]);
            //printf("%s\n",m[row]);
        }
        
        // ‚½‚Ä
        for(int i = 0;i < 4 && !xWon && !oWon;++i){
            int xval = 0;
            int oval = 0;
            for(int z = 0;z < 4 && !xWon && !oWon;++z){
                switch(m[i][z])
                {
                case 'X': ++xval; break;
                case 'O': ++oval; break;
                case 'T': ++xval; ++oval; break;
                default: orGameEnd = false;
                }
                xWon = xval >= 4;
                oWon = oval >= 4;
            }
        }

        // ‚æ‚±
        for(int i = 0;i < 4 && !xWon && !oWon;++i){
            int xval = 0;
            int oval = 0;
            for(int z = 0;z < 4 && !xWon && !oWon;++z){
                switch(m[z][i])
                {
                case 'X': ++xval; break;
                case 'O': ++oval; break;
                case 'T': ++xval; ++oval; break;
                default: orGameEnd = false;
                }
                xWon = xval >= 4;
                oWon = oval >= 4;
            }
        }

        // ‚È‚È‚ß‚P
        for(int i = 0;i < 1 && !xWon && !oWon;++i){
            int xval = 0;
            int oval = 0;
            for(int z = 0;z < 4 && !xWon && !oWon;++z){
                switch(m[z][z])
                {
                case 'X': ++xval; break;
                case 'O': ++oval; break;
                case 'T': ++xval; ++oval; break;
                default: orGameEnd = false;
                }
                xWon = xval >= 4;
                oWon = oval >= 4;
            }
        }

        // ‚È‚È‚ß‚Q
        for(int i = 0;i < 1 && !xWon && !oWon;++i){
            int xval = 0;
            int oval = 0;
            for(int z = 0;z < 4 && !xWon && !oWon;++z){
                switch(m[z][3-z])
                {
                case 'X': ++xval; break;
                case 'O': ++oval; break;
                case 'T': ++xval; ++oval; break;
                default: orGameEnd = false;
                }
                xWon = xval >= 4;
                oWon = oval >= 4;
            }
        }

        printf("Case #%d: ",r+1);
        if(xWon){
            printf("X won");
        }else if(oWon){
            printf("O won");
        }else if(orGameEnd){
            printf("Draw");
        }else{
            printf("Game has not completed");
        }
        printf("\n");
    }

}