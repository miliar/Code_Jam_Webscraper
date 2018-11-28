#include <stdio.h>

int T;
char A[10][10];

bool isWinner(char c) {
  for (int i = 0; i < 4; i++) {
    bool vert = true;
    bool oriz = true;
    for (int j = 0; j < 4; j++) {
      if (A[i][j] != c && A[i][j] != 'T') {
        oriz = false;
      }

      if (A[j][i] != c && A[j][i] != 'T') {
        vert = false;
      }
    } 

    if (vert || oriz) {
      return true;
    }
  }

  bool princ = true;
  bool secund = true;
  for (int i = 0; i < 4; i++) {
    if (A[i][i] != c && A[i][i] != 'T') {
      princ = false;
    }

    if (A[i][3-i] != c && A[i][3-i] != 'T') {
      secund = false;
    }
  }

  return princ || secund;
}

// Works iff is not a winner.
bool isDraw() {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (A[i][j] == '.') {
        return false;
      }
    }
  }

  return true;
}

const char* solve() {
  if (isWinner('X')) { return "X won";}
  if (isWinner('O')) { return "O won";}
  if (isDraw()) { return "Draw"; }
  return "Game has not completed";
}

int main() {
  scanf("%d", &T);
  for (int i = 0; i < T; ++i) {
    scanf("%s\n", A[0]);
    scanf("%s\n", A[1]);
    scanf("%s\n", A[2]);
    scanf("%s\n", A[3]);
    scanf("\n");
    printf("Case #%d: %s\n", i+1, solve());
  }

  return 0;
}
