#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>
#include <iomanip>

#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;
typedef long double ld;

int main() {
  int tc, cn = 0;
  cin >> tc;
  while (cn++ < tc) {
    int i, j, N = 4;
    vector<string> board;
    fr (i, N) {
      string s;
      cin >> s;
      board.pb(s);
    }

    bool xwin = false, owin = false, is_empty = false;
    fr (i, N) {
      bool empty = false;
      bool vrx = true, vcx = true;
      bool vro = true, vco = true;
      fr (j, N) {
        if (board[i][j] == '.') is_empty = true, vrx = vro = false;
        if (board[i][j] == 'X') vro = false;
        if (board[i][j] == 'O') vrx = false;

        if (board[j][i] == '.') is_empty = true, vcx = vco = false;
        if (board[j][i] == 'X') vco = false;
        if (board[j][i] == 'O') vcx = false;
      }
      xwin |= (vrx | vcx);
      owin |= (vro | vco);
    }

    bool vx1 = true, vx2 = true;
    bool vo1 = true, vo2 = true;
    fr (i, N) {
      if (board[i][i] == '.') vx1 = vo1 = false;
      if (board[i][i] == 'X') vo1 = false;
      if (board[i][i] == 'O') vx1 = false;
      
      if (board[i][N - i - 1] == '.') vx2 = vo2 = false;
      if (board[i][N - i - 1] == 'X') vo2 = false;
      if (board[i][N - i - 1] == 'O') vx2 = false;
    }
    xwin |= (vx1 | vx2);
    owin |= (vo1 | vo2);

    cout << "Case #" << cn << ": ";
    if (xwin) cout << "X won" << endl;
    else if (owin) cout << "O won" << endl;
    else if (is_empty) cout << "Game has not completed" << endl;
    else cout << "Draw" << endl;
  }
  return 0;
}
