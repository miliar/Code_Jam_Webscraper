#include <iostream>
using namespace std;
int GetResult(char *r) {
  int count_x = 0;
  int count_o = 0;
  int count_t = 0;
  for (int j = 0; j < 4; ++j) {
    switch(r[j]) {
      case 'T':
        count_t++; break;
      case 'X':
        count_x++; break;
      case 'O':
        count_o++; break;
    }
  }
  if (count_x >= 3 && count_x + count_t == 4) return 0;
  if (count_o >= 3 && count_o + count_t == 4) return 1;
  return -1;
}
int Judge(char s[4][5]) {
  char r[4];
  for (int i = 0; i < 4; ++i) {
    int result = GetResult(s[i]);
    if (result >= 0) return result;
    for (int j = 0; j < 4; ++j) r[j] = s[j][i];
    result = GetResult(r);
    if (result >= 0) return result;
  }
  for (int i = 0; i < 4; ++i) {
    r[i] = s[i][i];
  }
  int result = GetResult(r);
  if (result >= 0) return result;
  for (int i = 0; i < 4; ++i) {
    r[i] = s[3 - i][i];
  }
  result = GetResult(r);
  if (result >= 0) return result;
  for (int i = 0; i < 4; ++i) for (int j =0; j < 4; ++j)
    if (s[i][j] == '.') return 2;
  return 3;
}
int main(int argc, char** argv) {
  int tc;
  scanf("%d", &tc);
  const char* answer[4] = {"X won", "O won", "Game has not completed", "Draw"};
  for (int cas = 1; cas <= tc; ++cas) {
    char s[4][5];
    for (int i = 0; i < 4; ++i) scanf("%s", s[i]);
    int result = Judge(s);
    printf("Case #%d: %s\n", cas, answer[result]);
  }
  return 0;
}
