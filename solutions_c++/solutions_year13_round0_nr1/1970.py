#include <iostream>

using namespace std;

char board[4][4];

bool check(char c) {
  bool win;
  
  for (int i = 0; i < 4; i++) {
    win = true;
    for (int k = 0; k < 4; k++) {
      char v = board[i][k];
      if (v != c && v != 'T')
        win = false;
    }
    if (win) return true;    
    
    win = true;
    for (int k = 0; k < 4; k++) {
      char v = board[k][i];
      if (v != c && v != 'T')
        win = false;
    }    
    if (win) return true;
  }
  
  win = true;
  for (int k = 0; k < 4; k++) {
    char v = board[k][k];
    if (v != c && v != 'T')
      win = false;
  }    
  if (win) return true;
  
  win = true;
  for (int k = 0; k < 4; k++) {
    char v = board[k][3-k];
    if (v != c && v != 'T')
      win = false;
  }    
  if (win) return true;  
  
  return false;
}

bool draw() {
  for (int i = 0; i < 4; i++) {
    for (int k = 0; k < 4; k++) {
      if (board[i][k] == '.')
        return false;
    }
  }
  return true;
}

int main() {
  int tc; cin >> tc;
  for (int t = 1; t <= tc; t++) {
    for (int i = 0; i < 4; i++) {
      string s; cin >> s;
      for (int k = 0; k < 4; k++) {
        board[i][k] = s[k];
      }
    }
    
    cout << "Case #" << t << ": ";
    if (check('X')) { cout << "X won"; }
    else if (check('O')) { cout << "O won"; }
    else if (draw()) { cout << "Draw"; }
    else { cout << "Game has not completed"; }
    cout << endl;
  }

  return 0;
}
