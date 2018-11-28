#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {

  if(argc != 2) {
    cout << "please pass exactly one argument" << endl;
    exit(1);
  }
  ifstream input;
  input.open(argv[1]);
  int t(0);

  input >> t;
  vector<vector<int> > board(4, vector<int>(4,0));
  for(int i(0); i != t; ++i) {
      bool empty_cells(false);
      for(int j(0); j != 4; ++j) {
          for(int k(0); k != 4; ++k) {
              char temp_char;
              input >> temp_char;
              if(temp_char == '.') {
                  empty_cells = true;
              }
              board[j][k] = temp_char;
          }
      }
      bool x_is_done(false);
      bool o_is_done(false);
      //rows
      for(int j(0); j != 4; ++j) {
          int x_in_a_row(0);
          int o_in_a_row(0);
          for(int k(0); k != 4; ++k) {
              if(board[j][k] == 'X') ++x_in_a_row;
              if(board[j][k] == 'O') ++o_in_a_row;
              if(board[j][k] == 'T') {++x_in_a_row; ++o_in_a_row;}
          }
          if(x_in_a_row == 4) x_is_done = true;
          if(o_in_a_row == 4) o_is_done = true;
      }
      //columns
      for(int k(0); k != 4; ++k) {
          int x_in_a_row(0);
          int o_in_a_row(0);
          for(int j(0); j != 4; ++j) {
              if(board[j][k] == 'X') ++x_in_a_row;
              if(board[j][k] == 'O') ++o_in_a_row;
              if(board[j][k] == 'T') {++x_in_a_row; ++o_in_a_row;}
          }
          if(x_in_a_row == 4) x_is_done = true;
          if(o_in_a_row == 4) o_is_done = true;
      }
      //ul to lr
      int x_in_a_row(0);
      int o_in_a_row(0);
      for(int k(0); k != 4; ++k) {
          if(board[k][k] == 'X') ++x_in_a_row;
          if(board[k][k] == 'O') ++o_in_a_row;
          if(board[k][k] == 'T') {++x_in_a_row; ++o_in_a_row;}
      }
      if(x_in_a_row == 4) x_is_done = true;
      if(o_in_a_row == 4) o_is_done = true;
      //ur to lr
      x_in_a_row = 0;
      o_in_a_row = 0;
      for(int k(0); k != 4; ++k) {
          if(board[3-k][k] == 'X') ++x_in_a_row;
          if(board[3-k][k] == 'O') ++o_in_a_row;
          if(board[3-k][k] == 'T') {++x_in_a_row; ++o_in_a_row;}
      }
      if(x_in_a_row == 4) x_is_done = true;
      if(o_in_a_row == 4) o_is_done = true;

      cout << "Case #" << i+1 << ": ";
      if(x_is_done && o_is_done) {
          cout << "Draw";
      } else if(x_is_done) {
          cout << "X won";
      } else if(o_is_done) {
          cout << "O won";
      } else if(empty_cells) {
          cout << "Game has not completed";
      } else {
          cout << "Draw";
      }
      cout << endl;
  }

  input.close();
  return 0;
}
