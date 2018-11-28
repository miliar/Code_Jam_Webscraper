#include <cstdio>
#include <string>

using namespace std;

const int MAX_SIZE = 4 + 4;

typedef char Board[MAX_SIZE][MAX_SIZE];

int counts[] = {4, 4, 2};

char getByRow(Board board, int i, int j) {
  return board[i][j];
}

char getByCol(Board board, int i, int j) {
  return board[j][i];
}

char getByDiag(Board board, int i, int j) {
  if (i == 0) {
    return board[j][j];
  }
  return board[j][3 - j];
}

typedef char (*GetChar)(Board, int, int);

GetChar getters[] = {getByRow, getByCol, getByDiag};

bool checkLine(Board board, char player, int type) {
  for (int i = 0; i < counts[type]; ++i) {
    bool win = true;
    for (int j = 0; j < 4; ++j) {
      if (getters[type](board, i, j) != player && getters[type](board, i, j) != 'T') {
        win = false;
        break;
      }
    }
    if (win) {
      return true;
    }
  }
  return false;
}

string gameOutcome(char board[MAX_SIZE][MAX_SIZE]) {
  for (int i = 0; i < 3; ++i) {
    if (checkLine(board, 'X', i)) {
      return "X won";
    }
    if (checkLine(board, 'O', i)) {
      return "O won";
    }
  }
  bool hasEmpty = false;
  for (int i = 0; i < 4; ++i) {
    if (count(board[i], board[i] + 4, '.')) {
      hasEmpty = true;
      break;
    }
  }
  return hasEmpty ? "Game has not completed" : "Draw";
}

int main() {
  int T;
  scanf("%d\n", &T);
  Board board;
  for (int t = 0; t < T; ++t) {
    for (int i = 0; i < 4; ++i) {
      scanf("%s\n", board[i]);
    }
    printf("Case #%d: %s\n", t + 1, gameOutcome(board).c_str());
  }
}
