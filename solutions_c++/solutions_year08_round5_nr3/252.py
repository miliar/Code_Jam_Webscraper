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

int m,n,M[maxn][maxn],F[1<<10][maxn];

bool match(int m1,int m2) {
  REP(i,n) if(m2&1<<i) {
    int ii=i+1;
    if(ii<n) {
      if((m2&1<<ii)||(m1&1<<ii)) return false;
    }
    ii=i-1;
    if(i-1>=0) {
      if((m2&1<<ii)||(m1&1<<ii)) return false;
    }
  }
  return true;
}

int f(int mask,int i) {
  int& ret = F[mask][i];
  if(ret==-1) {
    ret = 0;
    int num = 0, valid = 1;
    REP(j,n) if(mask&1<<j) {
      num++;
      if(M[i][j]) valid=0;
    }
    if(valid) {
      if(i) {
	REP(tmp,1<<n) if(match(tmp,mask)) ret>?=f(tmp,i-1)+num;
      }
      else {
	if(match(0,mask)) ret=num;
      }
    }
  }
  return ret;
}

int main(){
  int T;
  cin>>T;
  for(int C=1; C<=T; C++) {
    cin>>m>>n;
    memset(M,0,sizeof(M));
    REP(i,m) REP(j,n) {
      char c;
      cin>>c;
      if(c=='x') M[i][j]=1;
    }
    int sol = 0;
    memset(F,-1,sizeof(F));
    REP(mask,1<<n) sol>?=f(mask,m-1);
    cout << "Case #"<<C<<": "<<sol<<endl;
  }
}
