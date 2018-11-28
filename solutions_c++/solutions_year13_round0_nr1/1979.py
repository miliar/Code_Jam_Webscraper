#include <string>
#include <iostream>
#include <vector>
using namespace std;

int XCount(char c)
{
  return ((c == 'X') || (c == 'T')) ? 1 : 0;
}

int OCount(char c)
{
  return ((c == 'O') || (c == 'T')) ? 1 : 0;
}

string CheckBoard(vector<string> &board)
{
  int diag1_x = 0, diag1_o = 0, diag2_x = 0, diag2_o = 0;
  for (int j = 0; j < 4; ++j)
  {
    int row_x = 0, row_o = 0, col_x = 0, col_o = 0;
    for (int i = 0; i < 4; ++i)
    {
      row_x += XCount(board[j][i]);
      row_o += OCount(board[j][i]);
      col_x += XCount(board[i][j]);
      col_o += OCount(board[i][j]);
    }
			    
    if ((row_x == 4) || (col_x == 4)) return "X won";
    if ((row_o == 4) || (col_o == 4)) return "O won";

    diag1_x += XCount(board[j][j]);
    diag1_o += OCount(board[j][j]);
    diag2_x += XCount(board[j][3 - j]);
    diag2_o += OCount(board[j][3 - j]);
  }
  if ((diag1_x == 4) || (diag2_x == 4)) return "X won";
  if ((diag1_o == 4) || (diag2_o == 4)) return "O won";

  int periods = 0;
  for (int j = 0; j < 4; ++j)
    for (int i = 0; i < 4; ++i)
      if (board[j][i] == '.')
	++periods;
  if (periods == 0)
    return "Draw";
  else
    return "Game has not completed";
}

int main()
{
  int T;
  cin >> T;
  for (int test_case = 1; test_case <= T; ++test_case)
  {
    vector<string> board(4);
    for (int row = 0; row < 4; ++row)
      cin >> board[row];

    cout << "Case #" << test_case << ": " << CheckBoard(board) << endl;
  }

  return 0;
}

