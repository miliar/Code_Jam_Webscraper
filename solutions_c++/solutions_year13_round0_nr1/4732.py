#include <cmath>
#include <set>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <cstring>
#include <cctype>
#include <string>
#include <sstream>
#include <stack>
#include <queue>

using namespace std;

#define maxn 4

bool isWin(char b[][maxn + 1], char c) {
  int x0[] = {0, 1, 2, 3, 0, 0, 0, 0, 0, 3};
  int y0[] = {0, 0, 0, 0, 0, 1, 2, 3, 0, 0};
  int ax[] = {0, 0, 0, 0, 1, 1, 1, 1, 1, -1};
  int ay[] = {1, 1, 1, 1, 0, 0, 0, 0, 1, 1};

  for (int i = 0; i < 10; i++) {
    int j = 0;
    while (j < maxn && (b[y0[i] + ay[i] * j][x0[i] + ax[i] * j] == c || b[y0[i] + ay[i] * j][x0[i] + ax[i] * j] == 'T')) j++;
    if (j == maxn) return true;
  }

  return false;
}

int main() {
  int t;
  scanf("%d", &t);

  char b[maxn][maxn + 1];
  bool isEmptySquareExists;

  for (int it = 0; it < t; it++) {
    isEmptySquareExists = false;

    for (int i = 0; i < 4; i++) {
      scanf("%s", b[i]);
      if (strchr(b[i], '.'))
        isEmptySquareExists = true;
    }

    printf("Case #%d: ", it + 1);

    if (isWin(b, 'X')) puts("X won");
    else if (isWin(b, 'O')) puts("O won");
    else if (isEmptySquareExists) puts("Game has not completed");
    else puts("Draw");
  }

  return 0;
}
