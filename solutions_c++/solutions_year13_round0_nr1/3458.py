#include<stdio.h>

int main(){

    int test;

    freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

    scanf("%d",&test);

    char board[5][5];

    for(int caseN=0;caseN<test;caseN++){

        int cond = 0;
        int isComplete = 1;

        for(int i=0;i<4;i++){
            scanf("%s",board[i]);
        }


        int dSumX = 0;
        int dSumO = 0;
        int rdSumX = 0;
        int rdSumO = 0;
        for(int i=0;i<4;i++){
            int rowSumX = 0;
            int colSumX = 0;
            int rowSumO = 0;
            int colSumO = 0;

            switch(board[i][i]){
                case 'T' : dSumO++;
                            dSumX++;break;
                case 'X' : dSumX++;
                            break;
                case 'O' : dSumO++;
                            break;
            }

//            printf(" dSum %d, rdSum %d\n",dSumX,rdSumX);
            switch(board[i][3-i]){
                case 'T' : rdSumO++;
                            rdSumX++;break;
                case 'X' : rdSumX++;
                            break;
                case 'O' : rdSumO++;
                            break;
            }

            for(int j=0;j<4;j++){
                    if(board[i][j] == 'X' || board[i][j] == 'T'){
                        rowSumX++;
                    }
                    if(board[j][i] == 'X' || board[j][i] == 'T'){
                        colSumX++;
                    }
                    if(rowSumX == 4 || colSumX == 4 || rdSumX == 4 || dSumX == 4){
                        cond = 1;
                    }

                    if(board[i][j] == 'O' || board[i][j] == 'T'){
                        rowSumO++;
                    }
                    if(board[j][i] == 'O' || board[j][i] == 'T'){
                        colSumO++;
                    }
                    if(rowSumO == 4 || colSumO == 4 || rdSumO == 4 || dSumO == 4){
                        cond = 2;
                    }

                    if(board[i][j] == '.'){
                        isComplete = 0;
                    }
            }

        }

        switch(cond){

            case 1: printf("Case #%d: X won\n",caseN+1);
                    break;
            case 2: printf("Case #%d: O won\n",caseN+1);
                    break;

            default: if(isComplete == 0){
                         printf("Case #%d: Game has not completed\n",caseN+1);
                    }
                    else{
                        printf("Case #%d: Draw\n",caseN+1);
                    }
        }


    }
}
