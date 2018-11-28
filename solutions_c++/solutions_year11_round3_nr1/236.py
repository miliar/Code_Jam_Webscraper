#include <cstdio>
#include <iostream>

using namespace std;

int T, R, C;
char G[50][50];

int main() {
  cin >> T;
  for (int t = 0; t < T; ++t) {
    cin >> R >> C;
    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        cin >> G[r][c];
      }
    }
    
    // Greedily cover from [0,0] -> [0,C] and then down

    bool isPossible = true;
    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        if (G[r][c] == '#') {
          // Check if neighbors are tileable
          if ((r+1 < R) && (c+1 < C) && G[r][c+1] == '#'
             && G[r+1][c] == '#' && G[r+1][c+1] == '#') {
            G[r][c] = '/'; G[r][c+1]='\\'; G[r+1][c]='\\'; G[r+1][c+1] = '/';
          } else {
            isPossible = false;
            break;
          }
        }
      }
      if (!isPossible) {
        break;
      }
    }

    cout << "Case #" << t+1 << ":" << endl;
    if (!isPossible) {
      cout << "Impossible" << endl;
    }
    else {
      for (int r = 0; r < R; ++r) {
        for (int c = 0; c < C; ++c) {
          cout << G[r][c];
        }
        cout << endl;
      }
    }
  }

  return 0;
}
