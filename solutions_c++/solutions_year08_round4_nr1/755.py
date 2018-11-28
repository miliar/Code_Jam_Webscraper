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
#define maxn 11000
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin

#define lc(x) (2*(x)+1)
#define rc(x) (2*(x)+2)
int n,m,V,gate[maxn],can[maxn],val[maxn];
int F[maxn][2];

int f(int i,int v) {
  int& ret = F[i][v];
  if(ret==-1) {
    ret = inf;
    if(i<m) {
      int l = lc(i), r = rc(i);
      int g[2], change[2]={};
      g[0]=g[1]=gate[i];
      if(can[i]) g[1]=!gate[i], change[1]=1;
      REP(j,2) {
	REP(ii,2) REP(jj,2) {
	  if(g[j]==0 && (ii|jj)==v) {
	    ret <?= f(l,ii)+f(r,jj)+change[j];
	  }
	  else if(g[j]==1 && (ii&jj)==v) {
	    ret <?= f(l,ii)+f(r,jj)+change[j];
	  }
	}
      }
    }
    else {
      if(val[i]==v) ret=0;
    }
  }
  return ret;
}

int doit() {
  int ret = inf;
  REP(mask,1<<m) {
    int num=0, valid=1;
    REP(i,m) {
      if(mask&1<<i) {
	num++;
	if(!can[i]) valid=0;
      }
    }
    if(!valid || num>=ret) continue;
    FORD(i,m-1,0) {
      int tmp = gate[i];
      if(mask&1<<i) tmp=!tmp;
      if(tmp) val[i]=val[lc(i)]&val[rc(i)];
      else val[i]=val[lc(i)]|val[rc(i)];
    }
    if(val[0]==V) ret=num;
  }
  return ret;
}

int main(){
  int T;
  cin>>T;
  for(int C=1; C<=T; C++) {
    cin>>n>>V;
    m=(n-1)/2;
    memset(F,-1,sizeof(F));
    REP(i,m) cin>>gate[i]>>can[i];
    FOR(i,m,n-1) cin>>val[i];
    cout << "Case #"<<C<<": ";
    //int sol1 = doit();
    int sol = f(0,V);
    //assert(sol1==sol);
    if(sol==inf) {
      cout << "IMPOSSIBLE"<<endl;
    }
    else {
      cout << sol<<endl;
    }
  }
}
