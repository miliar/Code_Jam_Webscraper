#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    char board[4][4];
    for (int j = 0; j < 4; ++j) {
      string input;
      cin >> input;
      for (int k = 0; k < 4; ++k) {
        board[j][k] = input[k];
      }
    }
    bool x_won = false;
    bool o_won = false;
    int diag_x_count = 0;
    int diag_o_count = 0;
    int diag_t_count = 0;
    int diag2_x_count = 0;
    int diag2_o_count = 0;
    int diag2_t_count = 0;
    int dot_count = 0;
    for (int j = 0; j < 4; ++j) {
      if (board[j][j] == 'X') {
        diag_x_count++;
      }
      if (board[j][j] == 'O') {
        diag_o_count++;
      }
      if (board[j][j] == 'T') {
        diag_t_count++;
      }
      if (board[j][3 - j] == 'X') {
        diag2_x_count++;
      }
      if (board[j][3 - j] == 'O') {
        diag2_o_count++;
      }
      if (board[j][3 - j] == 'T') {
        diag2_t_count++;
      }
      int x_count = 0;
      int o_count = 0;
      int t_count = 0;
      for (int k = 0; k < 4; ++k) {
        if (board[j][k] == 'X') {
          x_count++;
        }
        if (board[j][k] == 'O') {
          o_count++;
        }
        if (board[j][k] == 'T') {
          t_count++;
        }
        if (board[j][k] == '.') {
          dot_count++;
        }
      }
      if ((x_count + t_count) == 4) {
        x_won = true;
      }
      if ((o_count + t_count) == 4) {
        o_won = true;
      }
      x_count = 0;
      o_count = 0;
      t_count = 0;
      for (int k = 0; k < 4; ++k) {
        if (board[k][j] == 'X') {
          x_count++;
        }
        if (board[k][j] == 'O') {
          o_count++;
        }
        if (board[k][j] == 'T') {
          t_count++;
        }
      }
      if ((x_count + t_count) == 4) {
        x_won = true;
      }
      if ((o_count + t_count) == 4) {
        o_won = true;
      }
    }
    if ((diag_x_count + diag_t_count) == 4) {
      x_won = true;
    }
    if ((diag_o_count + diag_t_count) == 4) {
      o_won = true;
    }
    if ((diag2_x_count + diag2_t_count) == 4) {
      x_won = true;
    }
    if ((diag2_o_count + diag2_t_count) == 4) {
      o_won = true;
    }
    if (x_won) {
      cout << "Case #" << i << ": X won" << endl;
    }
    if (o_won) {
      cout << "Case #" << i << ": O won" << endl;
    }
    if (!x_won && !o_won && (dot_count == 0)) {
      cout << "Case #" << i << ": Draw" << endl;
    }
    if (!x_won && !o_won && (dot_count > 0)) {
      cout << "Case #" << i << ": Game has not completed" << endl;
    }
  }
  return 0;
}
