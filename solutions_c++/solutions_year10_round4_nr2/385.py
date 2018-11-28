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

int miss[1100];
int price[11][1100];
int cache[11][11][1100];

int cal(int m, int x, int y) {
  if (x == -1) return miss[y] >= m ? 0 : inf; 

  int & ret = cache[m][x][y]; 
  if (ret != -1) return ret;
  
  ret = inf;

  int tmp = cal(m+1, x-1, y*2) + cal(m+1, x-1, y*2+1); 
  ret = tmp < ret ? tmp : ret; 
  tmp = price[x][y] + cal(m, x-1, y*2) + cal(m, x-1, y*2+1);
  ret = tmp < ret ? tmp : ret; 
  return ret;
}

int main(){
  int C, n, x1, y1, x2, y2; cin >> C;
  
  for (int T = 1; T <= C; ++T) {
    cin >> n;
    
    REP(i, (1 << n)) {
      cin >> miss[i];
    }

    REP(i, n) {
      int k = n - i - 1;
      REP(j, (1 << k)) cin >> price[i][j];
    }

    CLEAR(cache, -1);
    cout << "Case #" << T << ": " << cal(0, n-1, 0) << endl;
  }
}
