#include <iostream>
#include <string>
#include <vector>
#include <cassert>

using namespace std;
const int DIMENSION = 4;


char judgement(const string& str)
{
  assert(0 == DIMENSION-str.length());
  if (string::npos == str.find_first_not_of("XT")) {
    return 'X';
  } else if (string::npos == str.find_first_not_of("OT")) {
    return 'O';
  }

  return 0;
}


int main(void)
{
  int testcase;
  cin >> testcase;

  for (int tc = 1; tc <= testcase; tc++) {
    bool full = true;
    vector<string> board;
    for (int i = 0; i < DIMENSION; i++) {
      string line;
      cin >> line;
      assert((0 == DIMENSION-line.length()) && (string::npos == line.find_first_not_of("XOT.")));
      board.push_back(line);
      if (full && (string::npos != line.find_first_of('.'))) {
        full = false;
      }
    }

    bool found = false;
    for (int i = 0; i < DIMENSION; i++) {
      char c = judgement(board[i]);
      if (c) {
        cout << "Case #" << tc << ": " << c << " won" << endl;
        found = true;
        break;
      }
    }

    for (int i = 0; (! found) && (i < DIMENSION); i++) {
      string col;
      for (int j = 0; j < DIMENSION; j++) {
        col.push_back(board[j][i]);
      }

      char c = judgement(col);
      if (c) {
        cout << "Case #" << tc << ": " << c << " won" << endl;
        found = true;
        break;
      }
    }

    if (! found) {
      string diagonal;
      for (int i = 0; (! found) && (i < DIMENSION); i++) {
        diagonal.push_back(board[i][i]);
      }

      char c = judgement(diagonal);
      if (c) {
        cout << "Case #" << tc << ": " << c << " won" << endl;
        found = true;
      }
    }

    if (! found) {
      string diagonal;
      for (int i = 0; (! found) && (i < DIMENSION); i++) {
        diagonal.push_back(board[i][DIMENSION-i-1]);
      }

      char c = judgement(diagonal);
      if (c) {
        cout << "Case #" << tc << ": " << c << " won" << endl;
        found = true;
      }
    }

    if (! found) {
      if (full) {
        cout << "Case #" << tc << ": Draw" << endl;
      } else {
        cout << "Case #" << tc << ": Game has not completed" << endl;
      }
    }
  }

  return 0;
}

