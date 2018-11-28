#include<iostream>
#include<vector>

using namespace std;

void solve(int testcase){
    vector<string> board(4);
    for(int i=0; i < 4; ++i){
        cin >> board[i];
    }
    bool founddot = false, linex = false, lineo = false;
    for(int i=0; i < 4; ++i){
        // Row i, column i
        bool rowx = true, rowo = true, colx = true, colo = true;
        for(int j=0; j < 4; ++j){
            if(rowx && (board[i][j] != 'X' && board[i][j] != 'T')){
                rowx = false;
            }
            if(rowo && (board[i][j] != 'O' && board[i][j] != 'T')){
                rowo = false;
            }
            if(colx && (board[j][i] != 'X' && board[j][i] != 'T')){
                colx = false;
            }
            if(colo && (board[j][i] != 'O' && board[j][i] != 'T')){
                colo = false;
            }
            if(!founddot && board[i][j]=='.'){
                founddot = true;
            }
        }
        if(rowx || colx){
            linex = true;
        }
        if(rowo || colo){
            lineo = true;
        }
    }
    // Diagonals
    bool diag1x = true, diag2x = true, diag1o = true, diag2o = true;
    for(int i=0; i<4; ++i){
        if(diag1x && (board[i][i] != 'X' && board[i][i] != 'T')){
            diag1x = false;
        }
        if(diag1o && (board[i][i] != 'O' && board[i][i] != 'T')){
            diag1o = false;
        }
        if(diag2x && (board[i][3-i] != 'X' && board[i][3-i] != 'T')){
            diag2x = false;
        }
        if(diag2o && (board[i][3-i] != 'O' && board[i][3-i] != 'T')){
            diag2o = false;
        }
    }
    cout << "Case #" << testcase << ": ";
    if(linex || diag1x || diag2x){
        cout << "X won\n";
        return;
    }
    if(lineo || diag1o || diag2o){
        cout << "O won\n";
        return;
    }
    if(founddot){
        cout << "Game has not completed\n";
    }
    else{
        cout << "Draw\n";
    }
}

int main(){
    int T; cin >> T;
    for (int i = 0; i < T; i++) {
        solve(i+1);
    }
    return 0;
}
