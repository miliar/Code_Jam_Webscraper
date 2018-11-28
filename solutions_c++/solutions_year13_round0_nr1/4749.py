#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>
#include <string>
#include <cassert>

using namespace std;
char board[4][5];

bool check_row (char player, int row) {
  for (int i=0; i<4; i++) {
    if (!(board[row][i] == player || board[row][i] == 'T')) {
      return false;
    }
  }
  return true;
}

bool check_col (char player, int col) {
  for (int i=0; i<4; i++) {
    if (!(board[i][col] == player || board[i][col] == 'T')) {
      return false;
    }
  }
  return true;
}

bool check_diag (char player, int diag) {
  assert (diag >= 0 && diag <= 1);
  int off = 0;
  int mult = 1;
  if (diag == 1) {
    off = 3;
    mult = -1;
  }
  for (int i=0; i<4; i++) {
    if (!(board[off + mult * i][i] == player
      || board[off + mult * i][i] == 'T')) {
      return false;
    }
  }
  return true;
}

bool check (char player) {
  for (int i=0; i<4; i++) {
    if (check_row (player, i)) return true;
    if (check_col (player, i)) return true;
  }
  if (check_diag (player, 0)) return true;
  if (check_diag (player, 1)) return true;

  return false;
}

bool completed () {
  for (int i=0; i<4; i++) {
    for (int j=0; j<4; j++) {
      if (board[i][j] == '.') return false;
    }
  }
  return true;
}

int main () {
  int T;
  scanf ("%d", &T);

  for (int i=0; i<T; i++) {
    for (int j = 0; j < 4; j++) {
      scanf ("%s", board[j]);
    }

    if (check ('X')) {
      cout << "Case #" << (i + 1) << ": " << "X won" << endl;
    } else if (check ('O')) {
      cout << "Case #" << (i + 1) << ": " << "O won" << endl;
    } else if (!completed ()) {
      cout << "Case #" << (i + 1) << ": " << "Game has not completed" << endl;
    } else {
      cout << "Case #" << (i + 1) << ": " << "Draw" << endl;
    }
  }

  return 0;
}
