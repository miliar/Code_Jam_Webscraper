#include<iostream>
#include<cstring>

using namespace std;

int main() {
  int T, board[4][4], rowsum, colsum, diag1sum, diag2sum;
  char ch;
  bool xwon, owon, gamenotcompleted;
  
  cin >> T;
  cin.ignore(256, '\n');
  for (int trial = 1; trial <= T; ++trial) {
    gamenotcompleted = false;
    xwon = false;
    owon = false;
    for (int line = 0; line < 4; ++line) {
      for (int character = 0; character < 4; ++character) {
        cin >> ch;
        if (ch == 'X') board[line][character] = 9;
        else if (ch == 'O') board[line][character] = 1;
        else if (ch == 'T') board[line][character] = 5;
        else {
          board[line][character] = 0;
          gamenotcompleted = true;
        }
      }
      cin.ignore(256, '\n');
    }
    cin.ignore(256, '\n');
    
    diag1sum = 0;
    diag2sum = 0;
    for (int i = 0; i < 4; ++i) {
      rowsum = 0;
      colsum = 0;
      diag1sum += board[i][i];
      diag2sum += board[3-i][i];
      for (int j = 0; j < 4; ++j) {
        rowsum += board[i][j];
        colsum += board[j][i];
      }
      if (rowsum >= 32 || colsum >= 32) {
        xwon = true;
        break;
      } else if (rowsum == 4 || rowsum == 8 || colsum == 4 || colsum == 8) {
        owon = true;
        break;
      }
    }
    if (diag1sum >= 32 || diag2sum >= 32) xwon = true;
    else if (diag1sum == 4 || diag1sum == 8 || diag2sum == 4 || diag2sum == 8) owon = true;
    
    cout << "Case #" << trial << ": ";
    if (xwon) cout << "X won";
    else if (owon) cout << "O won";
    else if (gamenotcompleted) cout << "Game has not completed";
    else cout << "Draw";
    cout << endl;
  }
}
