#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
const int N = 4;

bool inside(int y, int x) {
  return y >= 0 && y < N && x >= 0 && x < N;
}

bool won(const vector<string>& b, char p) {
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      for (int d = 0; d < 4; ++d) {
        bool w = true;
        int y = i, x = j;
        for (int k = 0; k < 4 && w; ++k) {
          if (!inside(y, x) || (b[y][x] != p && b[y][x] != 'T')) {
            w = false;
          }
          y += dy[d];
          x += dx[d];
        }
        if (w) return true;
      }
    }
  }
  return false;
}

bool full(const vector<string>& b) {
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      if (b[i][j] == '.') return false;
    }
  }
  return true;
}

int main() {
  int t;
  cin >> t;
  for (int ca = 1; t--; ++ca) {
    vector<string> b(N);
    for (int i = 0; i < N; ++i) {
      cin >> b[i];
    }
    bool xw = won(b, 'X');
    bool ow = won(b, 'O');
    cout << "Case #" << ca << ": ";
    if (xw && !ow) cout << "X won" << endl;
    else if (ow && !xw) cout << "O won" << endl;
    else if (!full(b)) cout << "Game has not completed" << endl;
    else cout << "Draw" << endl;
  }
}
