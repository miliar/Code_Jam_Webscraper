#include <iostream>

#define STATE_INCOMPLETE 0
#define STATE_X_WON 1
#define STATE_O_WON 2
#define STATE_DRAW 3

int checkFour(char row[4]) {
  bool seenX, seenO;
  seenX = seenO = false;

  for (int i = 0; i < 4; i++) {
    switch (row[i]) {
      case 'X':
        seenX = true;
        break;
      case 'O':
        seenO = true;
        break;
      case '.':
        return STATE_INCOMPLETE;
    }
  }

  // given that the row is complete, it's either a draw or someone won
  if (seenX && seenO) {
    return STATE_DRAW;
  } else if (seenX) {
    return STATE_X_WON;
  } else {
    return STATE_O_WON;
  }
}

int getGameState(char board[4][4]) {
    int complete = true;

    // check the rows
    for (int i = 0; i < 4; i++) {
      int state = checkFour(board[i]);
      switch (state) {
        case STATE_INCOMPLETE:
          // no result from this row, and the board is incomplete
          complete = false;
          break;
        case STATE_X_WON:
          return state;
        case STATE_O_WON:
          return state;
      }
    }

    // check the columns
    for (int j = 0; j < 4; j++) {
      char row[4];
      row[0] = board[0][j]; row[1] = board[1][j]; row[2] = board[2][j]; row[3] = board[3][j];
      int state = checkFour(row);
      if (state == STATE_X_WON || state == STATE_O_WON) return state;
    }

    // check the top-left to bottom-right diagonal
    char diag[4];
    for (int i=0; i < 4; i++) {
      diag[i] = board[i][i];
    }
    int state = checkFour(diag);
    if (state == STATE_X_WON || state == STATE_O_WON) return state;

    // check the top-right to bottom-left diagonal
    for (int i=0; i < 4; i++) {
      diag[i] = board[i][3-i];
    }
    state = checkFour(diag);
    if (state == STATE_X_WON || state == STATE_O_WON) return state;

    // all checks complete and no winner.  it's either a draw or incomplete.
    if (complete) {
      return STATE_DRAW;
    }

    return STATE_INCOMPLETE;
}

int main (int argc, char *argv[]) {
  int num_tests;

  std::cin >> num_tests;

  for (int t = 1; t <= num_tests; t++) {
    char board[4][4];
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        std::cin >> board[i][j];
      }
    }

    int state = getGameState(board);
    std::cout << "Case #" << t << ": ";
    switch (state) {
      case STATE_X_WON:
        std::cout << "X won";
        break;
      case STATE_O_WON:
        std::cout << "O won";
        break;
      case STATE_DRAW:
        std::cout << "Draw";
        break;
      case STATE_INCOMPLETE:
        std::cout << "Game has not completed";
    }

    std::cout << std::endl;
  }
}
