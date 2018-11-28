#include<iostream>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main() {
  int T;
  string tiles[50];
  cin >> T;
  for (int t = 0; t < T; t++) {
    int R, C;
    cin >> R >> C;
    for (int r = 0; r < R; r++) {
      cin >> tiles[r];
    }
    bool possible = true;
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (tiles[r][c] == '#') {
          if (r <= R - 2 && c <= C - 2 && tiles[r + 1][c] == '#' && tiles[r][c + 1] == '#' && tiles[r + 1][c + 1] == '#') {
            tiles[r][c] = tiles[r + 1][c + 1] = '/';
            tiles[r][c + 1] = tiles[r + 1][c] = '\\';
          } else {
            possible = false;
            break;
          }
        } 
      }
      if (!possible)
        break;
    }
    printf("Case #%d:\n", t + 1);
    if (possible) {
      for (int r = 0; r < R; r++)
        cout << tiles[r] << endl;
    } else cout << "Impossible" << endl;
  }  
  return 0;
}
