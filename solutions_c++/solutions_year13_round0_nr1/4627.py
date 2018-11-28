#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int T, full, i, j, winner;
char b[4][4];

int checkWinner() {
    /*  This function returns the winner of the game:
        0 => There is no winner
        1 => Xs have won
        2 => Os have won
    */

    // Information of the board:
    int rowX[4] = {0,0,0,0}; // number of Xs in row i
    int colX[4] = {0,0,0,0}; // number of Xs in col i
    int diagX[2] = {0,0};    // number of Xs in diag i
    int rowO[4] = {0,0,0,0}; // number of Os in row i
    int colO[4] = {0,0,0,0}; // number of Os in col i
    int diagO[2] = {0,0};    // number of Os in diag i

    // We fill the information of the board:
    for(i=0; i<4; ++i) {
        for(j=0; j<4; ++j) {
            if( b[i][j]=='X' || b[i][j]=='T' ) {
                ++rowX[i];
                ++colX[j];
                if(i==j) ++diagX[0]; // if it's in the main diagonal
                if(i+j==3) ++diagX[1]; // if it's in the counter-diagonal
            }
            if( b[i][j]=='O' || b[i][j]=='T' ) {
                ++rowO[i];
                ++colO[j];
                if(i==j) ++diagO[0]; // if it's in the main diagonal
                if(i+j==3) ++diagO[1]; // if it's in the counter-diagonal
            }
        }
    }

    // We select a winner:
    for(i=0; i<2; ++i) {
        if(diagX[i]==4) return 1;
        if(diagO[i]==4) return 2;
    }
    for(i=0; i<4; ++i) {
        if(rowX[i]==4 || colX[i]==4) return 1;
        if(rowO[i]==4 || colO[i]==4) return 2;
    }
    return 0;
}

int main() {
    cin >> T; // number of test cases
    for(int t=1; t<=T; ++t) { // for each test case:
        cout << "Case #" << t << ": "; // we print this thing
        full = true; // we assume board is full

        // we read the board
        for(i=0; i<4; ++i)
            for(j=0; j<4; ++j) {
                cin >> b[i][j];
                if( b[i][j]=='.' ) full = false; // if there is a '.', it is not full
            }

        int winner = checkWinner(); // we find the winner

        // we print the winner
        if(winner) {
            if(winner==1) cout << "X won";
            else cout << "O won";
        }
        else if(full) cout << "Draw";
        else cout << "Game has not completed";
        cout << endl;
    }
    return 0;
}