#include <stdio.h>

int main() {

  int n;

  scanf("%d", &n);

  char board[5][5];

  for (int _k = 0; _k < n; _k++) {
    bool xWin = false;
    bool oWin = false;

    bool hasEmpty = false;

    for (int i = 0; i < 4; i++) {
      scanf("%s", board[i]);

      bool allO = true;
      bool allX = true;
      for (int j = 0; j < 4; j++) {
        if (board[i][j] == 'T') {
          continue;
        }
        allO = allO && board[i][j] == 'O';
        allX = allX && board[i][j] == 'X';

        hasEmpty = hasEmpty || board[i][j] == '.';
      }

      xWin = xWin || allX;
      oWin = oWin || allO;
    }

    bool diagO = true;
    bool diagX = true;
    bool diagO2 = true;
    bool diagX2 = true;
    for (int i = 0; i < 4; i++) {
      bool allO = true;
      bool allX = true;
      for (int j = 0; j < 4; j++) {
        if (board[j][i] == 'T') {
          continue;
        }
        allO = allO && board[j][i] == 'O';
        allX = allX && board[j][i] == 'X';
      }
      xWin = xWin || allX;
      oWin = oWin || allO;

      if (board[i][i] != 'T') {
        diagO = diagO && board[i][i] == 'O';
        diagX = diagX && board[i][i] == 'X';
      }

      if (board[i][3 - i] != 'T') {
        diagO2 = diagO2 && board[i][3 - i] == 'O';
        diagX2 = diagX2 && board[i][3 - i] == 'X';
      }
    }

    xWin = xWin || diagX || diagX2;
    oWin = oWin || diagO || diagO2;

    printf("Case #%d: ", _k + 1);

    if (xWin) {
      if (oWin) {
        fprintf(stderr, "UNEXPECTED FAIL");
      } else {
        printf("X won\n");
      }
    } else {
      if (oWin) {
        printf("O won\n");
      } else {
        if (hasEmpty) {
          printf("Game has not completed\n");
        } else {
          printf("Draw\n");
        }
      }
    }
  }

  return 0;
}
