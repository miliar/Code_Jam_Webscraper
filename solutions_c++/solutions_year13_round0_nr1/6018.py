#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

const int N = 4;
char board[N][N];

bool IsWin(char b[N][N], char ele) {
  for (int row = 0; row < N; ++row) {
    int cnt = 0;
    for (int col = 0; col < N; ++col) {
      if (b[row][col] == ele || b[row][col] == 'T') {
	cnt ++;
      }
    }
    if (cnt == N) {
      return true;
    }
  }
  for (int col = 0; col < N; ++col) {
    int cnt = 0;
    for (int row = 0; row < N; ++row) {
      if (b[row][col] == ele || b[row][col] == 'T') {
	cnt ++;
      }
    }
    if (cnt == N) {
      return true;
    }
  }
  int cnt_1 = 0;
  int cnt_2 = 0;
  for (int row = 0; row < N; ++row) {
    if (board[row][row] == ele || b[row][row] == 'T') {
      cnt_1 ++;
    }
    if (board[row][N - row - 1] == ele || b[row][N - row - 1] == 'T') {
      cnt_2 ++;
    }
  }
  if (cnt_1 == N || cnt_2 == N) {
    return true;
  }
  return false;
}

const int XWIN = 0;
const int OWIN = 1;
const int DRAW = 2;
const int NONE = 3;

int GetStatus(char b[N][N]) {
  if (IsWin(b, 'O')) {
    return OWIN;
  }
  if (IsWin(b, 'X')) {
    return XWIN;
  }
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      if (b[i][j] == '.') {
	return NONE;
      }
    }
  }
  return DRAW;
}

void Input() {
  for (int i = 0; i < N; ++i) {
    scanf("%s", board[i]);
  } 
}

int main() {
  //  freopen("in.txt", "r", stdin);
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i){
    Input();
    int status = GetStatus(board);
    printf("Case #%d: ", i);
    if (status == XWIN) {
      printf("X won\n");
    }
    if (status == OWIN) {
      printf("O won\n");
    }
    if (status == DRAW) {
      printf("Draw\n");
    }
    if (status == NONE) {
      printf("Game has not completed\n");
    }
  }

  return 0;
}
