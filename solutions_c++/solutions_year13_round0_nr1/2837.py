#include <iostream>
using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; t++) {
    char a[4][4];
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        scanf("%c", &a[i][j]);
      }
      getchar();
    }
    getchar();
   
    printf("Case #%d: ", t);
    
    bool x_win = false;
    // horizontal
    for (int i = 0; i < 4; i++) {
      bool good = true;
      for (int j = 0 ; j < 4; j++) {
        if (a[i][j] == 'O' || a[i][j] == '.') {
          good = false;
          break;
        }
      }
      if (good) {
        x_win = true;
        break;
      }
    }
    // vert
    for (int j = 0; j < 4; j++) {
      bool good = true;
      for (int i = 0; i < 4; i++) {
        if (a[i][j] == 'O' || a[i][j] == '.') {
          good = false;
          break;
        }
      }
      if (good) {
        x_win = true;
        break;
      }
    }
    bool good = true;
    for (int n = 0; n < 4; n++) {
      if (a[n][n] == 'O' || a[n][n] == '.') {
        good = false;
        break;
      }
    }
    if (good) {
      x_win = true;
    }
    good = true;
    for (int n = 0; n < 4; n++) {
      if (a[n][3 - n] == 'O' || a[n][3 - n] == '.') {
        good = false;
        break;
      }
    }
    if (good) {
      x_win = true;
    }
    if (x_win) {
      printf("X won\n");
      continue;
    }
    
    bool y_win = false;
    // horizontal
    for (int i = 0; i < 4; i++) {
      bool good = true;
      for (int j = 0 ; j < 4; j++) {
        if (a[i][j] == 'X' || a[i][j] == '.') {
          good = false;
          break;
        }
      }
      if (good) {
        y_win = true;
        break;
      }
    }
    // vert
    for (int j = 0; j < 4; j++) {
      bool good = true;
      for (int i = 0; i < 4; i++) {
        if (a[i][j] == 'X' || a[i][j] == '.') {
          good = false;
          break;
        }
      }
      if (good) {
        y_win = true;
        break;
      }
    }
    good = true;
    for (int n = 0; n < 4; n++) {
      if (a[n][n] == 'X' || a[n][n] == '.') {
        good = false;
        break;
      }
    }
    if (good) {
      y_win = true;
    }
    good = true;
    for (int n = 0; n < 4; n++) {
      if (a[n][3 - n] == 'X' || a[n][3 - n] == '.') {
        good = false;
        break;
      }
    }
    if (good) {
      y_win = true;
    }
    if (y_win) {
      printf("O won\n");
      continue;
    }
    
    bool full = true;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        if (a[i][j] == '.') {
          full = false;
          break;
        }
      }
    }
    if (full) {
      printf("Draw\n");
    } else {
      printf("Game has not completed\n");
    }
  }
  return 0;
}