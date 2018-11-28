#include <iostream>

using namespace std;

int main (int arc, char** argv) {
  int N = 0;
  cin >> N;
  
  for (int n=0; n < N; n++) {
    bool foundDot = false;
    char* field = new char[16]();
    for (int i = 0; i < 16; i++) {
      cin >> field[i];
      if (field[i] == '.') {
        foundDot = true;
      }
    }
    int pointsX = 0;
    int pointsO = 0;
    //checkRows(field):
    for (int i = 0; i < 4; i++) {
      int row = i*4;
      if ((field[row + 0] == field[row + 1] && field[row + 0] == field[row + 2] && field[row + 0] == field[row + 3]) ||
          (field[row + 0] == field[row + 1] && field[row + 0] == field[row + 2] && field[row + 3] == 'T') ||
          (field[row + 0] == field[row + 1] && field[row + 0] == field[row + 3] && field[row + 2] == 'T') ||
          (field[row + 0] == field[row + 2] && field[row + 0] == field[row + 3] && field[row + 1] == 'T') ||
          (field[row + 1] == field[row + 2] && field[row + 1] == field[row + 3] && field[row + 0] == 'T')) {
        if (field[row + 0] == 'X' || field[row + 1] == 'X') {
          pointsX++;
        } else if (field[row + 0] == 'O' || field[row + 1] == 'O') {
          pointsO++;
        }
      }
    }
    //checkColumns(field);
    for (int i = 0; i < 4; i++) {
      int column = i;
      if (field[column + 0] == field[column + 4] && field[column + 0] == field[column + 8] && field[column + 0] == field[column + 12] ||
          (field[column + 0] == field[column + 4] && field[column + 0] == field[column + 8] && field[column + 12] == 'T') ||
          (field[column + 0] == field[column + 4] && field[column + 0] == field[column + 12] && field[column + 8] == 'T') ||
          (field[column + 0] == field[column + 8] && field[column + 0] == field[column + 12] && field[column + 4] == 'T') ||
          (field[column + 4] == field[column + 8] && field[column + 0] == field[column + 12] && field[column + 0] == 'T')) {
        if (field[column + 0] == 'X' || field[column + 4] == 'X') {
          pointsX++;
        } else if (field[column + 0] == 'O' || field[column + 4] == 'O') {
          pointsO++;
        }
      }
    }
    //checkDiagonals(field);
    char c1 = field[0];
    if (c1 == 'T') {
      c1 = field[5]; 
    }
    if (c1 != '.') {
      bool rightDiagonal = true;
      for (int i = 1; i < 4; i++) {
        int column = i;
        int row = i;
        if (field[row*4 + column] != c1 && field[row*4 + column] != 'T') {
          rightDiagonal = false;
          break;
        }
      }
      if (rightDiagonal) {
        if (c1 == 'X' || field[5] == 'X') {
          pointsX++;
        } else if (c1 == 'O' || field[5] == 'O') {
          pointsO++;
        }
      }
    }
    char c2 = field[3];
    if (c2 == 'T') {
      c2 = field[6]; 
    }
    if (c2 != '.') {
      bool leftDiagonal = true;
      for (int i = 1; i < 4; i++) {
        int column = (3 - i);
        int row = i;
        if (field[row*4 + column] != c2 && field[row*4 + column] != 'T') {
          leftDiagonal = false;
          break;
        }
      }
      if (leftDiagonal) {
        if (c2 == 'X' || field[6] == 'X') {
          pointsX++;
        } else if (c2 == 'O' || field[6] == 'O') {
          pointsO++;
        }
      }
    }
    cout << "Case #" << (n+1) << ": ";
    if (pointsX == pointsO && foundDot) {
      cout << "Game has not completed" << endl;
    } else if (pointsX == pointsO) {
      cout << "Draw" << endl;
    } else if (pointsX > pointsO) {
      cout << "X won" << endl;
    } else {
      cout << "O won" << endl;
    }
  }
}

