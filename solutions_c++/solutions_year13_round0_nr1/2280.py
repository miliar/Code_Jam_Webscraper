#include "TicTacToeTomek.h"
#include <assert.h>
namespace {

enum State {
  XWIN,
  OWIN,
  DRAW,
  INCOMPLETE
};

bool searchRow(char board[4][4], char c, int row, int col, bool* hasEmpty) {
  assert(row < 4);
  assert(col < 4);
  char x = board[row][col];
  bool r = true;
  if (x == c || x == 'T') {
    if (col == 3) {
      return true;
    }
  } else if (x == '.') {
    *hasEmpty = true;
    if (col == 3) {
      return false;
    }
    r = false;
  } else {
    if (col == 3) {
      return false;
    }
    r = false;
  }
  
  return searchRow(board, c, row, col + 1, hasEmpty) && r;
}

bool searchCol(char board[4][4], char c, int row, int col, bool* hasEmpty) {
  assert(row < 4);
  assert(col < 4);
  char x = board[row][col];
  bool r = true;
  if (x == c || x == 'T') {
    if (row == 3) {
      return true;
    }
  } else if (x == '.') {
    *hasEmpty = true;
    if (row == 3) {
      return false;
    }
    r = false;
  } else {
    if (row == 3) {
      return false;
    }
    r = false;
  }
  return searchCol(board, c, row + 1, col, hasEmpty) && r;
}

bool searchDiag(char board[4][4], char c) {
  bool r = true, q = true;
  for (int i = 0; i < 4; ++i) {
    if (board[i][i] != c && board[i][i] != 'T') {
      r = false;
    }
    if (board[i][3 - i] != c && board[i][3 - i] != 'T') {
      q = false;
    }
  }
  return r || q;
}

const char* realSolve(char board[4][4]) {
  bool hasEmpty = false;
  for (int i = 0; i < 4; ++i) {
    bool r = searchRow(board, 'X', i, 0, &hasEmpty) ||
      searchCol(board, 'X', 0, i, &hasEmpty);
    if (r) {
      return "X won";
    }
    r = searchRow(board, 'O', i, 0, &hasEmpty) ||
      searchCol(board, 'O', 0, i, &hasEmpty);
    if (r) {
      return "O won";
    }
  }
  if (searchDiag(board, 'X')) {
    return "X won";
  } else if (searchDiag(board, 'O')) {
    return "O won";
  }
  if (hasEmpty) {
    return "Game has not completed";
  } else {
    return "Draw";
  }
}

}

namespace codejam {

void TicTacToeTomek::solve(std::ostream& output, std::istream& input) {
  int n, _n = 1;
  input >> n;
  while (_n <= n) {
    char board[4][4];
    char buf[10];
    for (int i = 0; i < 4; ++i) {
      input >> buf;
      for (int j = 0; j < 4; ++j) {
        board[i][j] = buf[j];
      }
    }
    const char* result = realSolve(board);
    output << "Case #" << _n << ": " << result << std::endl;
    _n++;
  }
}

}