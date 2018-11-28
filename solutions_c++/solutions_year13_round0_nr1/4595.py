#include <stdio.h>
#include <string>

bool won(char player, char board[4][5]) {
  for (int i = 0; i < 4; i++) {
    bool row = true;
    bool column = true;
    bool diagonal_topleft = true;
    bool diagonal_bottomleft = true;
    int j;
    for (j = 0; j < 4; j++) {
      if (!(board[i][j] == player || board[i][j] == 'T')) {
        row = false;
      }
      if (!(board[j][i] == player || board[j][i] == 'T')) {
        column = false;
      }
      if (!(board[j][j] == player || board[j][j] == 'T')) {
        diagonal_topleft = false;
      }
      if (!(board[j][3-j] == player || board[j][3-j] == 'T')) {
        diagonal_bottomleft = false;
      }
    }
    if (row || column || diagonal_topleft || diagonal_bottomleft) {
      return true;
    }
  }
  return false;
}

bool draw(char board[4][5]) {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (board[i][j] == '.') {
        return false;
      }
    }
  }
  return true;
}

void Process(char board[4][5], int case_number) {
  FILE *fout = fopen("output", "a");
  fprintf(fout, "Case #%d: ", case_number);
  if (won('X', board)) {
    fprintf(fout, "X won");
  } else if (won('O', board)) {
    fprintf(fout, "O won");
  } else if (draw(board)) {
    fprintf(fout, "Draw");
  } else {
    fprintf(fout, "Game has not completed");
  }
  fprintf(fout, "\n");
  fclose(fout);
}

int main(int argc, const char *argv[]) {
  FILE *fin = fopen("input", "r");
  int T;
  fscanf(fin, "%d", &T);
  for (int test_case = 0; test_case < T; test_case++) {
    char board[4][5];
    for (int i = 0; i < 4; i++) {
      fscanf(fin, "%s", board[i]);
    }
    Process(board, test_case + 1);
  }
  fclose(fin);
  return 0;
}
