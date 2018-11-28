#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int z = 0; z < T; z++) {
    bool boardX [4][4];
    bool boardO [4][4];
    bool isDraw = true;
    for (int y = 0; y < 4; y++) {
      string line;
      cin >> line;
      for (int x = 0; x < 4; x++) {
        if (line[x] == '.') isDraw = false;
        if (line[x] == 'X' || line[x] == 'T')
          boardX[x][y] = true;
        else
          boardX[x][y] = false;
        if (line[x] == 'O' || line[x] == 'T')
          boardO[x][y] = true;
        else
          boardO[x][y] = false;
      }
    }
    bool wonX = false;
    bool wonO = false;
    for (int y = 0; y < 4; y++) {
      bool rowX = true;
      bool rowO = true;
      for (int x = 0; x < 4; x++) {
        if (!boardX[x][y]) rowX = false;
        if (!boardO[x][y]) rowO = false;
      }
      if (rowX) wonX = true;
      if (rowO) wonO = true;
    }
    for (int x = 0; x < 4; x++) {
      bool rowX = true;
      bool rowO = true;
      for (int y = 0; y < 4; y++) {
        if (!boardX[x][y]) rowX = false;
        if (!boardO[x][y]) rowO = false;
      }
      if (rowX) wonX = true;
      if (rowO) wonO = true;
    }
    bool diagX = true;
    bool diagO = true;
    for (int i = 0; i < 4; i++) {
      if (!boardX[i][i]) diagX = false;
      if (!boardO[i][i]) diagO = false;
    }
    if (diagX) wonX = true;
    if (diagO) wonO = true;
    diagX = true;
    diagO = true;
    for (int i = 0; i < 4; i++) {
      if (!boardX[i][3-i]) diagX = false;
      if (!boardO[i][3-i]) diagO = false;
    }
    if (diagX) wonX = true;
    if (diagO) wonO = true;
    if (wonX) {
      cout << "Case #" << z+1 << ": " << "X won" << endl;
    } else if (wonO) {
      cout << "Case #" << z+1 << ": " << "O won" << endl;
    } else if (isDraw) {
      cout << "Case #" << z+1 << ": " << "Draw" << endl;
    } else {
      cout << "Case #" << z+1 << ": " << "Game has not completed" << endl;
    }
  }
}
