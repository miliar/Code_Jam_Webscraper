#include <cstdio>

bool vertical(char a[4][5], char i, char j) {
  char times = 0;
  for (char k = 0; j + k < 4; ++k) {
    if (a[i][j + k] == a[i][j] || a[i][j + k] == 'T') {
      ++times;
    }
  }
  return times == 4;
}
bool horizontal(char a[4][5], char i, char j) {
  char times = 0;
  for (char k = 0; i + k < 4; ++k) {
    if (a[i + k][j] == a[i][j] || a[i][j + k] == 'T') {
      ++times;
    }
  }
  return times == 4;
}
bool diag1(char a[4][5], char i, char j) {
  char times = 0;
  for (char k = 0; i + k < 4 && j + k < 4; ++k) {
    if (a[i + k][j + k] == a[i][j] || a[i + k][j + k] == 'T') {
      ++times;
    }
  }
  return times == 4;
}
bool diag2(char a[4][5], char i, char j) {
  char times = 0;
  for (char k = 0; i + k < 4 && j - k >= 0; ++k) {
    if (a[i + k][j - k] == a[i][j] || a[i + k][j - k] == 'T') {
      ++times;
    }
  }
  return times == 4;
}

int main() {
  bool doContinue;
  char i, j, k, dots, a[4][5];
  short t;

  scanf("%hd", &t);
  for (i = 1; i <= t; ++i) {
    for (j = 0; j < 4; ++j) {
      scanf("%s", a[j]);
    }

    doContinue = false;
    for (j = 0; j < 4; ++j) {
      for (k = 0; k < 4; ++k) {
        if (a[j][k] == 'T' || a[j][k] == '.') {
          continue;
        }
        if (vertical(a, j, k) || horizontal(a, j, k) ||
            diag1(a, j, k) || diag2(a, j, k)) {
          printf("Case #%d: %c won\n", i, a[j][k]);
          doContinue = true;
          break;
        }
      }
      if (doContinue) {
        break;
      }
    }

    if (doContinue) {
      continue;
    }
    dots = 0;
    for (j = 0; j < 4; ++j) {
      for (k = 0; k < 4; ++k) {
        if (a[j][k] == '.') {
          ++dots;
        }
      }
    }
    printf("Case #%d: %s\n", i, dots ? "Game has not completed" : "Draw");
  }

  return 0;
}
