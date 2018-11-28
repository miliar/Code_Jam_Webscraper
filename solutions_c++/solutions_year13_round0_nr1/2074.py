#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isWinner (vector<string>& grid, char c, bool &gameOver) {
  // horizontal and vertical
  int d1 = 0, d2 = 0;
  for (int i = 0; i < 4; i++) {
    int l = 0;
    int k = 0;
    if (grid[i][i] == c || grid[i][i] == 'T')
      ++d1;
    if (grid[i][4-i-1] == c || grid[i][4-i-1] == 'T')
      ++d2;
    for (int j = 0; j < 4; j++) {
      if (grid[i][j] == c || grid[i][j] == 'T')
        ++l;
      if (grid[j][i] == c || grid[j][i] == 'T')
        ++k;
      if (grid[i][j] == '.')
        gameOver = false;
    }
    if (l == 4 || k == 4)
      return true;
  }
  if (d1 == 4 || d2 == 4)
    return true;

  return false;
}

int main ()
{
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    cout << "Case #" << t+1 << ": ";
    vector<string> grid(4);
    string line;
    for (int i = 0; i < 4; i++) {
      cin >> grid[i]; 
    }
    bool gameOver = true;
    bool xWins = isWinner(grid, 'X', gameOver);
    bool oWins;
    if (!xWins) {
      oWins = isWinner(grid, 'O', gameOver);
      if (oWins) {
        cout << "O won" << endl;
        continue;
      }
    }
    else {
      cout << "X won" << endl;
      continue;
    }
    if (!gameOver) {
      cout << "Game has not completed" << endl;
    }
    else {
      cout << "Draw" << endl;
    }
  }
}
