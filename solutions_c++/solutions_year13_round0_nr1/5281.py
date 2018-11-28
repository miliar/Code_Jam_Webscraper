#include <iostream>
#include <string>

using namespace std;

string
solve(char board[4][4]) {
  string result("Game has not completed");
  bool completed = true;
  bool won = false;
  
  for(int r = 0; r < 4; r++) {
    for(int c = 0; c < 4; c++) {
      if(board[r][c] == '.') {
        completed = false;
      }
    }
    
    if((board[r][0] == 'X' || board[r][0] == 'T') &&
       (board[r][1] == 'X' || board[r][1] == 'T') &&
       (board[r][2] == 'X' || board[r][2] == 'T') &&
       (board[r][3] == 'X' || board[r][3] == 'T')) {
      result = "X won";
      won = true;
      break;
    }
    if((board[0][r] == 'X' || board[0][r] == 'T') &&
       (board[1][r] == 'X' || board[1][r] == 'T') &&
       (board[2][r] == 'X' || board[2][r] == 'T') &&
       (board[3][r] == 'X' || board[3][r] == 'T')) {
      result = "X won";
      won = true;
      break;
    }
    if((board[r][0] == 'O' || board[r][0] == 'T') &&
       (board[r][1] == 'O' || board[r][1] == 'T') &&
       (board[r][2] == 'O' || board[r][2] == 'T') &&
       (board[r][3] == 'O' || board[r][3] == 'T')) {
      result = "O won";
      won = true;
      break;
    }
    if((board[0][r] == 'O' || board[0][r] == 'T') &&
       (board[1][r] == 'O' || board[1][r] == 'T') &&
       (board[2][r] == 'O' || board[2][r] == 'T') &&
       (board[3][r] == 'O' || board[3][r] == 'T')) {
      result = "O won";
      won = true;
      break;
    }
  }
  
  if(!won) {    
    if((board[0][0] == 'X' || board[0][0] == 'T') &&
       (board[1][1] == 'X' || board[1][1] == 'T') &&
       (board[2][2] == 'X' || board[2][2] == 'T') &&
       (board[3][3] == 'X' || board[3][3] == 'T')) {
      result = "X won";
      won = true;
    }
  }
  if(!won) {    
    if((board[0][3] == 'X' || board[0][3] == 'T') &&
       (board[1][2] == 'X' || board[1][2] == 'T') &&
       (board[2][1] == 'X' || board[2][1] == 'T') &&
       (board[3][0] == 'X' || board[3][0] == 'T')) {
      result = "X won";
      won = true;
    }
  }
  if(!won) {    
    if((board[0][0] == 'O' || board[0][0] == 'T') &&
       (board[1][1] == 'O' || board[1][1] == 'T') &&
       (board[2][2] == 'O' || board[2][2] == 'T') &&
       (board[3][3] == 'O' || board[3][3] == 'T')) {
      result = "O won";
      won = true;
    }
  }
  if(!won) {    
    if((board[0][3] == 'O' || board[0][3] == 'T') &&
       (board[1][2] == 'O' || board[1][2] == 'T') &&
       (board[2][1] == 'O' || board[2][1] == 'T') &&
       (board[3][0] == 'O' || board[3][0] == 'T')) {
      result = "O won";
      won = true;
    }
  }
  
  if(!won && completed) {
    result = "Draw";
  }
  
  return result;
}

int
main() {
  int T;
  cin >> T;
  
  for(int i = 1; i <=T; i++) {
    char board[4][4];
    
    for(int r = 0; r < 4; r++) {
      for(int c = 0; c < 4; c++) {
        cin >> board[r][c];
      }
    }
    
    cout << "Case #" << i << ": " << solve(board) << endl;
  }
  
  return 0;
}
