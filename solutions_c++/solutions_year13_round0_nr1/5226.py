#include <iostream>
using namespace std;

int main() {
  int T; cin >> T; string line;
  char grid[4][4];
  for (int caseNum = 1; caseNum <= T; ++caseNum) {
    for (int i = 0; i < 4; ++i) {
      cin >> line;
      for (int j = 0; j < 4; ++j) grid[i][j] = line[j];
    }
    bool xWin = false, oWin = false;
    int xCt, oCt, tCt;
    for (int i = 0; i < 4 && !xWin && !oWin; ++i) {
      xCt = 0; oCt = 0; tCt = 0;
      for (int j = 0; j < 4; ++j) {
        if (grid[i][j] == 'X') xCt++;
        else if (grid[i][j] == 'O') oCt++;
        else if (grid[i][j] == 'T') tCt++;
      }
      if (xCt == 4 || (xCt == 3 && tCt == 1)) xWin = true;
      if (oCt == 4 || (oCt == 3 && tCt == 1)) oWin = true;
    }
    if (xWin || oWin) {
      cout << "Case #" << caseNum << ": " << (xWin ? "X" : "O") << " won" << endl;
      continue;
    }
    xWin = false; oWin = false;
    for (int j = 0; j < 4; ++j) {
      xCt = 0; oCt = 0; tCt = 0;
      for (int i = 0; i < 4; ++i) {
        if (grid[i][j] == 'X') xCt++;
        else if (grid[i][j] == 'O') oCt++;
        else if (grid[i][j] == 'T') tCt++;
      }
      if (xCt == 4 || (xCt == 3 && tCt == 1)) xWin = true;
      if (oCt == 4 || (oCt == 3 && tCt == 1)) oWin = true;
    }
    if (xWin || oWin) {
      cout << "Case #" << caseNum << ": " << (xWin ? "X" : "O") << " won" << endl;
      continue;
    }
    xCt = 0; oCt = 0; tCt = 0;
    for (int i = 0; i < 4; ++i) {
      if (grid[i][i] == 'X') xCt++;
      else if (grid[i][i] == 'O') oCt++;
      else if (grid[i][i] == 'T') tCt++;
    }
    if (xCt == 4 || (xCt == 3 && tCt == 1)) xWin = true;
    if (oCt == 4 || (oCt == 3 && tCt == 1)) oWin = true;
    if (xWin || oWin) {
      cout << "Case #" << caseNum << ": " << (xWin ? "X" : "O") << " won" << endl;
      continue;
    }
    xCt = 0; oCt = 0; tCt = 0;
    for (int i = 0; i < 4; ++i) {
      if (grid[i][3 - i] == 'X') xCt++;
      else if (grid[i][3 - i] == 'O') oCt++;
      else if (grid[i][3 - i] == 'T') tCt++;
    }
    if (xCt == 4 || (xCt == 3 && tCt == 1)) xWin = true;
    if (oCt == 4 || (oCt == 3 && tCt == 1)) oWin = true;
    if (xWin || oWin) {
      cout << "Case #" << caseNum << ": " << (xWin ? "X" : "O") << " won" << endl;
      continue;
    }
    bool draw = true;
    for (int i = 0; i < 4 && draw; ++i) {
      for (int j = 0; j < 4 && draw; ++j) {
        if (grid[i][j] == '.') {
          draw = false;
        }
      }
    }
    cout << "Case #" << caseNum << ": " << (draw ? "Draw" : "Game has not completed") << endl;
  }
}
