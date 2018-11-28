#include <stdio.h>
#include <assert.h>

char map[4][4];

bool row (int a, int b, int da, int db, char c) {
  for (int i = 0; i < 4; i++) {
    int x = a + i * da;
    int y = b + i * db;
    if (map[x][y] != c && map[x][y] != 'T') {
      return false;
    }
  }
  return true;
}

bool hasWon (char c) {
  int a[] = {0, 0, 0, 1, 0, 2, 0, 3,
             0, 0, 1, 0, 2, 0, 3, 0,
             0, 0, 3, 0};
  int b[] = {1, 0, 1, 0, 1, 0, 1, 0,
             0, 1, 0, 1, 0, 1, 0, 1,
             1, 1, -1, 1};
  for (int i = 0; i < 10; i++) {
    if (row(a[2*i], a[2*i+1], b[2*i], b[2*i+1], c)) {
      return true;
    }
  }
  return false;
}

bool notOver () {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (map[i][j] == '.') {
        return true;
      }
    }
  }
  return false;
}

int main (void) {
  int T;
  int scanned = scanf("%d", &T);
  for (int currentcase = 1; currentcase <= T; ++currentcase) {
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        char c;
        while ((c = getchar()) != 'X' && c != 'T' && c != '.' && c != 'O');
        map[i][j] = c;
      }
    }
    if (hasWon('X')) {
      printf("Case #%d: X won\n", currentcase);
    } else if (hasWon('O')) {
      printf("Case #%d: O won\n", currentcase);
    } else if (notOver()) {
      printf("Case #%d: Game has not completed\n", currentcase);
    } else {
      printf("Case #%d: Draw\n", currentcase);
    }
  }
  return 0;
}
