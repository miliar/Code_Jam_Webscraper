#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <iomanip>
#include <fstream>
using namespace std;

int main() {
    ifstream read;
    read.open("A-large.in");
    ofstream write;
    write.open("answer.txt");
    int caseId;
    read >> caseId;

        for(int i = 1; i <= caseId; i++){
            enum GAME {X, O, D, N};
            GAME status = D;
            //4lines
            string board[4];
            for(int j = 0; j < 4; j++){
                read >> board[j];
            }

            for(int j = 0; j < 4; j++){
                //horizon win
                int xCount = 0, oCount = 0, tCount = 0;
                for(int k = 0; k < 4; k++){
                    if(board[j][k] == 'X') xCount++;
                    else if(board[j][k] == 'O') oCount++;
                    else if(board[j][k] == 'T') tCount++;
                }
                if(xCount == 4 || (xCount == 3 && tCount == 1)){
                    status = X;
                    break;
                } else if(oCount == 4 || (oCount == 3 && tCount == 1)){
                    status = O;
                    break;
                } else if(xCount + tCount + oCount != 4){
                    status = N;
                }
                //vertical win
                xCount = 0, oCount = 0, tCount = 0;
                for(int k = 0; k < 4; k++){
                    if(board[k][j] == 'X') xCount++;
                    else if(board[k][j] == 'O') oCount++;
                    else if(board[k][j] == 'T') tCount++;
                }
                if(xCount == 4 || (xCount == 3 && tCount == 1)){
                    status = X;
                    break;
                } else if(oCount == 4 || (oCount == 3 && tCount == 1)){
                    status = O;
                    break;
                } else if(xCount + tCount + oCount != 4){
                    status = N;
                }

            }
            //cross win
            if(status == N || status == D){
                int xCount = 0, oCount = 0, tCount = 0;
                for(int j = 0; j < 4; j++){
                    if(board[j][j] == 'X') xCount++;
                    else if(board[j][j] == 'O') oCount++;
                    else if(board[j][j] == 'T') tCount++;
                }
                if(xCount == 4 || (xCount == 3 && tCount == 1)){
                    status = X;
                } else if(oCount == 4 || (oCount == 3 && tCount == 1)){
                    status = O;
                } else if(xCount + tCount + oCount != 4){
                    status = N;
                }
            }
            //another cross
            if(status == N || status == D){
                int xCount = 0, oCount = 0, tCount = 0;
                for(int j = 0; j < 4; j++){
                    if(board[j][3-j] == 'X') xCount++;
                    else if(board[j][3-j] == 'O') oCount++;
                    else if(board[j][3-j] == 'T') tCount++;
                }
                if(xCount == 4 || (xCount == 3 && tCount == 1)){
                    status = X;
                } else if(oCount == 4 || (oCount == 3 && tCount == 1)){
                    status = O;
                } else if(xCount + tCount + oCount != 4){
                    status = N;
                }
            }
            //conclusion
            write << "Case #" << i << ": ";
            switch(status){
                case X:
                    write << "X won";
                    break;
                case O:
                    write << "O won";
                    break;
                case D:
                    write << "Draw";
                    break;
                case N:
                    write << "Game has not completed";
                    break;
            }
            write << endl;
        }

    return 0;
}
