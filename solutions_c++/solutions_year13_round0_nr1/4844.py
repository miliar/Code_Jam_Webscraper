#include<cstdio>

char B[4][4];
bool draw_possible;

bool check(char X) {
  bool flag;

  for (int i = 0; i < 4; i++) {
    flag = true;
    for (int j = 0; j < 4; j++) {
      if (B[i][j] != X && B[i][j] != 'T') {
        flag = false;
      }
    }
    if (flag) { return true; }
  }

  for (int i = 0; i < 4; i++) {
    flag = true;
    for (int j = 0; j < 4; j++) {
      if (B[j][i] != X && B[j][i] != 'T') {
        flag = false;
      }
    }
    if (flag) { return true; }
  }

  flag = true;
  for (int i = 0; i < 4; i++) {
    if (B[i][i] != X && B[i][i] != 'T') {
      flag = false;
    }
  }
  if (flag) { return true; }

  flag = true;
  for (int i = 0; i < 4; i++) {
    if (B[3-i][i] != X && B[3-i][i] != 'T') {
      flag = false;
    }
  }
  if (flag) { return true; }

  return false;
}

int main() {
  int T;
  scanf("%d ", &T);
  for (int Z = 1; Z <= T; Z++) {
    draw_possible = 1;
    for (int i = 0; i < 4; i++) {
      for (int j  = 0; j < 4; j++) {
        scanf("%c ", &B[i][j]);
        if (B[i][j] == '.') { draw_possible = 0; }
      }
    }

    printf("Case #%d: ", Z);
    if (check('X')) {
      printf("X won");
    } else if (check('O')) {
      printf("O won");
    } else if (draw_possible) {
      printf("Draw");
    } else {
      printf("Game has not completed");
    }

    printf("\n");
  }
  return 0;
}
