#include <cstdio>

char s[10][10];

int g(char c) {
  bool diag1 = 1, diag2 = 1;
  for (int i = 0; i < 4; ++i) {
    diag1 &= (s[i][i] == c || s[i][i] == 'T');
    diag2 &= (s[i][3 - i] == c || s[i][3 - i] == 'T');
    bool row = 1, col = 1;
    for (int j = 0; j < 4; ++j) {
      row &= (s[i][j] == c || s[i][j] == 'T');
      col &= (s[j][i] == c || s[j][i] == 'T');
    }
    if (row || col) return 1;
  }
  if (diag1 || diag2) return 1;
  return 0;
}

int f() {
  if (g('X')) return 1;
  if (g('O')) return 2;
  int cnt = 0;
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      if (s[i][j] == '.') ++cnt;
    }
  }
  if (cnt == 0) return 0;
  return 3;
}

int main() {
  int cas = 0;
  int T; scanf("%d", &T);
  while (T--) {
    for (int i = 0; i < 4; ++i) scanf("%s", s[i]);
    printf("Case #%d: ", ++cas);
    int ret = f();
    if (ret == 0) puts("Draw");
    if (ret == 1) puts("X won");
    if (ret == 2) puts("O won");
    if (ret == 3) puts("Game has not completed");
  }
  return 0;
}
