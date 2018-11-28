#include <algorithm>
#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

const int MAX = 505;
char grid[MAX][MAX+1];
int cumx[MAX][MAX+1], cumy[MAX][MAX+1];

int calcsum(int *cum, int a, int b) {
  return cum[b] - (a > 0 ? cum[a-1] : 0);
}

bool ok(int y1, int x1, int size) {
  long long massx = 0, massy = 0;
  for (int d=0; d<size; ++d) {
    int a = 0, b = size-1;
    if (d == 0 || d == size-1) ++a, --b;
    massy += (size - 2*d - 1) * calcsum(cumx[y1+d], x1+a, x1+b);
    massx += (size - 2*d - 1) * calcsum(cumy[x1+d], y1+a, y1+b);
  }
  return massx == 0 && massy == 0;
}

int main(void) {
  cin.sync_with_stdio(0);

  int CASES; cin >> CASES;
  for (int tt=1; tt<=CASES; ++tt) { // caret here
    int R, C, D;
    cin >> R >> C >> D;
    for (int i=0; i<R; ++i) {
      cin >> grid[i];
      for (int j=0; j<C; ++j) {
        grid[i][j] -= '0';
      }
    }

    for (int y=0; y<R; ++y) {
      for (int x=0; x<C; ++x) {
        cumy[x][y] = grid[y][x];
        if (y > 0) cumy[x][y] += cumy[x][y-1];

        cumx[y][x] = grid[y][x];
        if (x > 0) cumx[y][x] += cumx[y][x-1];
      }
    }

    int result = 0;
    for (int size=min(R, C); size>=3; --size) {
      for (int y1=0; y1<=R-size; ++y1) {
        for (int x1=0; x1<=C-size; ++x1) {
          if (ok(y1, x1, size)) {
            result = size;
            goto done;
          }
        }
      }
    }

done:
    cout << "Case #" << tt << ": ";
    if (result) {
      cout << result << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}
