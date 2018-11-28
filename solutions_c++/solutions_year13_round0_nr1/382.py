#include <stdio.h>

int main() {
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    char s[4][5];
    for (int i=0;i<4;i++) scanf("%s", s[i]);
    int xt = -1, yt = -1;
    for (int i=0;i<4;i++)
      for (int j=0;j<4;j++)
        if (s[i][j] == 'T') {
          xt = i;
          yt = j;
        }
    int ans = 0;
    for (int r=0;r<2;r++) {
      char ch = r == 0 ? 'X' : 'O';
      if (xt != -1) s[xt][yt] = ch;
      for (int i=0;i<4;i++)
        if (s[i][0] == ch && s[i][1] == ch && s[i][2] == ch && s[i][3] == ch) ans |= (1 << r);
      for (int i=0;i<4;i++)
        if (s[0][i] == ch && s[1][i] == ch && s[2][i] == ch && s[3][i] == ch) ans |= (1 << r);
      if (s[0][0] == ch && s[1][1] == ch && s[2][2] == ch && s[3][3] == ch) ans |= (1 << r);
      if (s[0][3] == ch && s[1][2] == ch && s[2][1] == ch && s[3][0] == ch) ans |= (1 << r);
    }
    printf("Case #%d: ", qq);
    if (ans == 1) printf("X won\n"); else
    if (ans == 2) printf("O won\n"); else {
      int ok = 0;
      for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
          if (s[i][j] == '.') ok = 1;
      if (ok) printf("Game has not completed\n");
      else printf("Draw\n");
    }
  }
  return 0;
}
