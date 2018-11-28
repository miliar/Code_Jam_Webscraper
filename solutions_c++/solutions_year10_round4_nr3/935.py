#include <string>
#include <vector>
#include <iostream>
using namespace std;
int bact[101][101];
int transfo() {
  int goon = 0;
  for (int x = 0; x < 100; x++) {
    for (int y = 0; y < 100; y++) {
      if (bact[x][y]) {
        goon = 1;
        if ((x && bact[x-1][y] > 0) || (y && bact[x][y-1] > 0)) {
        } else {
          bact[x][y] = 2;
        }
      } else {
        if (x && bact[x-1][y] > 0 && y && bact[x][y-1] > 0) {
          bact[x][y] = -1;
        }
      }
    }
  }
  for (int x = 0; x < 100; x++) {
    for (int y = 0; y < 100; y++) {
      switch (bact[x][y]) {
        case -1: bact[x][y] = 1; break;
        case 2: bact[x][y] = 0; break;
      }
    }
  }
  return goon;
}
int solver() {
  int r, x1, x2, y1, y2;
  cin >> r;
  for (int x = 0; x < 101; x++) 
    for (int y = 0; y < 101; y++) 
      bact[x][y] = 0;

  for (int l = 0; l < r; l++) {
    cin >> x1 >> y1 >> x2 >> y2;
    for (int x = x1; x <= x2; x++) {
      for (int y = y1; y <= y2; y++) bact[x - 1][y - 1] = 1;
    }
  }

  int ret = 0;
  while (transfo()) ret++;
  return ret;
}
int main() {
  int c;
  cin >> c;
  for (int x = 1; x <= c; x++) cout << "Case #" << x << ": " << solver() << endl;
  return 0;
}

