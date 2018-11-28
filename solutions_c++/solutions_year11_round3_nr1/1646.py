#include <iostream>
using namespace std;

int T;
int R, C;
char tile[55][55];

int main() {
  cin >> T;
  for (int t =1; t<=T; t++) {
    cout << "Case #" << t << ":"<< endl;
    cin >> R >> C;
    bool solved = true;
    for (int r = 0; r<R; r++) {
      for (int c = 0; c<C; c++) {
        cin >> tile[r][c];
      }
    }
    for (int r=0; r<R; r++) {
      for (int c=0; c<C; c++) {
        if (tile[r][c] == '#') {
          // replace it with red tiles
          if (r<R-1 and c<C-1 and tile[r][c+1] == '#' and tile[r+1][c]=='#' and tile[r+1][c+1]=='#') {
            tile[r][c] = '/';
            tile[r][c+1] = '\\';
            tile[r+1][c]= '\\';
            tile[r+1][c+1] = '/';
          } else {
            cout << "Impossible" << endl;
            solved = false;
            goto END;
          }
        }
      }
    }
  END:
    if (solved) {
      for (int r = 0; r<R; r++) {
        for (int c = 0; c<C; c++) {
          cout << tile[r][c];
        }
        cout << endl;
      }
    }
  }
}
      
