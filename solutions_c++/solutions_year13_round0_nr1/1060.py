#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define forab(i,a,b) for(int i = (a); i <= (int)(b); i++)
#define forn(i,n) for(int i = 0; i < (int)(n); i++)
// need declare it for vc, vc can not use <typeof> keyword
#define foreach(it,c) for(it = c.begin(); it != c.end(); ++it)

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define zero(a) memset(a, 0, sizeof(a))

#define pb push_back
#define mp make_pair

int t;
vector<string> m;

bool check(char c) {
  forn (i, 4) {
    int cnt = 0;
    forn (j, 4) {
      if (m[i][j] == c || m[i][j] == 'T')
        cnt++;
    }
    if (cnt == 4) {
      return true;
    }
    cnt = 0;
    forn (j, 4) {
      if (m[j][i] == c || m[j][i] == 'T')
        cnt++;
    }
    if (cnt == 4) {
      return true;
    }
  }
  int cnt = 0;
  forn(i, 4) {
    if (m[i][i] == c || m[i][i] == 'T')
      cnt++;
  }
  if (cnt == 4) {
    return true;
  }
  cnt = 0;
  forn(i, 4) {
    if (m[i][3-i] == c || m[i][3-i] == 'T')
      cnt++;
  }
  if (cnt == 4) {
    return true;
  }
  return false;
}

bool has_dot() {
  forn(i, 4) {
    forn (j, 4) {
      if (m[i][j] == '.')
        return true;
    }
  }
  return false;
}

int main() {
  //freopen("1.in", "r", stdin);
  //freopen("1.out", "w", stdout);

  //freopen("A-small-attempt0.in", "r", stdin);
  //freopen("A-small-attempt0.out", "w", stdout);

  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);

  cin >> t;
  for (int cc = 1; cc <= t; cc++) {
    string s;
    m.clear();
    forn(i, 4) {
      cin >> s;
      m.push_back(s);
    }
    cout << "Case #" << cc << ": ";
    if (check('X'))
      cout << "X won";
    else if (check('O'))
      cout << "O won";
    else if (has_dot())
      cout << "Game has not completed";
    else
      cout << "Draw";
    cout << endl;
  }
  return 0;
}
