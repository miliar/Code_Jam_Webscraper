#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

#define SIZE 100

int f = 0;
int data[2][SIZE][SIZE];

bool step() {
  int cnt = 0;
  for (int i = 0; i < SIZE; i++)
    for (int j = 0; j < SIZE; j++) {
      data[1 - f][i][j] = 0;

      if (data[f][i][j]) {
        bool ok = false;
        if (i > 0 && data[f][i - 1][j]) ok = true;
        if (j > 0 && data[f][i][j - 1]) ok = true;

        if (ok)
          data[1 - f][i][j] = data[f][i][j];

      } else if (i > 0 && j > 0 && data[f][i - 1][j] && data[f][i][j - 1]) {
        data[1 - f][i][j] = 1;

      }

      cnt += data[1 - f][i][j];
      
    }

  f = 1 - f;
  return cnt != 0;
}

int main() {
  int _t; cin >> _t;
  for (int _tt = 1; _tt <= _t; _tt++) {
    cout << "Case #" << _tt << ": ";
    int r; cin >> r;
    f = 0;
    memset(data, 0, sizeof (data));
    for (int i = 0; i < r; i++) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      for (int x = x1; x <= x2; x++)
        for (int y = y1; y <= y2; y++)
          data[0][x - 1][y - 1]++;
    }

    int t = 1;
    while (step()) t++;
    cout << t << endl;

  }

  return 0;
}