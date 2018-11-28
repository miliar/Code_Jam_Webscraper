#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <cmath>

using namespace std;

const int N = 50;

char arr[N][N];

bool go(int n, int t, char ch, int dy, int dx, int i, int j) {
  while (t--) {
    if (i < 0 || i >= n || j < 0 || j >= n) return false;
    if (arr[i][j] != ch) return false;
    i += dy; j += dx;
  }
  return true;
}

bool go(int n, int t, char ch) {
  for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) if (arr[i][j] == ch) {
    if (go(n, t, ch, 0, 1, i, j)) return true;
    if (go(n, t, ch, 1, 0, i, j)) return true;
    if (go(n, t, ch, 1, -1, i, j)) return true;
    if (go(n, t, ch, 1, 1, i, j)) return true;
  }
  return false;
}

int main() {
  int cases; cin >> cases;
  for (int caseNo = 1; caseNo <= cases; caseNo++) {
    int n, t; cin >> n >> t;
    for (int i = 0, j = n-1; i < n; i++, j--) {
      string s; cin >> s;
      for (int k = 0; k < n; k++) {
        arr[k][j] = s[k];
      }
    }

    for (int j = 0; j < n; j++) {
      int i = n-1;
      while (i >= 0) {
        if (arr[i][j] == '.') {
          bool found = false;
          for (int k = i-1; k >= 0; k--) {
            if (arr[k][j] != '.') {
              found = true;
              arr[i][j] = arr[k][j];
              arr[k][j] = '.';
              break;
            }
          }
          if (!found) break;
        }
        i--;
      }
    }

    int b = go(n, t, 'B');
    int r = go(n, t, 'R');
    cout << "Case #" << caseNo << ": ";
    if (!b && !r) cout << "Neither";
    if (!b && r) cout << "Red";
    if (b && !r) cout << "Blue";
    if (b && r) cout << "Both";
    cout << endl;
  }
  return 0;
}

