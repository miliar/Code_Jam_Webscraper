#include <iostream>
#include <string>

using namespace std;

enum {N = 4};

string grid[N];
char PLAYERS[2] = {'X', 'O'};

void process(int tc);
bool checkRow(char player, int row);
bool checkCol(char player, int col);
bool checkDiags(char player);

int main() {
  int T;
  cin >> T;

  for (int i = 1; i <= T; i++) {
    process(i);
  }
  
  return 0;
}

void process(int tc) {
  for (int row = 0; row < N; row++) {
    cin >> grid[row];
  }

  for (int i = 0; i < 2; i++) {
    for (int row = 0; row < N; row++) {
      if (checkRow(PLAYERS[i], row)) {
        cout << "Case #" << tc << ": " << PLAYERS[i] << " won" << endl;
        return;
      }
    }
    for (int col = 0; col < N; col++) {
      if (checkCol(PLAYERS[i], col)) {
        cout << "Case #" << tc << ": " << PLAYERS[i] << " won" << endl;
        return;
      }
    }
    if (checkDiags(PLAYERS[i])) {
      cout << "Case #" << tc << ": " << PLAYERS[i] << " won" << endl;
      return;
    }
  }

  for (int row = 0; row < N; row++) {
    for (int col = 0; col < N; col++) {
      if (grid[row][col] == '.') {
        cout << "Case #" << tc << ": Game has not completed" << endl;
        return;
      }
    }
  }

  cout << "Case #" << tc << ": Draw" << endl;
}

bool checkRow(char player, int row) {
  for (int col = 0; col < N; col++) {
    if (grid[row][col] != player && grid[row][col] != 'T') {
      return false;
    }
  }
  return true;
}

bool checkCol(char player, int col) {
  for (int row = 0; row < N; row++) {
    if (grid[row][col] != player && grid[row][col] != 'T') {
      return false;
    }
  }
  return true;
}

bool checkDiags(char player) {
  bool left_diag = true;
  for (int i = 0; i < N; i++) {
    if (grid[i][i] != player && grid[i][i] != 'T') {
      left_diag = false;
      break;
    }
  }
  if (left_diag) {
    return true;
  }
  for (int i = 0; i < N; i++) {
    if (grid[i][N - i - 1] != player && grid[i][N - i - 1] != 'T') {
      return false;
    }
  }
  return true;
}

