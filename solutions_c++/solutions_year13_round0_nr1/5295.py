#include <iostream>
using namespace std;

enum { N, T, X, O };
enum { NOTDONE, DRAW, XWIN, OWIN };
int val[4] = {0, 0, 1, -1};

int b[4][4];

int get() {
  char c;
  while (true) {
    c = 0;
    cin >> c;
    switch(c) {
      case '.': return N;
      case 'T': return T;
      case 'X': return X;
      case 'O': return O;
    }
  }
}

int check(int n1, int n2, int n3, int n4) {
  bool hasT = n1 == T || n2 == T || n3 == T || n4 == T;
  int sum = val[n1] + val[n2] + val[n3] + val[n4];
  if (sum == 4 || hasT && sum == 3) return XWIN;
  if (sum == -4 || hasT && sum == -3) return OWIN;
  return NOTDONE;
}

int checkAll() {
  int w;
  for (int i = 0; i< 4; ++i) {
    w = check(b[i][0], b[i][1], b[i][2], b[i][3]);
    if (w != NOTDONE) return w;
    w = check(b[0][i], b[1][i], b[2][i], b[3][i]);
    if (w != NOTDONE) return w;
  }
  w = check(b[0][0], b[1][1], b[2][2], b[3][3]);
  if (w != NOTDONE) return w;
  w = check(b[0][3], b[1][2], b[2][1], b[3][0]);
  if (w != NOTDONE) return w;
  for (int i = 0; i < 4; ++i)
    for (int j = 0; j < 4; ++j)
      if (b[i][j] == N) return NOTDONE;
  return DRAW;
}


int main(void) {
  int t;
  cin >> t;
  for (int c = 1; c <= t; ++c) {
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j)
        b[i][j] = get();
    cout << "Case #" << c << ": ";
    switch (checkAll()) {
      case NOTDONE: cout << "Game has not completed"; break;
      case DRAW: cout << "Draw"; break;
      case XWIN: cout << "X won"; break;
      case OWIN: cout << "O won"; break;
    }
    cout << endl;
  }
}
