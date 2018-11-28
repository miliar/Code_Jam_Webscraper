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
LL gcd(LL a, LL b){ return b?gcd(b, a % b):a; }


#define _ufind_run(x) for(;p[t=x];x=p[x],p[t]=(p[x]?p[x]:x))
#define _run_both _ufind_run(i);_ufind_run(j)
struct ufind{
  int p[maxn],t;
  void init(){memset(p,0,sizeof(p));}
  void set_friend(int i,int j){_run_both;p[i]=(i==j?0:j);}
  int is_friend(int i,int j){_run_both;return i==j&&i;}
};

int p[maxp],q[maxp],e[maxp];
void sieve() {
  p[1]=q[1]=e[1]=1;
  for(int i=2; i*i<maxp; i++)
    if(!p[i])
      for(int j=i*i; j<maxp; j+=i) if(!p[j]) p[j]=i;
  for(int i=2; i<maxp; i++) {
    if(!p[i]) p[i]=i;
    int prev = i/p[i];
    if(p[prev]==p[i]) q[i]=q[prev], e[i]=e[prev]+1;
    else q[i]=prev, e[i]=1;
  }
}

LL A,B,P;

LL doit() {
  LL ret = B-A+1;
  ufind uf;
  uf.init();
  FOR(i,A,B) FOR(j,i+1,B) {
    LL g = gcd(i,j);
    while(q[g]!=1) g=q[g];
    if(p[g]>=P && !uf.is_friend(i,j)) ret--,uf.set_friend(i,j);  
  }
  return ret;
}

int main(){
  sieve();
  int T;
  cin>>T;
  for(int C=1; C<=T; C++) {
    cin>>A>>B>>P;
    LL sol = doit();
    cout << "Case #"<<C<<": "<<sol<<endl;
  }
}
