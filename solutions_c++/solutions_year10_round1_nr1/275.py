#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int dy[] = {-1, -1, 0, 1},
          dx[] = {0, 1, 1, 1};

bool ok(int y, int x, int n) {
  return y >= 0 && y < n && x >= 0 && x < n;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    cerr << "ca = " << ca << endl;
    int n, k;
    cin >> n >> k;
    vector<string> v(n);
    for (int i = 0; i < n; ++i) {
      cin >> v[i];
    }
    for (int i = 0; i < n; ++i) {
      int free = n-1;
      for (; free >= 0 && v[i][free] != '.';) --free;
      for (int j = free; free >= 0 && j >= 0; --j) if (v[i][j] != '.') {
        char tmp = v[i][j];
        v[i][j] = '.';
        v[i][free] = tmp;
        --free;
      }
    }
    vector<string> w(n, string(n, ' '));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        w[i][j] = v[n-1-j][i];
      }
    }
    bool joinr = false, joinb = false;
    for (int d = 0; d < 4; ++d) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          bool red = true;
          for (int h = 0; h < k && red; ++h) {
            if (!ok(i+h*dy[d], j+h*dx[d], n) || v[i+h*dy[d]][j+h*dx[d]] != 'R') red = false;
          }
          if (red) joinr = true;
          bool blue = true;
          for (int h = 0; h < k && blue; ++h) {
            if (!ok(i+h*dy[d], j+h*dx[d], n) || v[i+h*dy[d]][j+h*dx[d]] != 'B') blue = false;
          }
          if (blue) joinb = true;
        }
      }
    }
    cout << "Case #" << ca << ": ";
    if (joinr && joinb) cout << "Both" << endl;
    else if (joinr) cout << "Red" << endl;
    else if (joinb) cout << "Blue" << endl;
    else cout << "Neither" << endl;
  }
}
