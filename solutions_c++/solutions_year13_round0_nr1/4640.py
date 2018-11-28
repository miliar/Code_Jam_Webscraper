#include <iostream>
#include <fstream>

using namespace std;

const int BOARD_SIZE = 4;
const char TOMEK = 'T';
const char XO[] = {'X', 'O'};

char board[BOARD_SIZE][BOARD_SIZE];

int *countR(int row, char c);
int *countC(int col, char c);
int *countDiagLR(char c);
int *countDiagRL(char c);

int main(){
    ifstream cin("input.txt");
    ofstream cout("output.txt");

    int nC;
    cin >> nC;

    for (int c = 1; c <= nC; c++){
        bool hasDots = false;
        bool winnerFound = false;

        // Read board
        for (int i = 0; i < BOARD_SIZE; i++){
            for (int j = 0; j < BOARD_SIZE; j++){
                cin >> board[i][j];
                if (board[i][j] == '.'){
                    hasDots = true;
                }
            }
        }

        char winner;

        for (int i = 0; i < 2 && !winnerFound; i++){
            for (int k = 0; k < BOARD_SIZE; k++){
                int *count = countR(k, XO[i]);
                if (count[0] == 4 || (count[0] == 3 && count[1] == 1)){
                    winnerFound = true;
                    winner = XO[i];
                    delete[] count;
                    break;
                }
                delete[] count;
                if (!winnerFound){
                    count = countC(k, XO[i]);
                    if (count[0] == 4 || (count[0] == 3 && count[1] == 1)){
                        winnerFound = true;
                        winner = XO[i];
                        delete[] count;
                        break;
                    }
                    delete[] count;
                }
            }
        }

        if (!winnerFound){
            for (int i = 0; i < 2 && !winnerFound; i++){
                int *count = countDiagLR(XO[i]);
                if (count[0] == 4 || (count[0] == 3 && count[1] == 1)){
                    winnerFound = true;
                    winner = XO[i];
                    delete[] count;
                    break;
                }
                delete[] count;

                if (!winnerFound){
                    count = countDiagRL(XO[i]);
                    if (count[0] == 4 || (count[0] == 3 && count[1] == 1)){
                        winnerFound = true;
                        winner = XO[i];
                        delete[] count;
                        break;
                    }
                    delete[] count;
                }
            }
        }

        if (winnerFound){
            cout << "Case #" << c << ": " << winner << " won" << endl;
        }
        else{
            if (hasDots){
                cout << "Case #" << c << ": Game has not completed" << endl;
            }
            else cout << "Case #" << c << ": Draw" << endl;
        }

    }
    return 0;
}


int *countR(int row, char c){
    int *ret = new int[2];
    ret[0] = ret[1] = 0;
    for (int i = 0; i < BOARD_SIZE; i++){
        if (board[row][i] == c){
            ret[0]++;
        }
        else if(board[row][i] == TOMEK){
            ret[1]++;
        }
    }
    return ret;
}

int *countC(int col, char c){
    int *ret = new int[2];
    ret[0] = ret[1] = 0;
    for (int i = 0; i < BOARD_SIZE; i++){
        if (board[i][col] == c){
            ret[0]++;
        }
        else if (board[i][col] == TOMEK){
            ret[1]++;
        }
    }
    return ret;
}

int *countDiagLR(char c){
    int *ret = new int[2];
    ret[0] = ret[1] = 0;
    for (int i = 0; i < BOARD_SIZE; i++){
        if (board[i][i] == c){
            ret[0]++;
        }
        else if (board[i][i] == TOMEK){
            ret[1]++;
        }
    }
    return ret;
}

int *countDiagRL(char c){
    int *ret = new int[2];
    ret[0] = ret[1] = 0;
    for (int i = 0; i < BOARD_SIZE; i++){
        if (board[i][BOARD_SIZE-1-i] == c){
            ret[0]++;
        }
        else if (board[i][BOARD_SIZE-1-i] == TOMEK){
            ret[1]++;
        }
    }
    return ret;
}
