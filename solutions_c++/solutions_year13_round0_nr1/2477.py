#include <cstdio>

bool eq(char a, char b) {
  if (a == '.' || b == '.') return false;
  if (a == 'T' || b == 'T') return true;
  return a == b;
}

char chr(char a, char b) {
  return a == 'T' ? b : a;
}

char m[4][5];

bool chk(int i, int j, int dx, int dy) {
  bool qq = true;
  for (int t = 0; t < 3; ++t, i+=dx, j+=dy)
    qq &= eq(m[i][j], m[i+dx][j+dy]);

  if (qq)
    printf("%c won", chr(m[i][j], m[i-dx][j-dy]));

  return qq;
}

void jizz() {
  for (int i = 0; i < 4; ++i)
    scanf("%s", m[i]);

  for (int i = 0; i < 4; ++i)
    if (chk(i, 0, 0, 1) || chk(0, i, 1, 0))
      return;

  if (chk(0, 0, 1, 1) || chk(3, 0, -1, 1))
    return;

  bool qq = true;
  for (int i = 0; i < 4; ++i)
    for (int j = 0; j < 4; ++j)
      qq &= m[i][j] != '.';

  printf("%s", qq ? "Draw" : "Game has not completed");
}

int main() {
  int t;
  scanf("%d", &t);

  for (int i = 1; i <= t; ++i) {
    printf("Case #%d: ", i);
    jizz();
    puts("");
  }

  return 0;
}
