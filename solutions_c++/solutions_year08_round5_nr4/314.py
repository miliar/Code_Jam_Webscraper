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
#define maxn 1100
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin

int m,n,R;
int M[maxn][maxn],F[maxn][maxn],P=10007;

int f(int i,int j) {
  int& ret = F[i][j];
  if(ret==-1) {
    ret = 0;
    if(i==0&&j==0) ret=1;
    else if(!M[i][j]) {
      int ii,jj;
      ii=i-2, jj=j-1;
      if(ii>=0&&jj>=0) ret+=f(ii,jj);
      ii=i-1, jj=j-2;
      if(ii>=0&&jj>=0) ret+=f(ii,jj);
      ret%=P;
    }
  }
  return ret;
}

int main(){
  int T;
  cin>>T;
  for(int C=1; C<=T; C++) {
    cin>>m>>n>>R;
    memset(M,0,sizeof(M));
    REP(i,R) {
      int u,v;
      cin>>u>>v;
      u--,v--;
      M[u][v]=1;
    }
    memset(F,-1,sizeof(F));
    int sol = f(m-1,n-1);
    cout << "Case #"<<C<<": "<<sol<<endl;
  }
}
