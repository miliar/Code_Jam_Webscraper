#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <algorithm>
using namespace std;

string board[4];

//process game board
string solve(){
    int emptyCount = 0;

    //check rows

    for (int i = 0; i < 4; i++){
        int Xs = 0;
        int Os = 0;

        for (int j = 0; j < 4; j++){
            if (board[i][j] == 'X'){
                Xs++;
            }
            else if(board[i][j] == 'O'){
                Os++;
            }
            else if(board[i][j] == 'T'){
                Xs++;
                Os++;
            }
            else if(board[i][j] == '.'){
                emptyCount++;
            }
        }

        if (Xs == 4){
            return "X won";
        }
        else if(Os == 4){
            return "O won";
        }
    }
    //cout << "Rows checked." << endl;
    //check columns

    for (int i = 0; i < 4; i++){
        int Xs = 0;
        int Os = 0;

        for (int j = 0; j < 4; j++){
            if (board[j][i] == 'X'){
                Xs++;
            }
            else if(board[j][i] == 'O'){
                Os++;
            }
            else if(board[j][i] == 'T'){
                Xs++;
                Os++;
            }
            else if(board[j][i] == '.'){
                emptyCount++;
            }
        }

        if (Xs == 4){
            return "X won";
        }
        else if(Os == 4){
            return "O won";
        }
    }

    //cout << "Cols checked." << endl;

    //check diagonal left to right

    int Xs = 0;
    int Os = 0;

    for (int i = 0; i < 4; i++){
        if(board[i][i] == 'X'){
            Xs++;
        }
        else if (board[i][i] == 'O'){
            Os++;
        }
        else if(board[i][i] == 'T'){
            Xs++;
            Os++;
        }
        else if(board[i][i] == '.'){
            emptyCount++;
        }
    }

    if (Xs == 4){
        return "X won";
    }
    else if(Os == 4){
        return "O won";
    }

    //cout << "Diag 1 checked." << endl;

    Xs = 0;
    Os = 0;

    //check diagonal right to left
    for (int i = 0; i < 4; i++){
        if(board[i][3 - i] == 'X'){
            Xs++;
        }
        else if (board[i][3 - i] == 'O'){
            Os++;
        }
        else if(board[i][3 - i] == 'T'){
            Xs++;
            Os++;
        }
        else if(board[i][3 - i] == '.'){
            emptyCount++;
        }
    }

    if (Xs == 4){
        return "X won";
    }
    else if(Os == 4){
        return "O won";
    }

    //no winner found

    if (emptyCount == 0){
        return "Draw";
    }
    else{
        return "Game has not completed";
    }
}

int main(){

    ifstream in("A-large.in");
    ofstream out("A-large.out");

    int T;
    in >> T;

    int caseNumber;

    for (caseNumber = 1; caseNumber <= T; caseNumber++){

        //input for test case
        for (int i = 0; i < 4; i++){
            in >> board[i];
            //cout << board[i] << endl;
        }

        //output
        out << "Case #" << caseNumber << ": " << solve() << endl;
    }

    in.close();
    out.close();

    return 0;
}
