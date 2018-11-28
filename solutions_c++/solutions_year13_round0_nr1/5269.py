#include <iostream>
#include <fstream>
using namespace std;
ifstream fin;
ofstream fout;
int tCase;
int currCase;
char** board;

void globInit(char** argv);
void dumpBoard();
void readIn();
int win();//0 = not complete, 1 = x win, 2 = o win, 3 = draw
void output(int state);
int main(int argc, char* argv[]){
    globInit(argv);
    for(currCase = 0; currCase < tCase; currCase++){
        readIn();
        output(win());
        //dumpBoard();
    }
}
void output(int state){
    cout << "Case #"<<currCase+1 <<": ";
    switch(state){
        case 0: cout << "Game has not completed"<< endl;
                break;
        case 1: cout <<"X won"<< endl;
                break;
        case 2: cout << "O won"<< endl;
                break;
        case 3: cout << "Draw" << endl;
                break;
    }
}
int win(){//0 = not complete, 1 = x win, 2 = o win, 3 = draw
    int countX = 0; int countO = 0; int countT = 0;
    for(int row = 0; row < 4; row ++){
        for(int col = 0; col < 4; col ++){
            if(board[row][col] == 'X'){
                countX ++;
            }else if(board[row][col] == 'O'){
                countO ++;
            }
            else if(board[row][col] == 'T'){
                countT ++;
            }
        }
        if(countX + countT > 3) return 1;
        if(countO + countT > 3) return 2;
        countX = 0;
        countO = 0;
        countT = 0;
    }
    for(int col = 0; col < 4; col ++){
        for(int row = 0; row < 4; row ++){
            if(board[row][col] == 'X'){
                countX ++;
            }
            else if(board[row][col] == 'O'){
                countO ++;
            }
            else if(board[row][col] == 'T'){
                countT ++;
            }
        }
        if(countX + countT > 3) return 1;
        if(countO + countT > 3) return 2;
        countX = 0;
        countO = 0;
        countT = 0;
    }
    for(int row = 0; row < 4; row ++){
        if(board[row][row] == 'X'){
            countX++;
        }else if(board[row][row] == 'O'){
            countO ++;
        }
        else if(board[row][row] == 'T'){
            countT ++;
        }
    }
    //cerr << "diag check. x: " << countX << " o: " << countO << " t: " << countT << endl; 
    if(countX + countT > 3) return 1;
    if(countO + countT > 3) return 2;
    countX = 0;
    countO = 0;
    countT = 0;
    for(int row = 0; row < 4; row ++){
        if(board[row][3 - row] == 'X'){
            countX++;
        }else if(board[row][3 - row] == 'O'){
            countO ++;
        }
        else if(board[row][3 - row] == 'T'){
            countT ++;
        }
    }
    //cerr << "rev diag check. x: " << countX << " o: " << countO << " t: " << countT << endl; 
    if(countX + countT > 3) return 1;
    if(countO + countT > 3) return 2;
    countX = 0;
    countO = 0;
    countT = 0;
   /* if(board[0][1] == 'X' && board[1][2] == 'X' && board[2][3] == 'X'){
        return 1;
    }
    if(board[0][1] == 'O' && board[1][2] == 'O' && board[2][3] == 'O'){
        return 2;
    }
    if(board[1][0] == 'X' && board[2][1] == 'X' && board[3][2] == 'X'){
        return 1;
    }
    if(board[1][0] == 'O' && board[2][1] == 'O' && board[3][2] == 'O'){
        return 2;
    }
    if(board[0][2] == 'X' && board[1][1] == 'X' && board[2][0] == 'X'){
        return 1;
    }
    if(board[0][2] == 'O' && board[1][1] == 'O' && board[2][0] == 'O'){
        return 2;
    }
    if(board[1][3] == 'X' && board[2][2] == 'X' && board[3][1] == 'X'){
        return 1;
    }
    if(board[1][3] == 'O' && board[2][2] == 'O' && board[3][1] == 'O'){
        return 2;
    }*/
    for(int row = 0; row < 4; row ++){
        for(int col = 0; col < 4; col ++){
            if(board[row][col] == '.')
                return 0;
        }
    }
    return 3;
}
void globInit(char** argv){
    fin.open(argv[1]);
    fin >> tCase;
    board = new char*[4];
    for(int i = 0;i < 4; i ++){
        board[i] = new char[4];
    }
}
void readIn(){
    for(int row = 0; row < 4; row ++){
        for(int col = 0; col < 4; col ++){
            fin >> board[row][col];
        }
    }
}
void dumpBoard(){
    for(int i = 0; i < 4; i ++){
        for(int j = 0; j < 4; j ++){
            cout << board[i][j];
        }
        cout << endl;
    }
    cout << endl;
}
