#include <iostream>
#include <string>
#include <vector> 

using namespace std;

int isX(vector<string> rows, int row, int col) {
  if (rows[row].c_str()[col] == 'X') {
    return true;
  }

  if (rows[row].c_str()[col] == 'T') {
    return true;
  }

  return false;
}

int isO(vector<string> rows, int row, int col) {
  if (rows[row].c_str()[col] == 'O') {
    return true;
  }
  
  if (rows[row].c_str()[col] == 'T') {
    return true;
  }

  return false;
}

int hasEmpty(vector<string> rows) {
  for (int i=0; i<4; i++)
    for (int j=0; j<4; j++)
      if (rows[i].c_str()[j] == '.')
        return true;

  return false;
}

int main() {
  int cases;
  vector<string> rows(4);

  cin >> cases;
  for (int i=0; i<cases; i++) {
    bool Owin = false;
    bool Xwin = false;

    cin >> rows[0] >> rows[1] >> rows[2] >> rows[3];    

    // Try the verticals.
    for (int k=0; k<4; k++) {    
      if (isX(rows, 0, k) && isX(rows, 1, k) && isX(rows, 2, k) && isX(rows, 3, k))
        Xwin = true; 
      if (isO(rows, 0, k) && isO(rows, 1, k) && isO(rows, 2, k) && isO(rows, 3, k))
        Owin = true;
    }
   

    // Try horizontals.
    for (int j=0; j<4; j++) { 
      if (isX(rows, j, 0) && isX(rows, j, 1) && isX(rows, j, 2) && isX(rows, j, 3))
        Xwin = true;
      if (isO(rows, j, 0) && isO(rows, j, 1) && isO(rows, j, 2) && isO(rows, j, 3))
        Owin = true;
    }

    // Upwards diag    
    if (isX(rows, 0, 3) && isX(rows, 1, 2) && isX(rows, 2, 1) && isX(rows, 3, 0))
      Xwin = true;
    if (isO(rows, 0, 3) && isO(rows, 1, 2) && isO(rows, 2, 1) && isO(rows, 3, 0))
      Owin = true;

    // Downwards diag    
    if (isX(rows, 0, 0) && isX(rows, 1, 1) && isX(rows, 2, 2) && isX(rows, 3, 3))
      Xwin = true;
    if (isO(rows, 0, 0) && isO(rows, 1, 1) && isO(rows, 2, 2) && isO(rows, 3, 3))
      Owin = true;

    cout << "Case #" << (i + 1) << ": ";

    if (!Xwin && !Owin) {
      if (hasEmpty(rows)) {
        cout << "Game has not completed\n";
      } else {
        cout << "Draw\n";
      }
    }

    if (Xwin && !Owin) {
      cout << "X won\n";
    }

    if (!Xwin && Owin) {
      cout << "O won\n";
    }

    if (Xwin && Owin) {
      cout << "Draw\n";
    }
  }

  return 0;
}
