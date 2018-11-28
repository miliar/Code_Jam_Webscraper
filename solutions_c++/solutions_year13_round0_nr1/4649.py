#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <cstdlib>
#include <utility>

using namespace std;

string A[4];

int check(int r, int c, int dr, int dc) {
  int v = 0;
  for(int i = 0; i < 4; i++, r += dr, c += dc) {
    if(A[r][c] == 'X') {
      v |= 1;
    } else if(A[r][c] == 'O') {
      v |= 2;
    } else if(A[r][c] == '.') {
      v |= 4;
    }
  }
  if(__builtin_popcount(v) > 1) {
    v &= 4;
  }
  return v;
}

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    for(int i = 0; i < 4; i++) {
      cin >> A[i];
    }
    int v = check(0, 0, 0, 1) | check(1, 0, 0, 1) |
            check(2, 0, 0, 1) | check(3, 0, 0, 1) |
            check(0, 0, 1, 0) | check(0, 1, 1, 0) |
            check(0, 2, 1, 0) | check(0, 3, 1, 0) |
            check(0, 0, 1, 1) | check(3, 0, -1, 1);

    cout << "Case #" << t << ": ";
    if(v & 1) {
      cout << "X won" << endl;
    } else if(v & 2) {
      cout << "O won" << endl;
    } else if(v & 4) {
      cout << "Game has not completed" << endl;
    } else {
      cout << "Draw" << endl;
    }
  }
  return 0;
}
