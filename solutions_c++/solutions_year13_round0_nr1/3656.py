#include <iostream>
#include <vector>

int check_status(int X, int O, int T, int status) {
  if (X * O == 0) {
    if (X == 4 || (X == 3 && T == 1)) { return 0; }
    else if (O == 4 || (O == 3 && T == 1)) { return 1; }
  }
  return status;
}

void solve() {
  int t;
  std::vector<std::string> board(4);
  std::cin >> t;
  for (int ti = 0; ti < t; ++ti) {
    int status = 3, Xh, Oh,Th, Xv, Ov, Tv, Xd0, Od0, Td0, Xd1, Od1, Td1;
    Xd0 = Od0 = Td0 = Xd1 = Od1 = Td1 = 0;
    bool empty_cell = false;
    for (int i = 0; i < 4; ++i) std::cin >> board[i];
    for (int i = 0; i < 4; ++i) {
      Xh = Oh = Th = Xv = Ov = Tv = 0;
      for (int j = 0; j < 4; ++j) {
        if (board[i][j] == 'X') { ++Xh; }
        else if (board[i][j] == 'O') { ++Oh; }
        else if (board[i][j] == '.') { empty_cell = true; }
        else { ++Th; }

        if (board[j][i] == 'X') { ++Xv; /*std::cout << board[j][i] << j << i;*/ }
        else if (board[j][i] == 'O') { ++Ov; }
        else if (board[j][i] == 'T') { ++Tv; }

        if (i == j) {
          if (board[i][j] == 'X') { ++Xd0; }
          else if (board[i][j] == 'O') { ++Od0; }
          else if (board[i][j] == 'T') { ++Td0; }
        }

        if (i + j == 3) {
          if (board[i][j] == 'X') { ++Xd1; }
          else if (board[i][j] == 'O') { ++Od1; }
          else if (board[i][j] == 'T') { ++Td1; }
        }
      }
      status = check_status(Xh, Oh, Th, status);
      status = check_status(Xv, Ov, Tv, status);
      //std::cout << Xv << "," << Ov << " ";
    }
    status = check_status(Xd0, Od0, Td0, status);
    status = check_status(Xd1, Od1, Td1, status);
    //std::cout << std::endl;
    if (status == 3 && !empty_cell) {
      status = 2;
    }
    std::cout << "Case #" << ti + 1 << ": ";
    switch (status) {
      case 0: std::cout << "X won\n"; break;
      case 1: std::cout << "O won\n"; break;
      case 2: std::cout << "Draw\n"; break;
      case 3: std::cout << "Game has not completed\n"; break;
    }
  }
}

int main(int argc, char *argv[]) {
  solve();
  return 0;
}
