/* Google Code Jam 2010, Round 1A, Problem A: "Rotate". */
/* Fri. May. 21, 2010, By: Samuel Tien-Chieh Huang. */
// Last update: Fri. May. 21, 2010.
#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

inline void maxim (int &d, int s) {if (d < s) d = s;}

int scan (vector <string> &ar, int n, int x, int y, int dx, int dy, int k) {
  int ret = 0, cur = 0;
  for (; (x >= 0) && (y >= 0) && (x < n) && (y < n); x += dx, y += dy) {
    if (ar [y][x] == k) cur ++; else cur = 0;
    maxim (ret, cur);
  }
  return ret;
}

int main (void) {
  int nc, ca;
  char col [2] = {'R', 'B'};
  string ans [4] = {"Neither", "Red", "Blue", "Both"};
  cin >> nc;
  for (ca = 1; ca <= nc; ca ++) {
    int n, k, i, j, c;
    cin >> n >> k;
    vector <string> br (n);
    for (i = 0; i < n; i ++) cin >> br [i];
    for (i = 0; i < n; i ++) {
      int tail = n - 1;
      for (j = n - 1; j >= 0; j --) {
        if (br [i][j] != '.') {
          br [i][tail] = br [i][j];
          tail --;
        }
      }
      for (; tail >= 0; tail --) br [i][tail] = '.';
    }
    vector <string> rot (br);
    for (i = 0; i < n; i ++) {  // Fetch.
      for (j = 0; j < n; j ++) rot [i][j] = br [n - 1 - j][i];
    }
    //for (i = 0; i < n; i ++) cout << rot [i] << endl;
    int sol [2] = {0, 0};
    for (i = 0; i < n; i ++) {
      for (j = 0; j < n; j ++) {
        for (c = 0; c < 2; c ++) {
          maxim (sol [c], scan (rot, n, j, i, 1, 0, col [c]));
          maxim (sol [c], scan (rot, n, j, i, 0, 1, col [c]));
          maxim (sol [c], scan (rot, n, j, i, 1, 1, col [c]));
          maxim (sol [c], scan (rot, n, j, i, 1, -1, col [c]));
        }
      }
    }
    //printf ("%d %d\n", sol [0], sol [1]);
    int mask = ((sol [0] >= k) ? 1 : 0) | ((sol [1] >= k) ? 2 : 0);
    printf ("Case #%d: %s\n", ca, ans [mask].c_str ());
  }
  return 0;
}
