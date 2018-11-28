#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <cstring>
using namespace std;

//function declaraions


int main(){

    string fname = "large";
    freopen((fname+".in").c_str(), "r", stdin);
    freopen((fname+".out").c_str(), "w", stdout); //------- needed to output to file

    //number of cases to follow
    int cases;
    scanf("%d", &cases);

    for (int i = 1; i <= cases; ++i) {
        //values about each case

        // individual problem data
        char board[4][5];
        for (int j = 0;j<4;++j){
            scanf("%s",&board[j]);
        }
        // logic

        int numBoard[4][4] = {};

        for(int aa = 0;aa<4;aa++){
            for(int bb = 0;bb<4;bb++){
                if (board[aa][bb] == '.'){
                    numBoard[aa][bb] = 0;
                }else if(board[aa][bb] == 'O'){
                    numBoard[aa][bb] = 1;
                }else if(board[aa][bb] == 'X'){
                    numBoard[aa][bb] = 2;
                }else if(board[aa][bb] == 'T'){
                    numBoard[aa][bb] = 3;
                }
            }
        }

        int winner = 0;
        //0 - draw
        //1 - O
        //2 - X
        //3 - not finished

        for(int it = 0; it<4; it++){
            //horizontal
            int pa,pb,pc,pd,padtot;

            pa = numBoard[it][0];
            pb = numBoard[it][1];
            pc = numBoard[it][2];
            pd = numBoard[it][3];
            padtot = pa*pb*pc*pd;
            if(padtot == 16 || padtot == 24){
                winner = 2;
                break;
            }else if(padtot == 1 || padtot == 3){
                winner = 1;
                break;
            }
            //hacky buuut who cares
            //vertical
            pa = numBoard[0][it];
            pb = numBoard[1][it];
            pc = numBoard[2][it];
            pd = numBoard[3][it];
            padtot = pa*pb*pc*pd;
            if(padtot == 16 || padtot == 24){
                winner = 2;
                break;
            }else if(padtot == 1 || padtot == 3){
                winner = 1;
                break;
            }
        }

        //diagonals
        int pa,pb,pc,pd,padtot;
        pa = numBoard[0][0];
        pb = numBoard[1][1];
        pc = numBoard[2][2];
        pd = numBoard[3][3];
        padtot = pa*pb*pc*pd;
        if(padtot == 16 || padtot == 24){
            winner = 2;
        }else if(padtot == 1 || padtot == 3){
            winner = 1;
        }

        pa = numBoard[3][0];
        pb = numBoard[2][1];
        pc = numBoard[1][2];
        pd = numBoard[0][3];
        padtot = pa*pb*pc*pd;
        if(padtot == 16 || padtot == 24){
            winner = 2;
        }else if(padtot == 1 || padtot == 3){
            winner = 1;
        }

        if(winner == 0){
            for(int ll = 0; ll<4;ll++){
                for(int mm = 0; mm<4;mm++){
                    if (board[ll][mm] == '.'){
                        winner = 3;
                    }
                }
            }
        }


/*
        //winning positions
        //horizontal
        board[0][0] == board[0][1] == board[0][2] == board [0][3];
        board[1][0] == board[1][1] == board[1][2] == board [1][3];
        board[2][0] == board[2][1] == board[2][2] == board [2][3];
        board[3][0] == board[3][1] == board[3][2] == board [3][3];
        //vertical
        board[0][0] == board[1][0] == board[2][0] == board [3][0];
        board[0][1] == board[1][1] == board[2][1] == board [3][1];
        board[0][2] == board[1][2] == board[2][2] == board [3][2];
        board[0][3] == board[1][3] == board[2][3] == board [3][3];
        //diagonal
        board[0][0] == board[1][1] == board[2][2] == board [3][3];
        board[0][3] == board[1][2] == board[2][1] == board [3][0];

  */



        // answer
        string winners[4] = {"Draw","O won","X won","Game has not completed"};
        printf("Case #%d: ", i);
        cout<<winners[winner]<<endl;

    }

    return 0;
}
