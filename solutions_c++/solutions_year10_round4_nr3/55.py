#include <cstring>
#include <iostream>
using namespace std;

int b[100][100];
int c[100][100];

bool empty() {
  for (int x = 0; x < 100; x++) {
    for (int y = 0; y < 100; y++) {
      if (b[x][y] == 1) {
        return false;
      }
    }
  }
  return true;
}

void change() {
  memmove(c, b, sizeof(c));
  for (int x = 0; x < 100; x++) {
    for (int y = 0; y < 100; y++) {
      if (b[x][y] == 1 && ((x == 0 || b[x - 1][y] == 0) && (y == 0 || b[x][y - 1] == 0))) {
        c[x][y] = 0;
      }
      if (b[x][y] == 0 && ((x > 0 && b[x - 1][y] == 1) && (y > 0 && b[x][y - 1] == 1))) {
        c[x][y] = 1;
      }
    }
  }
  memmove(b, c, sizeof(b));
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int R;
    cin >> R;
    memset(b, 0, sizeof(b));
    for (int i = 0; i < R; i++) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      x1--, y1--, x2--, y2--;
      for (int x = x1; x <= x2; x++) {
        for (int y = y1; y <= y2; y++) {
          b[x][y] = 1;
        }
      }
    }
    int time = 0;
    while (!empty()) {
      change();
      time++;
    }
    cout << "Case #" << t << ": " << time << endl;
  }
}
