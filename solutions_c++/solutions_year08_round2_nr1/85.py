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
#define maxn 100010
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin

typedef complex<double> point;
#define x real()
#define y imag()

bool valid(double r) {
  int s = r+0.5;
  return fabs(r-s)<eps;
}

int n;
point P[maxn];

LL doit() {
  LL ret = 0;
  REP(i,n) FOR(j,i+1,n-1) FOR(k,j+1,n-1) {
    point Q = (P[i]+P[j]+P[k])/3.;
    if(valid(Q.x)&&valid(Q.y)) ret++;
  }
  return ret;
}

int main(){
  int T;
  cin>>T;
  for(int ca=1; ca<=T; ca++) {
    LL A,B,C,D,x0,y0,M;
    cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
    int cx=x0, cy=y0;
    P[0]=point(cx,cy);
    FOR(i,1,n-1) {
      cx = (A*cx+B)%M;
      cy = (C*cy+D)%M;
      P[i]=point(cx,cy);
    }

    LL sol = doit();
    cout << "Case #"<<ca<<": "<<sol<<endl;
  }
}
