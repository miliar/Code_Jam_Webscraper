#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

typedef vector <   int  > vi;
typedef vector <   vi   > vvi;
typedef vector < double > vd;
typedef vector <   vd   > vvd;
typedef vector < string > vs;


bool xwon(char a, char b, char c, char d) {
  return ((a == 'X' || a == 'T') && (b == 'X' || b == 'T') && (c == 'X' || c == 'T') && (d == 'X' || d == 'T') );
}

bool owon(char a, char b, char c, char d) {
  return ((a == 'O' || a == 'T') && (b == 'O' || b == 'T') && (c == 'O' || c == 'T') && (d == 'O' || d == 'T') );
}

bool contains(const vector<string>& m, char c) {
  for (int i = 0; i < m.size(); ++i)
    for (int j = 0; j < m[i].length(); ++j) 
      if (m[i][j] == c)
        return true;

  return false;
}

int main () {
  vector<string> rows (4);

  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    for (int i = 0; i < 4; i++)
      cin >> rows[i];

    char whoWon = 'd';

    for (int i = 0; i < 4; i++) {
      if (xwon(rows[i][0], rows[i][1], rows[i][2], rows[i][3])) {
        whoWon = 'X';
        break;
      }
      if (owon(rows[i][0], rows[i][1], rows[i][2], rows[i][3])) {
        whoWon = 'O';
        break;
      }
    }

    for (int i = 0; i < 4; i++) {
      if (xwon(rows[0][i], rows[1][i], rows[2][i], rows[3][i])) {
        whoWon = 'X';
        break;
      }
      if (owon(rows[0][i], rows[1][i], rows[2][i], rows[3][i])) {
        whoWon = 'O';
        break;
      }
    }

    if (xwon(rows[0][0], rows[1][1], rows[2][2], rows[3][3])) {
      whoWon = 'X';
    }
    if (owon(rows[0][0], rows[1][1], rows[2][2], rows[3][3])) {
      whoWon = 'O';
    }

    if (xwon(rows[0][3], rows[1][2], rows[2][1], rows[3][0])) {
      whoWon = 'X';
    }
    if (owon(rows[0][3], rows[1][2], rows[2][1], rows[3][0])) {
      whoWon = 'O';
    }

    if (whoWon == 'd' && contains(rows,'.'))
      whoWon = '.';

    switch (whoWon) {
      case '.' : { cout << "Case #" << t << ": Game has not completed" << endl; break;}
      case 'd' : { cout << "Case #" << t << ": Draw" << endl; break;}
      default  : { cout << "Case #" << t << ": " << whoWon << " won" << endl; break;}
    }

  }
  return 0;
}
