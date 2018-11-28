//
//  Google Jam 2013
//
//  Problem: Qualif. A
//   
//  Author: Marçal Sola

#include <iostream>
#include <string>
#include <vector>

#define ROWS 4
#define COLS 4
#define TO_WIN 4

using namespace std;


int main (void) {
  
  int cases; 
  cin >> cases; 
  
  for (int ncase = 1; ncase <= cases; ncase++) {
    vector<int> ver_cont_x(COLS, 0);
    vector<int> hor_cont_x(ROWS, 0);
    int dia_lr_cont_x = 0;
    int dia_rl_cont_x = 0;

    vector<int> ver_cont_o(COLS, 0);
    vector<int> hor_cont_o(ROWS, 0);
    int dia_lr_cont_o = 0;
    int dia_rl_cont_o = 0;

    char sq; 
    bool filled = true; 
    int won = 0;
    for (int r = 0; r < ROWS; r++ ) {
      for (int c = 0; c < COLS; c++) {
        cin >> sq;
        //cout << "sq: " << sq << endl;
        // diagonals
        if (r == c) {
          //cout << "cont:" << dia_cont_x << " diacont+: " << (dia_cont_x + (sq == 'X' or sq == 'T')) << " win:" << (int)((dia_cont_x + (sq == 'X' or sq == 'T')) == TO_WIN) << endl;
          if ((dia_lr_cont_x += (sq == 'X' or sq == 'T')) == TO_WIN) {
            won = 1; 
          } 
          if ((dia_lr_cont_o += (sq == 'O' or sq == 'T')) == TO_WIN) {
            won = 2; 
          }
        }
        if (r == (COLS - c - 1)) {
          //cout << "cont:" << dia_cont_x << " diacont+: " << (dia_cont_x + (sq == 'X' or sq == 'T')) << " win:" << (int)((dia_cont_x + (sq == 'X' or sq == 'T')) == TO_WIN) << endl;
          if ((dia_rl_cont_x += (sq == 'X' or sq == 'T')) == TO_WIN) {
            won = 1; 
          } 
          if ((dia_rl_cont_o += (sq == 'O' or sq == 'T')) == TO_WIN) {
            won = 2; 
          }
        }
       
        if ((hor_cont_x[r] += (sq == 'X' or sq == 'T')) == TO_WIN) {
          won = 1;
        }
       
        if ((hor_cont_o[r] += (sq == 'O' or sq == 'T')) == TO_WIN) {
          won = 2;
        }
        if ((ver_cont_x[c] += (sq == 'X' or sq == 'T')) == TO_WIN) {
          won = 1;
        }
        if ((ver_cont_o[c] += (sq == 'O' or sq == 'T')) == TO_WIN) {
          won = 2;
        }
      if (sq == '.') filled = false; 
      }
    }
    
    // end
    if (won == 1) cout << "Case #" << ncase << ": X won" << endl;
    else if (won == 2) cout << "Case #" << ncase << ": O won" << endl;
    else if ( filled ) cout << "Case #" << ncase << ": Draw" << endl;
    else cout << "Case #" << ncase << ": Game has not completed" << endl;
  }

  return 0;
}
