
#include<iostream>
#include<sstream>
#include<string>
#include<map>
#include<vector>



void tick(int row, int col, int &rc, int *cc, int *dc) {
  rc++;
  cc[col]++;
  if (col == row) {
    dc[0]++;
  } 
  if (col == 3-row) {
    dc[1]++;
  }
}

bool is_win(int *cc, int *dc) {
  return (cc[0] == 4 || cc[1] == 4 || cc[2] == 4 || cc[3] == 4 || dc[0] == 4 || dc[1] == 4);
}

int main() 
{
  using namespace std;

  int T = 0;
  cin >> T;

  std::string str;
  getline(cin, str);

  int i = 0;
  for (i=1;i<=T;i++) 
  {
    int ans = -1; // -1-> unfinish, 0-> X won, 1-> O won, 2-> Draw, 3-> not completed

    int x_col[4] = {0,0,0,0};
    int o_col[4] = {0,0,0,0};
    int x_diag[2] = {0,0};
    int o_diag[2] = {0,0};
    bool is_complete = true;

    for (int row=0; row<4; row++) {
      getline(cin, str); // read line
      if (ans >= 0) continue; // we have an answer

      int x_row = 0;
      int o_row = 0;
      for (int col=0; col<4; col++) {
        if (str[col] == 'X') {
          tick(row, col, x_row, x_col, x_diag);
        } else if (str[col] == 'O') {
          tick(row, col, o_row, o_col, o_diag);
        } else if (str[col] == 'T') {
          tick(row, col, x_row, x_col, x_diag);
          tick(row, col, o_row, o_col, o_diag);
        } else {
          is_complete = false;
        }
      }

      if (x_row == 4) {
        ans = 0;
      } else if (o_row == 4) {
        ans = 1;
      }
    }

    getline(cin, str); // empty line

    if (ans < 0) { //not know yet
      if (is_win(x_col, x_diag)) { // if x win
        ans =  0;
      } else if (is_win(o_col, o_diag)) { // if o win
        ans = 1;
      } else if (is_complete) { // if all cell complete
        ans = 2; 
      } else {
        ans = 3;
      }
    }

    // Print answer
    cout << "Case #" << i << ": ";
    switch (ans) {
      case 0: 
        cout << "X won";
        break;
      case 1: 
        cout << "O won";
        break;
      case 2: 
        cout << "Draw";
        break;
      case 3: 
        cout << "Game has not completed";
        break;
    }
    cout << endl;
  }
}

