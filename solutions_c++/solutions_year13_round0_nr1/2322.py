#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <boost/lexical_cast.hpp>

using namespace std;

string solve(const vector<string>&);

int main(){
  int num_cases;
  string s;
  getline(cin,s);
  num_cases = boost::lexical_cast<int>(s);
  for(int i = 0; i < num_cases; i++){
    vector<string> board(5);
    for(int j = 0; j < 5; j++){
      getline(cin, board[j]);
    }
    string r = solve(board);
    cout << "Case #" << i+1 << ": " << r << endl;
  }
}

enum result {X, O, D};

result check_row(const vector<string>& board, int row) {
  bool is_determined = true;
  for(int i = 0; i < 4; i++) {
    if(board[row][i] == 'X' || board[row][i] == 'T') continue;
    else {
      is_determined = false; break;
    }
  }
  if(is_determined) return X;
  
  is_determined = true;
  for(int i = 0; i < 4; i++) {
    if(board[row][i] == 'O' || board[row][i] == 'T') continue;
    else {
      is_determined = false; break;
    }
  }
  if(is_determined) return O;
  else return D;
}

result check_col(const vector<string>& board, int row) {
  bool is_determined = true;
  for(int i = 0; i < 4; i++) {
    if(board[i][row] == 'X' || board[i][row] == 'T') continue;
    else {
      is_determined = false; break;
    }
  }
  if(is_determined) return X;
  
  is_determined = true;
  for(int i = 0; i < 4; i++) {
    if(board[i][row] == 'O' || board[i][row] == 'T') continue;
    else {
      is_determined = false; break;
    }
  }
  if(is_determined) return O;
  else return D;
}

result check_diag_back_slash(const vector<string>& board) {
  bool is_determined = true;
  for(int i = 0; i < 4; i++) {
    if(board[i][i] == 'X' || board[i][i] == 'T') continue;
    else {
      is_determined = false; break;
    }
  }
  if(is_determined) return X;
  
  is_determined = true;
  for(int i = 0; i < 4; i++) {
    if(board[i][i] == 'O' || board[i][i] == 'T') continue;
    else {
      is_determined = false; break;
    }
  }
  if(is_determined) return O;
  else return D;
}

result check_diag_slash(const vector<string>& board) {
  bool is_determined = true;
  for(int i = 0; i < 4; i++) {
    if(board[i][3-i] == 'X' || board[i][3-i] == 'T') continue;
    else {
      is_determined = false; break;
    }
  }
  if(is_determined) return X;
  
  is_determined = true;
  for(int i = 0; i < 4; i++) {
    if(board[i][3-i] == 'O' || board[i][3-i] == 'T') continue;
    else {
      is_determined = false; break;
    }
  }
  if(is_determined) return O;
  else return D;
}

bool is_draw(const vector<string>& board) {
  for(int i = 0; i < 4; i++) {
    for(int j = 0; j < 4; j++) {
      if(board[i][j] == '.') return false;
    }
  }
  return true;
}

string solve(const vector<string>& board){
  result r;
  for(int i = 0; i < 4; i++) {
    r = check_row(board,i);
    if(r == X) return "X won";
    if(r == O) return "O won";
  }
  for(int i = 0; i < 4; i++) {
    r = check_col(board,i);
    if(r == X) return "X won";
    if(r == O) return "O won";
  }
  r = check_diag_back_slash(board);
  if(r == X) return "X won";
  if(r == O) return "O won";
  r = check_diag_slash(board);
  if(r == X) return "X won";
  if(r == O) return "O won";
  if(is_draw(board)) return "Draw";
  else return "Game has not completed";
}
