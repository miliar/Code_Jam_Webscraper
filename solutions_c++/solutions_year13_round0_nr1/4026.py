#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>

using namespace std;

char board[4][4];

bool win(char a){
    for (int i = 0; i < 4; i++){
        bool won = true;
        
        for ( int j = 0; j < 4; j++){
            if ( board[i][j] != a && board[i][j] != 'T' ){
                won = false;
                break;
            }
        }
        
        if ( won ){
            return true;
        }
    }
    
    for (int i = 0; i < 4; i++){
        bool won = true;
        
        for ( int j = 0; j < 4; j++){
            if ( board[j][i] != a && board[i][j] != 'T' ){
                won = false;
                break;
            }
        }
        
        if ( won ){
            return true;
        }
    }
    
    bool won = true;
    
    for (int i =0; i < 4; i++){
        if ( board[i][i] != a && board[i][i] != 'T'){
            won = false;
            break;
        }
    }
    
    if (won){
        return true;
    }
    
    for (int i =0; i < 4; i++){
        if ( board[3-i][i] != a && board[3-i][i] != 'T'){
            return false;
        }
    }
    
    return true;
    
}

int main(){
    
    int N;
    int round = 1;
    ifstream in("test.in.txt");
    ofstream out("Tic-Tac-Toe-Tomek.out");
    in >> N;
    
    while (round <= N){
        bool done = true;
        
        for (int i = 0; i < 4; i++){
            for ( int j = 0; j < 4; j++){
                in >> board[i][j];
                if (board[i][j] == '.'){
                    done = false;
                }
            }
        }
        if (win('X')){
            out << "Case #" << round << ": X won\n";
        }
        else if (win('O')){
            out << "Case #" << round << ": O won\n";
        }
        else if (!done){
            out << "Case #" << round << ": Game has not completed\n";
        }
        else 
            out << "Case #" << round << ": Draw\n";
        
        round++;
        
    }
    
    return 0;
    
}
