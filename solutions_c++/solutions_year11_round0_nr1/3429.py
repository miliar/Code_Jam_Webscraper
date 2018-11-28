#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
  int T; 
  cin >> T;
  for (int test = 1; test <= T; test++) {
    int bp = 1, op = 1, N, sec = 0, oi = 0, bi = 0, dif, dif2;
    char col[100];
    vector<int> o, b;
    cin >> N;
    for (int i = 0; i < N; i++) {
      int p;
      char r;
      cin >> r >> p;
      if (r == 'O') {
        o.push_back(p);
        col[i] = 'o';
      } else {
        b.push_back(p);
        col[i] = 'b';
      }
    }
    while (oi != o.size() || bi != b.size()) {
      dif2 = 0;
      if (col[oi + bi] == 'o') {
        dif = abs(o[oi] - op);
        if (bi != b.size()) {
          dif2 = abs(b[bi] - bp);
          if (dif2 > dif + 1) {
            dif2 = dif + 1;
          }
          if (b[bi] > bp) {
            bp += dif2;
          } else {
            bp -= dif2;
          }
        }
        op = o[oi];
        oi++;
      } else {
        dif = abs(b[bi] - bp);
        if (oi != o.size()) {
          dif2 = abs(o[oi] - op);
          if (dif2 > dif + 1) {
            dif2 = dif + 1;
          }
          if (o[oi] > op) {
            op += dif2;
          } else {
            op -= dif2;
          }
        }
        bp = b[bi];
        bi++;
      }
      //cout << "O moved to " << op << endl;
      //cout << "B moved to " << bp << endl;
      //cout << "Primary movement: " << dif << ", secondary: " << dif2 << endl;
      sec += dif + 1;
      //cout << "Time elapsed: " << sec << endl;
    }
    cout << "Case #" << test << ": " << sec << endl;
  }
  return 0;
}

