#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

void printBoard (vector< vector<char> > &board) {

    for( int i = 0; i < board.size(); ++i) {

        for(int j = 0; j < board[i].size(); ++j) {
            cout << board[i][j] << " ";
        }

        cout << endl;
    }
}

void initBoard(vector< vector<char> > &board, ifstream &ins, bool &boardFilled) {
    boardFilled = true;

    for(int i = 0; i < board.size(); ++i) {

        for(int j = 0; j < board[i].size(); ++j) {

            ins >> board[i][j];

            if( board[i][j] == '.' ) {
                boardFilled = false;
            }

        }
    }

    //prepare for next read
    string junk;
    getline(ins, junk);
}

bool ckAcross(vector< vector<char> > &board, int startRow, int startCol, 
              char freeSpace, char direction, char &player) 
{


    if(startRow < 0 || startRow >= board.size()) {
        cerr << "startRow out of bounds in LR" << endl;
        exit(1);
    }

    player = board[startRow][startCol];

    if(player == freeSpace) {

        if(direction == 'D') {
            player = board[startRow + 1][startCol];
        }
        else if(direction == 'A') {
            player = board[startRow][startCol + 1];
        }
        else {
            cerr << "BAD direction ckA" << endl;
            exit(1);
        }
       
    }

    if(player != 'X' && player != 'O') {
        return false;
    }
    
    int row = startRow;
    int col = startCol;

    for(int i = 0; i < board.size(); ++i) {

        if( board[row][col] != player && board[row][col] != freeSpace) {
            return false;
        }

        if (direction == 'D') {
            ++row;
        }
        else if (direction == 'A') {
            ++col;
        }
        else {
            cerr << "BAD direction ckA2" << endl;
            exit(1);  
        }

    }

    return true;

}

bool ckDiag(vector< vector<char> > &board, const int startRow, const char freeSpace, 
            char direction, char &player) 
{
    if(startRow < 0 || startRow >= board.size()) {
        cerr << "startRow out of bounds in DIAG" << endl;
        exit(1);
    }

    player = board[startRow][0];

      if(player == freeSpace) {

        if(direction == 'T') {
            player = board[startRow + 1][1];
        }
        else if(direction == 'B') {
            player = board[startRow - 1][1];
        }
        else {
            cerr << "BAD direction" << endl;
            exit(1);
        }
    }

    if(player != 'X' && player != 'O') {
        return false;
    }

  

    int row = startRow;
    for(int col = 0; col < board.size(); ++col) {

        if( board[row][col] != player && board[row][col] != freeSpace) {
            return false;
        }

        if(direction == 'T') {
            ++row;
        }
        else if(direction == 'B') {
            --row;
        }
        else {
            cerr << "BAD direction2" << endl;
            exit(1);
        }

    }

    return true;

}


int main(int argc, char **argv) {

    if(argc != 2) {
        cerr << "Invalid Arguments" << endl;
        return 1;
    }

    string fileName = argv[1];

    ifstream ins;

    ins.open(fileName.c_str());

    if(!ins) {
        cerr << "Bad File Name" << endl;;
        return 1;
    }

    string junk;

    int numTests;

    ins >> numTests;
    getline(ins, junk);


    int boardSize = 4;
    char freeSpace = 'T';
    char player;
    bool boardFilled;
    

    vector< vector<char> > board(boardSize, vector<char>(boardSize, '.'));

    for(int i = 0; i < numTests; ++i) {

        bool winFound = false;
        initBoard(board, ins, boardFilled);

        cout << "Case #" << i + 1 << ": ";

        for( int i = 0; i < board.size(); ++i) {
            
            if(i == 0 ) {
                
                // cout << "TOP DIAG: " << ckDiag(board, i, freeSpace, 'T', player) << endl;
                if(ckDiag(board, i, freeSpace, 'T', player)) {
                    winFound = true;
                    cout << player << " won" << endl;
                    break;
                }

                for(int j = 0; j < board.size(); ++j) {
                    // cout << "TOP ROW " << j << ": " << ckAcross(board, 0, j, freeSpace, 'D', player) << endl;
                    if(ckAcross(board, 0, j, freeSpace, 'D', player)) {
                        winFound = true;
                        cout << player << " won" << endl;
                        break;
                    }
                }

                if(winFound) break;
            }
            
            if ( i == board.size() - 1) {
                // cout << "BOT DIAG: " << ckDiag(board, i, freeSpace, 'B', player) << endl;
                if(ckDiag(board, i, freeSpace, 'B', player)) {
                    winFound = true;
                    cout << player << " won" << endl;
                    break;
                }

            }
            
            // cout << ckAcross(board, i, 0, freeSpace, 'A', player) << endl;
            if(ckAcross(board, i, 0, freeSpace, 'A', player)) {
                winFound = true;
                cout << player << " won" << endl;
                break;
            }

        }

        if(!winFound) {
            
            if(boardFilled) {
                cout << "Draw" << endl;
            }
            else {
                cout << "Game has not completed" << endl;
            }

        }

        // printBoard(board);

        // cout << endl; 
    }
   
    

    return 0;

}













