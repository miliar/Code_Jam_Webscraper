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

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
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
#define maxn 200
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin

int n,m,H[maxn][maxn],M[maxn][maxn],I,ix[maxn],xi[maxn];
int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};

bool inside(int i,int j) {
  if(i>=m || i<0 || j<0 || j>=n) return false;
  return true;
}

void dfs(int i,int j) {
  if(M[i][j]==-1) {
    int k = -1, cur = H[i][j];
    REP(d,4) {
      int ii = i+di[d], jj = j+dj[d];
      if(inside(ii,jj) && H[ii][jj]<cur) cur=H[ii][jj],k=d;
    }
    if(k==-1) M[i][j]=I++;
    else {
      int ii = i+di[k], jj = j+dj[k];
      dfs(ii,jj);
      M[i][j]=M[ii][jj];
    }
  }
}

int main() {
  int T;
  cin >> T;
  FOR(K,1,T) {
    cin>>m>>n;
    REP(i,m) REP(j,n) cin>>H[i][j];
    I = 0;
    memset(M,-1,sizeof(M));
    REP(i,m) REP(j,n) dfs(i,j);    
    cout << "Case #"<<K<<':'<<endl;
/*
REP(i,m) {
  REP(j,n) cout << M[i][j]<<' ';
  cout << endl;
}
*/
    memset(xi,-1,sizeof(xi));
    I = 0;
    REP(i,m) REP(j,n) {
       if(xi[M[i][j]]==-1) {
         xi[M[i][j]] = I;
         ix[I] = M[i][j];
         I++;
       }
    }
    REP(i,m) {
      REP(j,n) {
        if(j) cout <<' ';
        cout << char('a'+xi[M[i][j]]);
      }
      cout << endl;
    }
  }
}
