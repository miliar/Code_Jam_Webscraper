#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <queue>
#include <cassert>
#include <bitset>
#include <climits>
#include <cfloat>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define FF first
#define SS second

#define FOR(v, s, e) for (int v = s; v < e; v++)
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define FI(c) for (ll i = 0; i < c; ++i)
#define FJ(s,c) for (ll j = s; j < c; ++j)
#define FK(s,c) for (ll k = s; k < c; ++k)
#define MP(X,Y) make_pair(X,Y)
// end boilerplate code...

void runcase() {
  char brd[4][4];
  int dotcnt = 0;
  bool xwins, owins;
  FI(4) {
    string s;
    cin >> s;
    FJ(0, 4) {
      brd[i][j] = s[j];
      if (s[j] == '.') dotcnt++;
    }
  }

  /* check horiz */
  FI(4) {
    xwins = true;
    owins = true;
    FJ(0, 4) {
      if (brd[i][j] != 'X' && brd[i][j] != 'T') xwins = false;
      if (brd[i][j] != 'O' && brd[i][j] != 'T') owins = false;
    }
    if (xwins) {
      cout << "X won";
      return;
    }
    if (owins) {
      cout << "O won";
      return;
    }
  }

  /* check vert */
  FI(4) {
    xwins = true;
    owins = true;
    FJ(0, 4) {
      if (brd[j][i] != 'X' && brd[j][i] != 'T') xwins = false;
      if (brd[j][i] != 'O' && brd[j][i] != 'T') owins = false;
    }
    if (xwins) {
      cout << "X won";
      return;
    }
    if (owins) {
      cout << "O won";
      return;
    }
  }
  /* check D1 */
  xwins = true;
  owins = true;
  FJ(0, 4) {
    if (brd[j][j] != 'X' && brd[j][j] != 'T') xwins = false;
    if (brd[j][j] != 'O' && brd[j][j] != 'T') owins = false;
  }
  if (xwins) {
    cout << "X won";
    return;
  }
  if (owins) {
    cout << "O won";
    return;
  }

  /* check D2 */
  xwins = true;
  owins = true;
  FJ(0, 4) {
    if (brd[3-j][j] != 'X' && brd[3-j][j] != 'T') xwins = false;
    if (brd[3-j][j] != 'O' && brd[3-j][j] != 'T') owins = false;
  }
  if (xwins) {
    cout << "X won";
    return;
  }
  if (owins) {
    cout << "O won";
    return;
  }

  if (dotcnt == 0) {
    cout << "Draw";
  } else {
    cout << "Game has not completed";
  }

}

int main() {
  cout << setprecision(9);
/* *** codejam style *** */
  int case_count;
  cin >> case_count;
  for (int i = 0; i < case_count; i++) {
    cout << "Case #" << (i+1) << ": ";
    runcase();
    cout << endl;
  }
/* *** because I'm awesome *** */
  return 0;
}

