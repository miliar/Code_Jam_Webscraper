#include <iostream>

using namespace std;

bool won(char T[4][5], int r0, int c0, int dr, int dc, char ch) {
  for (int r = r0, c = c0; 0 <= r && r < 4 && 0 <= c && c < 4;
      r += dr, c += dc) {
    if (T[r][c] != ch && T[r][c] != 'T') {
      return false;
    }
  }
  return true;
}

int main() {
  int n_tests;
  scanf("%d", &n_tests);
  for (int test = 1; test <= n_tests; ++test) {
    char T[4][5];
    for (int r = 0; r < 4; ++r) {
      scanf(" %s", T[r]);
    }
    bool X_won = false;
    bool O_won = false;
    for (int r = 0; r < 4 && !X_won && !O_won; ++r) {
      X_won = won(T, r, 0, 0, +1, 'X');
      O_won = won(T, r, 0, 0, +1, 'O');
    }
    for (int c = 0; c < 4 && !X_won && !O_won; ++c) {
      X_won = won(T, 0, c, +1, 0, 'X');
      O_won = won(T, 0, c, +1, 0, 'O');
    }
    if (!X_won && !O_won) {
      X_won = won(T, 0, 0, +1, +1, 'X') || won(T, 0, 3, +1, -1, 'X');
      O_won = won(T, 0, 0, +1, +1, 'O') || won(T, 0, 3, +1, -1, 'O');
    }
    if (X_won) {
      printf("Case #%d: X won\n", test);
    } else if (O_won) {
      printf("Case #%d: O won\n", test);
    } else {
      bool game_is_over = true;
      for (int r = 0; r < 4 && game_is_over; ++r) {
        for (int c = 0; c < 4 && game_is_over; ++c) {
          game_is_over = (T[r][c] != '.');
        }
      }
      if (game_is_over) {
        printf("Case #%d: Draw\n", test);
      } else {
        printf("Case #%d: Game has not completed\n", test);
      }
    }
  }
  return 0;
}
