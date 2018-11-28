#include <iostream>
using namespace std;

#define DIM 4

class Board {
  char board[DIM][DIM];
  bool wonRow(int row, char player);
  bool wonCol(int col, char player);
  bool wonDiag(char player);
  bool won(char player);
  bool hasDot();
public:
  Board ();
  void print ();
  void printStatus();
};

Board::Board() {
  string line;
  for (int i = 0; i < DIM; i++) {
    getline(cin, line);
    for (int j = 0; j < DIM; j++) {
      board[i][j] = line[j];
    }
  }
};

void Board::print() {
  for (int i = 0; i < DIM; i++) {
    for (int j = 0; j < DIM; j++) {
      cout << board[i][j];
    }
    cout << "\n";
  }
}

bool Board::hasDot() {
  for (int i = 0; i < DIM; i++) {
    for (int j = 0; j < DIM; j++) {
      if (board[i][j] == '.') {
	return true;
      }
    }
  }
  return false;
}

bool isPlayer(char c, char player) {
  return (c == player || c == 'T');
}

bool Board::wonRow(int row, char player) {
  bool won = true;
  char c;
  for (int j = 0; j < DIM; j++ ) {
    c = board[row][j];
    won = won && isPlayer(c, player);
  }
  return won;
}

bool Board::wonCol(int col, char player) {
  bool won = true;
  char c;
  for (int i = 0; i < DIM; i++ ) {
    c = board[i][col];
    won = won && isPlayer(c, player);
  }
  return won;
}

bool Board::wonDiag(char player) {
  bool won = true;
  char c;
  for (int i = 0; i < DIM; i++ ) {
    c = board[i][i];
    won = won && isPlayer(c, player);
  }
  if (won) {
    return won;
  } else {
    won = true;
    for (int i = 0; i < DIM; i++ ) {
      c = board[DIM-1-i][i];
      won = won && isPlayer(c, player);
    }
    return won;
  }
}

bool Board::won(char player) {
  bool won = false;
  for (int i = 0; i < DIM; i++) {
    won = won || this->wonRow(i, player) || this->wonCol(i, player);
  }
  won = won || this->wonDiag(player);
  return won;
}

void Board::printStatus() {
  if (this->won('X')) {
    cout << "X won\n";
  } else if (this->won('O')) {
    cout << "O won\n";
  } else if (this->hasDot()) {
    cout << "Game has not completed\n";
  } else {
    cout << "Draw\n";
  }
}

void oneBoard(int n) {
  Board *b;
  b = new Board();
  cout << "Case #" << n+1 << ": ";
  b->printStatus();
}

int main(int argc, char *argv[]) {
  int numBoards, n;
  string emptyLine;
  cin >> numBoards;
  getline(cin, emptyLine);
  for (n = 0; n < numBoards; n++) {
    oneBoard(n);
    getline(cin, emptyLine);
  }
}
