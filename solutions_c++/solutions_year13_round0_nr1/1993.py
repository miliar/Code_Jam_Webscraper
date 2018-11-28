#include <iostream>
#include <fstream>

using namespace std;

char board[4][4];
ifstream in;
ofstream out;

void read(){
    for(int i=0; i<4; i++){
        for(int j = 0; j < 4; j++){
            in >> board[i][j];
        }
    }
}

int solve(){
    for(int i=0; i<4; i++){
        if(board[i][0]=='X' || board[i][0]=='T'){
            if((board[i][1]=='X' || board[i][1]=='T') && (board[i][2]=='X' || board[i][2]=='T') && (board[i][3]=='X' || board[i][3]=='T')){
                return 1;
            }
        }
        if(board[0][i]=='X' || board[0][i]=='T'){
            if((board[1][i]=='X' || board[1][i]=='T') && (board[2][i]=='X' || board[2][i]=='T') && (board[3][i]=='X' || board[3][i]=='T')){
                return 1;
            }
        }
        if(board[i][0]=='O' || board[i][0]=='T'){
            if((board[i][1]=='O' || board[i][1]=='T') && (board[i][2]=='O' || board[i][2]=='T') && (board[i][3]=='O' || board[i][3]=='T')){
                return 2;
            }
        }
        if(board[0][i]=='O' || board[0][i]=='T'){
            if((board[1][i]=='O' || board[1][i]=='T') && (board[2][i]=='O' || board[2][i]=='T') && (board[3][i]=='O' || board[3][i]=='T')){
                return 2;
            }
        }
        if(board[0][0]=='O' || board[0][0]=='T'){
            if((board[1][1]=='O' || board[1][1]=='T') && (board[2][2]=='O' || board[2][2]=='T') && (board[3][3]=='O' || board[3][3]=='T')){
                return 2;
            }
        }
        if(board[0][0]=='X' || board[0][0]=='T'){
            if((board[1][1]=='X' || board[1][1]=='T') && (board[2][2]=='X' || board[2][2]=='T') && (board[3][3]=='X' || board[3][3]=='T')){
                return 1;
            }
        }
        if(board[0][3]=='X' || board[0][3]=='T'){
            if((board[1][2]=='X' || board[1][2]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[3][0]=='X' || board[3][0]=='T')){
                return 1;
            }
        }
        if(board[0][3]=='O' || board[0][3]=='T'){
            if((board[1][2]=='O' || board[1][2]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[3][0]=='O' || board[3][0]=='T')){
                return 2;
            }
        }
    }

    for(int i=0; i<4; i++){
        for(int j = 0; j < 4; j++){
            if(board[i][j]=='.'){
                return 4;
            }
        }
    }
    return 3;
}

void print(int caseNumber, int solutionNumber){
    out << "Case #" << caseNumber << ": ";
    if(solutionNumber == 1){
        out << "X won" << endl;
    }
    if(solutionNumber == 2){
        out << "O won" << endl;
    }
    if(solutionNumber == 3){
        out << "Draw" << endl;
    }
    if(solutionNumber == 4){
        out << "Game has not completed" << endl;
    }
}

int main()
{
    out.open("out.txt");
    in.open("A-large.in");
    int T;
    in >> T;
    for(int i=1; i<=T; i++){
        read();
        print(i,solve());
    }
    out.close();
    in.close();
    return 0;
}
