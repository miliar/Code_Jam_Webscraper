#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;


char board[5][5];
char line[5];
bool over() {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (board[i][j] == '.') {
        return false;
      }
    }
  }
  return true;
}
bool checkwin(char c) {
  for (int i = 0; i < 4; i++) {
    int num = 0;
    for (int j = 0; j < 4; j++) {
      if (board[i][j] == c || board[i][j] == 'T') {
        num++;
      }
    }
    if (num == 4) return true;
  }
  for (int i = 0; i < 4; i++) {
    int num = 0;
    for (int j = 0; j < 4; j++) {
      if (board[j][i] == c || board[j][i] == 'T') {
        num++;
      }
    }
    if (num == 4) return true;
  }

  int diag1num = 0;
  for (int i = 0; i < 4; i++) {
    if (board[i][i] == c || board[i][i] == 'T') {
      diag1num++;
    }
  }
  if (diag1num == 4) return true;

  int diag2num = 0;
  for (int i = 0; i < 4; i++) {
    if (board[i][4-i-1] == c || board[i][4-i-1] == 'T') {
      diag2num++;
    }
  }
  if (diag2num == 4) return true;
  return false;
}
void solve() {
  if (checkwin('X')) {
    printf("X won\n");
    return;
  }
  if (checkwin('O')) {
    printf("O won\n");
    return;
  }
  if (over()) {
    printf("Draw\n");
    return;
  }
  printf("Game has not completed\n");
}
int main() {
  int n;
  scanf("%d\n", &n);
  for (int i = 0; i < n; i++) {
    int r = 0;
    for (int j = 0; j < 4; j++) {
      scanf("%s", board[j]);
    }
    printf("Case #%d: ", i +1);
    solve();
  }
  return 0;
}

