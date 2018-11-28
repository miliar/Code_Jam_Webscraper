#include <iostream>
using namespace std;

bool check(string s[4], int x, int y, int dx, int dy, char *c) {
  int i = dx == 1 ? 0 : x;
  int j = dy == 1 ? 0 : y;
  char ch = s[i][j];
  if (ch == 'T') ch = s[i+dx][j+dy];
  if (ch == '.') return false;
  for (int k = 0; k < 4; ++ k) {
    if (s[i][j] != 'T' && s[i][j] != ch) {
      //cout << "checking " << i << j << s[i][j] << ch << endl;
      return false;
    }
    i += dx;
    j += dy;
  }
  *c = ch;
  return true;
}

bool checkd(string s[4], int dx, int dy, char *c) {
  int i = dx == 1 ? 0 : 3;
  int j = dy == 1 ? 0 : 3;
  char ch = s[i][j];
  if (ch == 'T') ch = s[i+dx][j+dy];
  if (ch == '.') return false;
  for (int k = 0; k < 4; ++ k) {
    if (s[i][j] != 'T' && s[i][j] != ch) {
      //cout << "checking " << i << j << s[i][j] << ch << endl;
      return false;
    }
    i += dx;
    j += dy;
  }
  *c = ch;
  return true;
}

bool CHECK_(string s[4], char *c) {
  for (int k = 0; k < 4; ++ k) {
    if (check(s, 0, k, 1, 0, c) || check(s, k, 0, 0, 1, c)) {
      return true;
    }
  }
  if (checkd(s, 1, 1, c) || checkd(s, 1, -1, c)) {
    return true;
  }
  return false;
}

int main() {
  int T;
  cin >> T;

  bool has_dot;
  string s[4];
  for (int t = 1; t <= T; ++ t) {
    has_dot = false;
    for (int i = 0; i < 4; ++ i) {
      cin >> s[i];
      for (int j = 0; j < 4; ++ j) {
        if (s[i][j] == '.') {
          has_dot = true;
          break;
        }
      }
    }

    char win[2][20] = { "X won", "O won" };
    string ans;
    char c;
    if (CHECK_(s, &c)) {
      ans = win[c == 'O'];
    } else if (has_dot) {
      ans = "Game has not completed";
    } else {
      ans = "Draw";
    }

    cout << "Case #" << t << ": " << ans << endl;
  }

  return 0;
}
