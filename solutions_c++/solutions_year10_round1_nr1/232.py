#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
const int dy[] = {1, 1, 0, -1, -1, -1, 0, 1};

bool check(int n, int k, const vector<string>& board, char color) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (board[i][j] != color) {
        continue;
      }
      for (int d = 0; d < 8; d++) {
        int x = i + (k - 1) * dx[d];
        int y = j + (k - 1) * dy[d];
        if (x < 0 || x >= n || y < 0 || y >= n) {
          continue;
        }
        x = i;
        y = j;
        bool success = true;
        for (int c = 0; c < k; c++) {
          if (board[x][y] != color) {
            success = false;
            break;
          }
          x += dx[d];
          y += dy[d];
        }
        if (success) {
          return true;
        }
      }
    }
  }
  return false;
}

string rotate_and_check(int n, int k, const vector<string>& board) {
  vector<string> b;
  for (int i = 0; i < n; i++) {
    b.push_back(string(n, ' '));
  }
  // rotate
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      b[j][n - 1 - i] = board[i][j];
    }
  }
  // gravity
  for (int i = 0; i < n; i++) {
    int p = n - 1;
    for (int q = n - 1; q >=0; q--) {
      if (b[q][i] != '.') {
        if (p != q) {
          b[p][i] = b[q][i];
          b[q][i] = '.';
        }
        p--;
      }
    }
  }
  // check
  bool red = check(n, k, b, 'R');
  bool blue = check(n, k, b, 'B');
  if (red) {
    if (blue) {
      return "Both";
    } else {
      return "Red";
    }
  } else {
    if (blue) {
      return "Blue";
    } else {
      return "Neither";
    }
  }
}

int main() {
  int T;
  cin >> T;
  for (int x = 1; x <= T; x++) {
    int N, K;
    cin >> N >> K;
    vector<string> board;
    string line;
    for (int i = 0; i < N; i++) {
      cin >> line;
      board.push_back(line);
    }
    string y = rotate_and_check(N, K, board);
    cout << "Case #" << x << ": " << y << endl;
  }
}
