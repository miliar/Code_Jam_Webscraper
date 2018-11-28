#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0)
       return a;
    else
       return gcd(b, a % b);
}


bool process(char grid[][100], int R, int C, int numHash) {
  if (numHash%4 != 0) return false;
  int totalHashed = 0;
  while (totalHashed < numHash) {
    bool hashed = false;
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (grid[r][c] == '#') {
          if (c+1 < C && grid[r][c+1] == '#' &&
              r+1 < R && grid[r+1][c] == '#' &&
              r+1 < R && grid[r+1][c+1] == '#') {
                grid[r][c] = '/'; grid[r][c+1] = '\\'; grid[r+1][c] = '\\'; grid[r+1][c+1] = '/';
                totalHashed += 4;
                hashed = true;
                break;
          } else {
            return false;
          }
        }
      }
      if (hashed)
        break;
    }
  }
  return true;
}

int main() {
  freopen("data.txt", "r", stdin);
  freopen("outp1.txt", "w", stdout);
  long long T, n, R, C; char grid[100][100];
  cin >> T;
  for (int p = 0; p < T; p++) {
    cin >> R >> C;
    int numHash = 0;
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        cin >> grid[r][c];
        if (grid[r][c] == '#')
          numHash++;
      }
    }
    cout << "Case #" << p+1 << ":" << endl;
    if (process(grid, R, C, numHash)) {
      for (int r = 0; r < R; r++) {
        for (int c = 0; c< C; c++) {
          cout << grid[r][c];
        }
        cout << endl;
      }
    } else {
      cout << "Impossible" << endl;
    }
  }
}