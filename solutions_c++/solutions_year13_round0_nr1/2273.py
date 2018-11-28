#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool check(vector<char> grid, char symb, int a, int b, int c, int d) {
  bool ans = ( (grid[a] == symb || grid[a] == 'T') && (grid[b] == symb || grid[b] == 'T') && (grid[c] == symb || grid[c] == 'T') && (grid[d] == symb || grid[d] == 'T') );
  return ans;
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    string line;
    getline(cin, line); // blank or ignore()
    vector<char> grid(16);
    // read in each line and fill vector
    bool finished = true;
    for (int i = 0; i < 4; i++) {
      getline(cin, line);
      for (int j = 0; j < 4; j++) {
        grid[i * 4 + j] = line[j];
        if (line[j] == '.')
          finished = false;
      }
    }
    string ans;
    // check X win
    if (check(grid, 'X', 0, 1, 2, 3) || check(grid, 'X', 4, 5, 6, 7) || check(grid, 'X', 8, 9, 10, 11) || check(grid, 'X', 12, 13, 14, 15) || check(grid, 'X', 0, 4, 8, 12) || check(grid, 'X', 1, 5, 9, 13) || check(grid, 'X', 2, 6, 10, 14) || check(grid, 'X', 3, 7, 11, 15) || check(grid, 'X', 0, 5, 10, 15) || check(grid, 'X', 3, 6, 9, 12) )
      ans = "X won";
    else if (check(grid, 'O', 0, 1, 2, 3) || check(grid, 'O', 4, 5, 6, 7) || check(grid, 'O', 8, 9, 10, 11) || check(grid, 'O', 12, 13, 14, 15) || check(grid, 'O', 0, 4, 8, 12) || check(grid, 'O', 1, 5, 9, 13) || check(grid, 'O', 2, 6, 10, 14) || check(grid, 'O', 3, 7, 11, 15) || check(grid, 'O', 0, 5, 10, 15) || check(grid, 'O', 3, 6, 9, 12) )
      ans = "O won";
    else if (finished)
      ans = "Draw";
    else if (!finished)
      ans = "Game has not completed";
    else
      ans = "Error";
    cout << "Case #" << t+1 << ": " << ans << endl;
  }
  return 0;
}
