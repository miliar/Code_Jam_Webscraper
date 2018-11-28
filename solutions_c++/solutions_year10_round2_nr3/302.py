#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>
#include <memory.h>

using namespace std;

// last, cnt
int data[1000][100];

int C[1000][1000];

int main() {

  C[0][0] = 1;
  for (int i = 1; i < 1000; i++) {
    C[i][0] = 1;
    for (int j = 1; j <= i; j++)
      C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % 100003 ;
  }

  int _t; cin >> _t;
  for (int _tt = 1; _tt <= _t; _tt++) {
    cout << "Case #" << _tt << ": ";
    int n; cin >> n;

    memset(data, 0, sizeof (data));
    data[1][0] = 1;

    for (int i = 2; i <= n; i++) {
      for (int size = 1; size < i; size++) {
        int j = size;
        for (int skip = 0; size - skip - 1 >= 0 && skip < i - j; skip++) {
          int add = C[i - j - 1][skip] * data[j][size - skip - 1];
          data[i][size] = (data[i][size] + add) % 100003;
        }
      }
    }

    int r = 0;
    for (int size = 1; size < n; size++)
      r = (r + data[n][size]) % 100003;
    cout << r << endl;
  }

  return 0;
}
