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

int join[300][300];

int main() {

  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    cout << "Case #" << itc+1 << ": ";
    FORN(i, 300) FORN(j, 300) join[i][j] = -1;
    int njoin;
    cin >> njoin;
    FORN(i, njoin) {
      string buf;
      cin >> buf;
      join[(int)buf[0]][(int)buf[1]] = join[(int)buf[1]][(int)buf[0]] = buf[2];
    }
    vector<char> opposed[300];
    int nopposed;
    cin >> nopposed;
    FORN(i, nopposed) {
      string buf;
      cin >> buf;
      opposed[(int)buf[0]].PB(buf[1]);
      opposed[(int)buf[1]].PB(buf[0]);
    }

    int n;
    cin >> n;
    string seq;
    cin >> seq;

    deque<char> elements;
    map<char, int> count;

    FORN(i, SZ(seq)) {
      char ch = seq[i];
      if (!elements.empty() && join[(int)elements.back()][(int)ch] != -1) {
        count[(int)elements.back()]--;
        ch = join[(int)elements.back()][(int)ch];
        count[ch]++;
        elements.pop_back();
        elements.PB(ch);
        continue;
      }
      elements.PB(ch);
      count[ch]++;
      FORIT(it, opposed[(int)ch]) {
        if (count[*it]) {
          elements.clear();
          count.clear();
          break;
        }
      }
    }

    cout << "[";
    FORN(i, SZ(elements)) {
      if (i) cout << ", ";
      cout << elements[i];
    }
    cout << "]\n";

  }


  return 0;
}

