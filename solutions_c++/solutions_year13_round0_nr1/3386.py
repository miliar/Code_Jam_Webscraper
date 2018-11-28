#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int _t, result;
string in[5];

string result_string[4] = {"X won", "O won", "Draw", "Game has not completed"};

bool won(string line, int player) {
  int c = 0;
  for (int i = 0; i < 4; i++) {
    c += line[i] == (player == 0 ? 'X' : 'O') || line[i] == 'T';
  }
  return c == 4;
}

string column(int k) {
  string ret = "";
  for (int i = 0; i < 4; i++) ret += in[i][k];
  return ret;
}

string diagonal(int t) {
  string ret = "";
  for (int i = 0; i < 4; i++) {
    ret += in[i][(t == 0) ? 3 - i : i];
  }
  return ret;
}

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  cin >> _t;
  for (int t = 1; t <= _t; t++) {
    result = 2;
    for (int i = 0; i < 4; i++) {
      cin >> in[i];
      if (in[i].find('.') != -1) result = 3;
    }
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < 4; j++) {
        if (won(in[j], i) || won(column(j), i)) result = i;
      }
      if (won(diagonal(0), i) || won(diagonal(1), i)) result = i;
    }
    cout << "Case #" << t << ": " << result_string[result] << endl;
  }
  return 0;
}