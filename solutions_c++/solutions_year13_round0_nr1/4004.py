// #include <assert.h>

#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
//#include <unordered_map>
#include <vector>

using namespace std;

#define FOR(i, n) for (int i = 0; i < n; ++i)
#define FOR_(i, n) for (int i = n - 1; i >= 0; --i)

int FindWinner(const vector<string> & board) {
  bool filled = true;
  for (int i = 0; i < 4; ++i)
    for (int j = 0; j < 4; ++j)
      if (board[i][j] != 'X' && board[i][j] != 'O' && board[i][j] != 'T')
        filled = false;

  // check rows X
  for (int i = 0; i < 4; ++i) {
    bool b = true;
    for (int j = 0; j < 4; ++j)
      if (board[i][j] != 'X' && board[i][j] != 'T')
        b = false;
    if (b == true)
      return 0;
  }

  // check columns X
  for (int i = 0; i < 4; ++i) {
    bool b = true;
    for (int j = 0; j < 4; ++j)
      if (board[j][i] != 'X' && board[j][i] != 'T')
        b = false;
    if (b == true)
      return 0;
  }

  // check diagonals X
  bool b = true;
  for (int j = 0; j < 4; ++j)
    if (board[j][j] != 'X' && board[j][j] != 'T')
      b = false;
  if (b == true)
    return 0;

  b = true;
  for (int j = 0; j < 4; ++j)
    if (board[j][3-j] != 'X' && board[j][3-j] != 'T')
      b = false;
  if (b == true)
    return 0;

  // check rows O
  for (int i = 0; i < 4; ++i) {
    bool b = true;
    for (int j = 0; j < 4; ++j)
      if (board[i][j] != 'O' && board[i][j] != 'T')
        b = false;
    if (b == true)
      return 1;
  }

  // check columns O
  for (int i = 0; i < 4; ++i) {
    bool b = true;
    for (int j = 0; j < 4; ++j)
      if (board[j][i] != 'O' && board[j][i] != 'T')
        b = false;
    if (b == true)
      return 1;
  }

  // check diagonals O
  b = true;
  for (int j = 0; j < 4; ++j)
    if (board[j][j] != 'O' && board[j][j] != 'T')
      b = false;
  if (b == true)
    return 1;

  b = true;
  for (int j = 0; j < 4; ++j)
    if (board[j][3-j] != 'O' && board[j][3-j] != 'T')
      b = false;
  if (b == true)
    return 1;

  // Check a draw.
  if (filled == true)
    return 2;

  // Not completed.
  return 3;

}

int main () {
  ifstream in_("A-large.in");
  ofstream out_("out");
  int n;
  in_ >> n;
  vector<vector<string> > v;
  vector<string> w;
  string s;
  string dummy = " ";
  w.push_back(dummy);
  v.push_back(w);
  in_.ignore();
  for (int i = 1; i <= n; ++i) {
    vector<string> rows;
    for (int j = 0; j < 4; ++j) {
      getline(in_, s);
      rows.push_back(s);
    }
    v.push_back(rows);
    getline(in_, dummy);
  }
  // End of input.

  vector<int> states;
  states.push_back(0);
  for (int i = 1; i <= n; ++i) {
    states.push_back(FindWinner(v[i]));
  }


  string s0 = "X won";
  string s1 = "O won";
  string s2 = "Draw";
  string s3 = "Game has not completed";
  vector<string> output;
  output.push_back("");
  for (int i = 1; i <= n; ++i) {
    switch (states[i]) {
    case 0:
      output.push_back(s0);
      break;
    case 1:
      output.push_back(s1);
      break;
    case 2:
      output.push_back(s2);
      break;
    case 3:
      output.push_back(s3);
      break;
    default:
      break;
    }
  }

  for (int i = 1; i <= n; ++i) {
    stringstream ss;
    ss << i;
    string s1("Case #");
    string s2;
    ss >> s2;
    string s3(": ");

    output[i] = s1 + s2 + s3 + output[i];
  }

  for (int i = 1; i <= n; ++i) {
    out_ << output[i] << endl;
  }
  in_.close();
  out_.close();

  return 0;
}
