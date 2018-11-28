#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstring>
#include <hash_map>
#include <hash_set>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define REP(i,n) FOR(i,0,(n))
#define FORD(i,a,b) for(int i=(a),_b=(b);i>_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000
#define maxn 1100
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin
int board[300][300];

set<pair<int, int> > next(set<pair<int, int> > has) {
  set<pair<int, int> > ret;
  CLEAR(board, 0);
  
  FORE(e, has) {
    int x = e->first;
    int y = e->second;
    board[x][y] = 1;
  }

  FORE(e, has) {
    int x = e->first;
    int y = e->second;
 
    if (board[x-1][y] || board[x][y-1]) {
      ret.insert(make_pair(x, y));
    }

    if (board[x+1][y]) {
      ret.insert(make_pair(x+1, y));
    }

    if (board[x-1][y+1]) {
      ret.insert(make_pair(x, y+1));
    }
  }

  return ret;
}

int main(){
  int C, n, x1, y1, x2, y2; cin >> C;
  
  for (int T = 1; T <= C; ++T) {
    cin >> n;
    set<pair<int, int> > has;
    REP(i, n) {
      cin >> x1 >> y1 >> x2 >> y2;
      
      FOR(x, x1, x2+1) FOR(y, y1, y2+1) has.insert(make_pair(x, y));
    }
    int ans = 0;
    while (has.size()) {
      ans++;
      has = next(has);
      // cout << has.size() << endl;
    }
    cout << "Case #" << T << ": " << ans << endl;
  }
}
