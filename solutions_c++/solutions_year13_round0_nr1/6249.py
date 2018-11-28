/** 
 *
 * rais.fathin38
 */

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cctype>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <utility>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <bitset>

using namespace std;

#define REP(a, b) for(int a = 0; a < b; a++)
#define FOR(a, b, c) for(int a = b; a <= c; a++)
#define FOREACH(a, b) for(typeof(b.end()) a = b.begin(); a != b.end(); a++)
#define RESET(a, b) memset(a, b, sizeof a)
#define MAX(a, b) a = max(a, b)
#define MIN(a, b) a = min(a, b)

#ifdef F
#define OPEN freopen("tc", "r", stdin)
#define DEBUG(x) cout << #x << " : " << x << endl
#define TIME cout << fixed << setprecision(3) << clock() / (double)CLOCKS_PER_SEC << endl
#else
#define OPEN {}
#define DEBUG(x) {}
#define TIME {}
#endif

#define INF 0x7FFFFFFF
#define INFLL 0x7FFFFFFFFFFFFFFF

#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef long long int64;
typedef pair<int, int> pii;

template<class T> ostream& operator<<(ostream &S, const vector<T> &v) {S<<"(";REP(i,v.size()){if(i)S<<", ";S<<v[i];}S<<")";return S;}
template<class T1, class T2> ostream& operator<<(ostream &S, const pair<T1, T2> &p) {S<<"("<<p.fi<<", "<<p.se<<")";return S;}
template<class T> T abs(T num) { return num > 0 ? num : -num; }
template<class T> T sqr(T num) { return num*num; }

string board[4];
bool X, O;

void check(string line) {
  int t = 0, x = 0, o = 0;
  REP(i, 4) {
    if (line[i] == 'T') t++;
    else if (line[i] == 'O') o++;
    else if (line[i] == 'X') x++;
  }
  if (t == 1 && o == 3) O = true;
  else if (t == 1 && x == 3) X = true;
  else if (o == 4) O = true;
  else if (x == 4) X = true;
}

int main() {
  // freopen("tc", "r", stdin);
  // freopen("out", "w", stdout);
  int tc; cin >> tc;
  FOR(t, 1, tc) {
    X = O = false;
    REP(i, 4) cin >> board[i];
    REP(i, 4) check(board[i]);
    REP(i, 4) {
      string line = "";
      REP(j, 4) line += board[j][i];
      check(line);
    }
    {
      string line = "";
      REP(i, 4) line += board[i][i];
      check(line);
    }
    {
      string line = "";
      REP(i, 4) line += board[i][3-i];
      check(line);
    }
    if (X) printf("Case #%d: X won\n", t);
    else if (O) printf("Case #%d: O won\n", t);
    else {
      bool full = true;
      REP(i, 4) REP(j, 4) if (board[i][j] == '.') full = false;
      if (full) printf("Case #%d: Draw\n", t);
      else printf("Case #%d: Game has not completed\n", t);
    }
  }
  return 0;
}