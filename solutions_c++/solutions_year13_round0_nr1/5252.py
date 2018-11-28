#include <cstdio>

char m[10][10];
int same(char a1, char a2, char a3, char a4) {
  if (a1 == '.' || a2 == '.' || a3 == '.' || a4 == '.') {
    return 0;
  }
  if (a1 == 'T') a1 = a2;
  if (a2 == 'T') a2 = a1;
  if (a3 == 'T') a3 = a1;
  if (a4 == 'T') a4 = a1;
  if (a1 == a2 && a2 == a3 && a3 == a4) {
    if (a1 == 'O') 
      return 1;
    else 
      return 2;
  }
  return 0;
}

int work() {
  for (int i = 0; i < 4; ++i) {
    scanf("%s", m[i]);
  }

  for (int i = 0; i < 4; ++i) {
    int t = same(m[i][0], m[i][1], m[i][2], m[i][3]);
    if (t != 0)
      return t;

    t = same(m[0][i], m[1][i], m[2][i], m[3][i]);
    if (t != 0)
      return t;
  }
  int t = same(m[0][0], m[1][1], m[2][2], m[3][3]);
  if (t != 0)
    return t;
  t = same(m[3][0], m[2][1], m[1][2], m[0][3]);
  if (t != 0)
    return t;

  // Draw or not completed
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      if (m[i][j] == '.') {
        return 3;
      }
    }
  }
  return 0;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i) {
    printf("Case #%d: ", i);
    int v = work();
    if (v == 0) {
      puts("Draw");
    } else if (v == 1) {
      puts("O won");
    } else if (v == 2) {
      puts("X won");
    } else {
      puts("Game has not completed");
    }
  }
}
