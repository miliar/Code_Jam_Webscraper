#include <iostream>

using namespace std;

void solve(int t) {
  int r, c; cin >> r >> c;
  printf("Case #%d:\n", t);
  
  cin.ignore();
  char board[51][51]; memset(board, 0, sizeof board);
  
  for (int y = 0; y < r; y++) {
    string s;
    scanf("%s", board[y]);
  }
  
  for (int y = 0; y < r; y++) {
    for (int x = 0; x < c; x++) {
      if ((board[y][x] == '#') &&
          (board[y+1][x] == '#') &&
          (board[y][x+1] == '#') &&
          (board[y+1][x+1] == '#')) {
            board[y][x] = '/';
            board[y+1][x] = '\\';
            board[y][x+1] = '\\';
            board[y+1][x+1] = '/';
      }
    }
  }

  for (int y = 0; y < r; y++) {
    for (int x = 0; x < c; x++) {
      if (board[y][x] == '#') {
        printf("Impossible\n");
        return;
      }
    }
  }

  for (int y = 0; y < r; y++) {
    printf("%s\n", board[y]);
  }  
}

int main() {
  int t; cin >> t;
  for(int i=1;i<=t;i++) solve(i);
}