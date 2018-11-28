#include <iostream>

using namespace std;

// Game
// ==== 
//
// 4x4 tic tac toe; 'X' vs 'O'
// 
// 'X' starts.
// 
// Goal
// ====
// 
// 4 in a row (row, col or diag), or 3 in a row and the 'T'
// symbol.
//
// Problem
// =======
//
// Decide the winner given a configuration.

enum Result {
  X_WON, O_WON, DRAW, NOT_FINISHED
};

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {


    char board [4][4];   // the board as given from input
    int empty = 0;       // number of empty characters on the board
    
    // Fill the board
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        char c;
        cin >> c;
        board[i][j] = c;
        empty += (c == '.');
      }
    }

    // Process the board
    //
    // - 'X' or 'O' won
    // - Game not yet finished
    // - Game finished with a draw

    Result res = DRAW;
    int diag_xs0 = 0, diag_xs1 = 0;
    int diag_os0 = 0, diag_os1 = 0;
    
    for (int i = 0; i < 4; ++i) {
      //
      // Accumulate diagonals
      //
      diag_xs0 += ((board[i][i] == 'X') || (board[i][i] == 'T'));
      diag_xs1 += ((board[i][4-i-1] == 'X') || (board[i][4-i-1] == 'T'));
      
      diag_os0 += ((board[i][i] == 'O') || (board[i][i] == 'T'));
      diag_os1 += ((board[i][4-i-1] == 'O') || (board[i][4-i-1] == 'T'));
      
      //
      // Process row / column
      //
      int row_xs = 0, col_xs = 0;
      int row_os = 0, col_os = 0;
      
      for (int j = 0; j < 4; ++j) {
        row_xs += ((board[i][j] == 'X') || (board[i][j] == 'T'));
        col_xs += ((board[j][i] == 'X') || (board[j][i] == 'T'));
        
        row_os += ((board[i][j] == 'O') || (board[i][j] == 'T'));
        col_os += ((board[j][i] == 'O') || (board[j][i] == 'T'));
      }
      
      if ((row_xs == 4) || (col_xs == 4)) {
        res = X_WON;
        goto output_result;
      }
      if ((row_os == 4) || (col_os == 4)) {
        res = O_WON;
        goto output_result;
      }
    }
    //
    // Check for diagonal winners
    //
    if ((diag_xs0 == 4) || (diag_xs1 == 4)) {
      res = X_WON;
      goto output_result;
    }
    if ((diag_os0 == 4) || (diag_os1 == 4)) {
      res = O_WON;
      goto output_result;
    }

    //
    // There is no winner yet, so check if it's a draw
    // 
    if (empty == 0) {
      // no empty square and no winner, so it's a draw
      res = DRAW;
    } else {
      // there are still empty squares
      res = NOT_FINISHED;
    }
    
  output_result:
    cout << "Case #" << t << ": ";
    switch (res) {
    case X_WON:
      cout << "X won\n";
      break;
    case O_WON:
      cout << "O won\n";
      break;
    case DRAW:
      cout << "Draw\n";
      break;
    default:
      cout << "Game has not completed\n";
      break;
    }
  }
  
  return 0;
}
