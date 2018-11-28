#include <iostream>
#include <cstdio>

using namespace std;

int N;

char board[4][5];

string solve() {
  bool x_win = false;
  bool o_win = false;

  int xs = 0;
  int zs = 0;
  for (int i = 0; i < 4; i++) {
    if (board[i][i] == 'X' || board[i][i] == 'T') {
      xs++;
    }
    if (board[i][i] == 'O' || board[i][i] == 'T') {
      zs++;
    }
  }
  if (xs == 4) x_win = true;
  if (zs == 4) o_win = true;

  xs = 0, zs = 0;
  for (int i = 0; i < 4; i++) {
    if (board[3 - i][i] == 'X' || board[3 - i][i] == 'T') {
      xs++;
    }
    if (board[3 - i][i] == 'O' || board[3 - i][i] == 'T') {
      zs++;
    }
  }
  if (xs == 4) x_win = true;
  if (zs == 4) o_win = true;


  for (int i = 0; i < 4; i++) {
    xs = 0, zs = 0;
    for (int j = 0; j < 4; j++) {
      if (board[j][i] == 'X' || board[j][i] == 'T') {
        xs++;
      }
      if (board[j][i] == 'O' || board[j][i] == 'T') {
        zs++;
      }
    }
    if (xs == 4) x_win = true;
    if (zs == 4) o_win = true;
  }

  for (int i = 0; i < 4; i++) {
    xs = 0, zs = 0;
    for (int j = 0; j < 4; j++) {
      if (board[i][j] == 'X' || board[i][j] == 'T') {
        xs++;
      }
      if (board[i][j] == 'O' || board[i][j] == 'T') {
        zs++;
      }
    }
    if (xs == 4) x_win = true;
    if (zs == 4) o_win = true;
  }

  if (x_win && o_win) {
    return "Draw";
  } else if (x_win) {
    return "X won";
  } else if (o_win) {
    return "O won";
  } else {
    int cnt = 0;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        if (board[i][j] == '.') cnt++;
      }
    }
    if (cnt == 0)
      return "Draw";
    else
      return "Game has not completed";
  }
}

int main() {
  scanf("%d\n", &N);
  for (int test = 0; test < N; test++) {
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        scanf("%c", &board[i][j]);
      }
      getchar();
    }
    getchar();
    printf("Case #%d: ", test + 1);
    cout << solve() << endl;
  }

  return 0;
}
