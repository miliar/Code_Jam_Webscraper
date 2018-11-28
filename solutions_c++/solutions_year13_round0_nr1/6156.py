#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    vector<string> board(4);
    for (int i = 0; i < 4; ++i) cin >> board[i];
    cout << "Case #" << cas << ": ";
    bool fi = false;
    bool dot = false;
    for (int i = 0; i < 4 and not fi; ++i) {
      bool subfi = fi;
      char p = board[i][0];
      if (p == '.') {
	subfi = true;
	dot = true;
      }
      for (int j = 1; j < 4 and not subfi; ++j) {
        char q = board[i][j];
        if (q == '.')  {
	  subfi = true;
	  dot = true;
        }
        else if (p == 'T') p = q;
        else if (q != 'T' and q != p) subfi = true;
      }
      if (not subfi) {
        cout << p << " won" << endl;
	fi = true;
      }
    }
    for (int i = 0; i < 4 and not fi; ++i) {
      bool subfi = fi;
      char p = board[0][i];
      if (p == '.') {
	subfi = true;
	dot = true;
      }
      for (int j = 1; j < 4 and not subfi; ++j) {
        char q = board[j][i];
        if (q == '.')  {
	  subfi = true;
	  dot = true;
        }
        else if (p == 'T') p = q;
        else if (q != 'T' and q != p) subfi = true;
      }
      if (not subfi) {
        cout << p << " won" << endl;
	fi = true;
      }
    }
    if (not fi) {
      bool subfi = fi;
      char p = board[0][0];
      if (p == '.') {
	subfi = true;
	dot = true;
      }
      for (int j = 1; j < 4 and not subfi; ++j) {
        char q = board[j][j];
        if (q == '.')  {
	  subfi = true;
	  dot = true;
        }
        else if (p == 'T') p = q;
        else if (q != 'T' and q != p) subfi = true;
      }
      if (not subfi) {
        cout << p << " won" << endl;
	fi = true;
      }
    }
    if (not fi) {
      bool subfi = fi;
      char p = board[0][3];
      if (p == '.') {
	subfi = true;
	dot = true;
      }
      for (int j = 1; j < 4 and not subfi; ++j) {
        char q = board[j][3-j];
        if (q == '.')  {
	  subfi = true;
	  dot = true;
        }
        else if (p == 'T') p = q;
        else if (q != 'T' and q != p) subfi = true;
      }
      if (not subfi) {
        cout << p << " won" << endl;
	fi = true;
      }
    }
    if (not fi) {
      if (not dot) cout << "Draw" << endl;
      else cout << "Game has not completed" << endl;
    }
  }
}
