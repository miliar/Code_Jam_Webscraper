#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

char board[4][4];

inline bool check_win(char player) {

  bool win_main = true, win_sec = true;

  for (int i = 0; i < 4; ++i) {
    bool win_row = true, win_col = true;
    for (int j = 0; j < 4 && (win_row || win_col); ++j) {
      // row
      if (board[i][j] != player && board[i][j] != 'T')
        win_row = false;
      // col
      if (board[j][i] != player && board[j][i] != 'T')
        win_col = false;
    }

    if (win_row || win_col) return true;

    // diag
    if (board[i][i] != player && board[i][i] != 'T')
      win_main = false;
    if (board[i][4 - i - 1] != player &&
        board[i][4 - i - 1] != 'T')
      win_sec = false;
  }

  return win_main || win_sec;
}

// pre use after calls to check win
inline bool check_draw() {
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      if (board[i][j] == '.')
        return false;
    }
  }
  return true;
}

void print_board() {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++)
      printf("%c", board[i][j]);
    printf("\n");
  }
}

int main(int argc, char *argv[])
{

  int ntests;
  cin >> ntests;
  scanf("\n");
  for (int t = 1; t <= ntests; t++) {

    for (int i = 0; i < 4; ++i)
      scanf("%c%c%c%c\n", &board[i][0], &board[i][1], &board[i][2], &board[i][3]);

    if (check_win('X')) {
      printf("Case #%d: %s\n", t, "X won" );
    } else if (check_win('O')) {
      printf("Case #%d: %s\n", t, "O won" );
    } else if (check_draw()) {
      printf("Case #%d: %s\n", t, "Draw");
    } else {
      printf("Case #%d: %s\n", t, "Game has not completed");
    }
  }

  return 0;
}
