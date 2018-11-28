#include <cstdio>

char F[4][4];

bool won(char w) {
  for (int y = 0; y < 4; y++) {
    int ok = true;
    for (int x = 0; x < 4; x++) if (!(F[y][x] == w || F[y][x] == 'T')) ok = false;
    if (ok) return true;
  }
  for (int y = 0; y < 4; y++) {
    int ok = true;
    for (int x = 0; x < 4; x++) if (!(F[x][y] == w || F[x][y] == 'T')) ok = false;
    if (ok) return true;
  }
  if (1) {
    int ok = true;
    for (int x = 0; x < 4; x++) if (!(F[x][x] == w || F[x][x] == 'T')) ok = false;
    if (ok) return true;
  }
  if (1) {
    int ok = true;
    for (int x = 0; x < 4; x++) if (!(F[x][3-x] == w || F[x][3-x] == 'T')) ok = false;
    if (ok) return true;
  }
  return false;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int caseno = 1; caseno <= T; caseno++) {
    bool isdot = false;
    for (int y = 0; y < 4; y++) {
      char buf[10]; scanf("%s", buf);
      for (int x = 0; x < 4; x++) {
        F[y][x] = buf[x];
        if (F[y][x] == '.') isdot = true;
//        fprintf(stderr, "%d,%d -> %c\n", x, y, F[y][x]);
      }
    }

    printf("Case #%d: ", caseno);
    if (won('X')) printf("X won\n");
    else if (won('O')) printf("O won\n");
    else if (!isdot) printf("Draw\n");
    else printf("Game has not completed\n");
  }
}
