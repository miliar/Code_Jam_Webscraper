#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <cmath>

using namespace std;

int arr[2][128][128];
const int dx[] = { -1, 0, 1, 0 };
const int dy[] = { 0, -1, 0, 1 };

int main() {
  int cases; cin >> cases;
  for (int caseNo = 1; caseNo <= cases; caseNo++) {
    memset(arr, 0, sizeof(arr));
    int r; cin >> r;
    for (int i = 0; i < r; i++) {
      int x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
      for (int x = x1; x <= x2; x++) for (int y = y1; y <= y2; y++)
        arr[0][y][x] = 1;
    }

    int curr = 0, next = 1;
    int steps = 0;
    while (true) {
      steps++;
      memset(arr[next], 0, sizeof(arr[next]));

      int cnt = 0;
      for (int x = 1; x <= 100; x++) for (int y = 1; y <= 100; y++) {
        if (arr[curr][y][x]) {
          bool empty = true;
          for (int d = 0; d < 2; d++) if (arr[curr][y+dy[d]][x+dx[d]]) {
            empty = false; break;
          }
          if (!empty) cnt++, arr[next][y][x] = 1;
        } else {
          bool ok = true;
          for (int d = 0; d < 2; d++) if (!arr[curr][y+dy[d]][x+dx[d]]) {
            ok = false; break;
          }
          if (ok) cnt++, arr[next][y][x] = 1;
        }
      }
      if (cnt == 0) break;
      curr = 1-curr; next = 1-next;
    }

    cout << "Case #" << caseNo << ": " << steps << endl;
  }
  return 0;
}

