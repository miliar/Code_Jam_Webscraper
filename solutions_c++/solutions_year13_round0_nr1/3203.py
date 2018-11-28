#include <iostream>
#include <string>
using namespace std;

bool all_is_color(char c, const string &s) {
  for (int i = 0; i < 4; i++)
    if (s[i] != 'T' && s[i] != c)
      return false;
  return true;
}

char check_someone_wins(const string board[4]) {
  for (int i = 0; i < 4; i++)
    if (all_is_color('X', board[i])) return 'X';
    else if (all_is_color('O', board[i])) return 'O';
  
  for (int i = 0; i < 4; i++) {
    string col = "....";
    col[0] = board[0][i]; col[1] = board[1][i]; col[2] = board[2][i]; col[3] = board[3][i];
    if (all_is_color('X', col)) return 'X';
    else if (all_is_color('O', col)) return 'O';
  }

  string diag1 = "....";
  diag1[0] = board[0][0];
  diag1[1] = board[1][1];
  diag1[2] = board[2][2];
  diag1[3] = board[3][3];
  if (all_is_color('X', diag1)) return 'X';
  else if (all_is_color('O', diag1)) return 'O';

  string diag2 = "....";
  diag2[0] = board[0][3]; diag2[1] = board[1][2]; diag2[2] = board[2][1]; diag2[3] = board[3][0];
  if (all_is_color('X', diag2)) return 'X';
  else if (all_is_color('O', diag2)) return 'O';
  
  return 0;
}

bool has_empty_cell(const string board[4]) {
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      if (board[i][j] == '.') return true;
  return false;
}

string won_string(char c) {
  string won = ". won";
  won[0] = c;
  return won;
}

string solve_case() {
  string board[4];
  cin >> board[0] >> board[1] >> board[2] >> board[3];
  char someone_wins = check_someone_wins(board);
  if (someone_wins) return won_string(someone_wins);
  if (has_empty_cell(board)) return "Game has not completed";
  return "Draw";
}

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": " << solve_case() << endl;
  }
  return 0;
}

