#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

const int N = 64;

char arr[N][N];
int rows, cols;

bool valid(int i, int j) {
  if (i+1 >= rows) return false;
  if (j+1 >= cols) return false;
  return arr[i][j] == '#' && arr[i][j+1] == '#' && arr[i+1][j] == '#' && arr[i+1][j+1] == '#';
}

bool process() {
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      if (arr[i][j] == '#') {
        if (!valid(i, j)) return false;

        arr[i][j] = '/';
        arr[i][j+1] = '\\';
        arr[i+1][j] = '\\';
        arr[i+1][j+1] = '/';
      }
    }
  }

  return true;
}

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    cin >> rows >> cols;
    for (int i = 0; i < rows; i++) cin >> arr[i];

    cout << "Case #" << tt << ":" << endl;
    if (!process()) cout << "Impossible" << endl;
    else {
      for (int i = 0; i < rows; i++) cout << arr[i] << endl;
    }
  }

  return 0;
}

