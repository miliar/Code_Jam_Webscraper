#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <cmath>

using namespace std;

int arr[100][100];

inline int val(int large, int small, int oi, int oj, int i, int j) {
  if (oi <= i && i < oi+small && oj <= j && j < oj+small)
    return arr[i-oi][j-oj];
  return -1;
}

bool valid(int large, int small, int oi, int oj) {
  for (int i = 0; i < large; i++) {
    int x1 = large-i-1, y1 = 0;
    int x2 = large-1, y2 = i;
    while (x1 < x2) {
      int a = val(large, small, oi, oj, y1, x1);
      int b = val(large, small, oi, oj, y2, x2);
      if (!(a < 0 || b < 0 || a == b)) return false;
      x1++; x2--; y1++; y2--;
    }
  }

  for (int i = 1; i < large; i++) {
    int y1 = i, x1 = 0;
    int y2 = large-1, x2 = large-i-1;
    while (x1 < x2) {
      int a = val(large, small, oi, oj, y1, x1);
      int b = val(large, small, oi, oj, y2, x2);
      if (!(a < 0 || b < 0 || a == b)) return false;
      x1++; x2--; y1++; y2--;
    }
  }

  for (int i = 0; i < large; i++) {
    int y1 = i, x1 = 0;
    int y2 = 0, x2 = i;
    while (x1 < x2) {
      int a = val(large, small, oi, oj, y1, x1);
      int b = val(large, small, oi, oj, y2, x2);
      if (!(a < 0 || b < 0 || a == b)) return false;
      x1++; x2--; y1--; y2++;
    }
  }

  for (int i = 1; i < large; i++) {
    int y1 = large-1, x1 = i;
    int y2 = i, x2 = large-1;
    while (x1 < x2) {
      int a = val(large, small, oi, oj, y1, x1);
      int b = val(large, small, oi, oj, y2, x2);
      if (!(a < 0 || b < 0 || a == b)) return false;
      x1++; x2--; y1--; y2++;
    }
  }

  return true;
}

bool valid(int large, int small) {
  for (int i = 0; i + small <= large; i++) {
    for (int j = 0; j + small <= large; j++) {
      if (valid(large, small, i, j)) return true;
    }
  }
  return false;
}

int main() {
  int cases; cin >> cases;
  for (int caseNo = 1; caseNo <= cases; caseNo++) {
    int k; cin >> k;
    for (int i = 0; i < k; i++) {
      int x = k-i-1, y = 0;
      for (; x < k; x++, y++) cin >> arr[y][x];
    }
    for (int i = 1; i < k; i++) {
      int y = i, x = 0;
      for (; y < k; x++, y++) cin >> arr[y][x];
    }

    for (int kk = k; true; kk++) {
      if (valid(kk, k)) {
        cout << "Case #" << caseNo << ": " << ((kk*kk) - (k*k)) << endl;
        break;
      }
    }

  }
  return 0;
}

