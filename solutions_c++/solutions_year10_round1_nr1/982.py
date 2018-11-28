#include <iostream>
#include <deque>

using namespace std;

deque< deque<char> > board;

int dir[3] = {-1, 0, 1};

int n, k;

bool check(char p, int &cur, int r, int c, int dx, int dy) {
  if (board[r][c] == p) {
    ++cur;
  } else {
    return false;
  }
  if (cur == k) {
    return true;
  } else if (r + dir[dx] >= 0 && c + dir[dy] >= 0 && r + dir[dx] < n && c + dir[dy] < n) {
    return check(p, cur, r + dir[dx], c + dir[dy], dx, dy);
  } else {
    return false;
  }
}

int main () {
  int T;
  cin >> T;
  deque<char> row;
  deque< pair<int, int> > red;
  deque< pair<int, int> > blue;
  for (int i = 0; i < T; ++i) {
    board.clear();
    red.clear();
    blue.clear();
    cin >> n >> k;
    for (int j = 0; j < n; j++) {
      row.clear();
      for (int k = 0; k < n; ++k) {
        char cur;
        cin >> cur;
        if (cur == '.') {
          row.push_front(cur);
        } else {
          row.push_back(cur);
        }
      }
      board.push_back(row);
    }
    for (int j = 0; j < n; ++j) {
      for (int k = 0; k < n; ++k) {
        char c = board[j][k];
        if (c == 'R') {
          red.push_back(make_pair<int, int>(j, k));
        } else if (c == 'B') {
          blue.push_back(make_pair<int, int>(j, k));
        }
      }
    }
    int winner = 0;
    bool gogo = true;
    for (size_t j = 0; j < red.size() && gogo; ++j) {
      for (int k = 0; k < 3 && gogo; ++k) {
        for (int l = 0; l < 3 && gogo; ++l) {
          if (k == 1 && l == 1) continue;
          int cur = 0;
          if (check('R', cur, red[j].first, red[j].second, k, l)) {
            winner += 1;
            gogo = false;
          }
        }
      }
    }
    gogo = true;
    for (size_t j = 0; j < blue.size() && gogo; ++j) {
      for (int k = 0; k < 3 && gogo; ++k) {
        for (int l = 0; l < 3 && gogo; ++l) {
          if (k == 1 && l == 1) continue;
          int cur = 0;
          if (check('B', cur, blue[j].first, blue[j].second, k, l)) {
            winner += 2;
            gogo = false;
          }
        }
      }
    }
    cout << "Case #" << i + 1 << ": ";
    if (winner == 3) {
      cout << "Both";
    } else if (winner == 1) {
      cout << "Red";
    } else if (winner == 2) {
      cout << "Blue";
    } else {
      cout << "Neither";
    }
    cout << endl;
  }
  return 0;
}
