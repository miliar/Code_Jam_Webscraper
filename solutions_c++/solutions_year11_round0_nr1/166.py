//Authored by dolphinigle
//Google Code Jam Prelim
//May 7 2011

#include <vector>
#include <list>
#include <map>
#include <set>

#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <assert.h>

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define DEBUG(x) cout << '>' << #x << ':' << x << '\n';

#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))
#define RESET(Z,Y) memset(Z,Y,sizeof(Z))

#define SZ(Z) ((int)Z.size())
#define ALL(W) W.begin(), W.end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define INF 1023123123
#define EPS 1e-8

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;
typedef vector<ll> vll;

int main() {

  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    cout << "Case #" << itc+1 << ": ";
    int n;
    cin >> n;

    queue<int> blue;
    queue<int> orange;
    queue<char> turn;
    int bp = 1;
    int op = 1;
    FORN(i, n) {
      char ch;
      cin >> ch;
      int pos;
      cin >> pos;
      turn.push(ch);
      switch (ch) {
        case 'O':
          orange.push(pos);
          break;
        case 'B':
          blue.push(pos);
          break;
      }
    }
    blue.push(1);
    orange.push(1);
    int ret = 0;
    while (!turn.empty()) {
      ++ret;
      int bm = 0;
      int om = 0;
      if (turn.front() == 'B') {
        if (blue.front() == bp) {
          blue.pop();
          turn.pop();
          bm = 1;
        }
      } else {
        if (orange.front() == op) {
          orange.pop();
          turn.pop();
          om = 1;
        }
      }
      if (!bm) {
        if (bp < blue.front()) ++bp;
        else if (bp > blue.front()) --bp;
      }
      if (!om) {
        if (op < orange.front()) ++op;
        else if (op > orange.front()) --op;
      }
    }
    cout << ret << endl;
  }


  return 0;
}

