#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>
#include <numeric>

using namespace std;

map <char, string> pattern;

bool check(int x, int y, int n, vector <string> &board) {
  int i, j;
  for (i=0; i<n; i++) {
    char cur = board[x+i][y];
    if (i > 0)
      if (cur == board[x+i-1][y])
        return false;
    for (j=0; j<n; j++) {
      if (board[x+i][y+j] == '.')
        return false;
      if (board[x+i][y+j] != cur)
        return false;
      cur = ((cur - '0') + 1) % 2 + '0';
    }
  }

  return true;
}

void cut(int x, int y, int n, vector <string> &board) {
  int i, j;
  for (i=0; i<n; i++)
    for (j=0; j<n; j++)
      board[x+i][y+j] = '.';
  return;
}

vector <pair <int, int> >  solve(vector <string> board) {
  vector <pair <int, int> > ret;
  int most = min(board.size(), board[0].size());
  int i, j, k;

  for (i=most; i>=1; i--) {
    int num = 0;
    for (j=0; j<=board.size()-i; j++) {
      for (k=0; k<=board[0].size()-i; k++) {
        if (check(j, k, i, board)) {
          cut(j, k, i, board);
          num++;
        }
      }
    }

//     for (int jjj=0; jjj<board.size(); jjj++)
//       cout << board[jjj] << endl;
//     cout << i << " " << num << endl;

    if (num > 0)
      ret.push_back(make_pair(i, num));
  }

//   for (i=0; i<ret.size(); i++)
//     cout << ret[i].first << ", " << ret[i].second << endl;

  return ret;
}

int main(void) {
  int probNum, i, j, k;
  string line;

  pattern['0'] = "0000";
  pattern['1'] = "0001";
  pattern['2'] = "0010";
  pattern['3'] = "0011";
  pattern['4'] = "0100";
  pattern['5'] = "0101";
  pattern['6'] = "0110";
  pattern['7'] = "0111";
  pattern['8'] = "1000";
  pattern['9'] = "1001";
  pattern['A'] = "1010";
  pattern['B'] = "1011";
  pattern['C'] = "1100";
  pattern['D'] = "1101";
  pattern['E'] = "1110";
  pattern['F'] = "1111";

  cin >> probNum;

  for (i=0; i<probNum; i++) {
    int N, M;
    vector <string> board;
    cin >> N >> M;
    cin.ignore();

    for (j=0; j<N; j++) {
      string tmp;
      getline(cin, line);
      for (k=0; k<M/4; k++)
        tmp += pattern[line[k]];
      board.push_back(tmp);
    }

    vector <pair <int, int> > res = solve(board);
    cout << "Case #" << i + 1 << ": " << res.size() << endl;
    for (j=0; j<res.size(); j++)
      cout << res[j].first << " " << res[j].second << endl;
  }

  return 0;
}
