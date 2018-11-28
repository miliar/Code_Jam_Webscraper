#include <iostream>
#include <string>

using namespace std;

int board[4][4];

int check(int a1, int a2, int b1, int b2, int c1, int c2, int d1, int d2) {
  // Guess 1
  if ((board[a1][a2] == 1 || board[a1][a2] == -1) &&
      (board[b1][b2] == 1 || board[b1][b2] == -1) &&
      (board[c1][c2] == 1 || board[c1][c2] == -1) &&
      (board[d1][d2] == 1 || board[d1][d2] == -1)) {
    return 1;
  }

  // Guess 2
  if ((board[a1][a2] == 2 || board[a1][a2] == -1) &&
      (board[b1][b2] == 2 || board[b1][b2] == -1) &&
      (board[c1][c2] == 2 || board[c1][c2] == -1) &&
      (board[d1][d2] == 2 || board[d1][d2] == -1)) {
    return 2;
  }

  return 0;
}

int main() {
  int t; cin >> t;
  for (int test = 1; test <= t; ++test) {
    cout << "Case #" << test << ": ";
    string dummy; getline(cin, dummy);

    bool filled = true;
    bool done = false;
    int result;

    for (int i = 0; i < 4; ++i) {
      string s; getline(cin, s);
      for (int j = 0; j < 4; ++j) {
        if (s[j] == 'X') {
          board[i][j] = 1;
        } else if (s[j] == 'O') {
          board[i][j] = 2;
        } else if (s[j] == 'T') {
          board[i][j] = -1;
        } else if (s[j] == '.') {
          filled = false;
          board[i][j] = 0;
        }
      }
    }

    for (int i = 0; i < 4; ++i) {
      result = check(i, 0, i, 1, i, 2, i, 3);
      if (result == 1) { cout << "X won" << endl; done = true; break; }
      if (result == 2) { cout << "O won" << endl; done = true; break; }
    }
    if (done) continue;
    
    for (int i = 0; i < 4; ++i) {
      result = check(0, i, 1, i, 2, i, 3, i);
      if (result == 1) { cout << "X won" << endl; done = true; break; }
      if (result == 2) { cout << "O won" << endl; done = true; break; }
    }
    if (done) continue;

    result = check(0, 0, 1, 1, 2, 2, 3, 3);
    if (result == 1) { cout << "X won" << endl; done = true; }
    if (result == 2) { cout << "O won" << endl; done = true; }
    if (done) continue;

    result = check(0, 3, 1, 2, 2, 1, 3, 0);
    if (result == 1) { cout << "X won" << endl; done = true; }
    if (result == 2) { cout << "O won" << endl; done = true; }
    if (done) continue;

    if (filled) {
      cout << "Draw" << endl;
    } else {
      cout << "Game has not completed" << endl;
    }
  }
  return 0;
}