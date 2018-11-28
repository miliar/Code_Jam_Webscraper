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
#define maxn 1024
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin

int n,m,F[maxn][maxn];
string name[maxn],query[maxn];

int f(int i,int t) {
  int& ret = F[i][t];
  if(ret==-1) {
    ret = inf;
    if(t==m) ret = 0;
    else if(name[i]!=query[t]) REP(j,n) ret<?=f(j,t+1)+(i!=j);
  }
  return ret;
}

int main(){
  int T;
  cin>>T;
  for(int C=1; C<=T; C++) {
    cin>>n;
    string s;
    getline(cin,s);
    REP(i,n) {
      getline(cin,s);
      name[i]=s;
    }
    cin>>m;
    getline(cin,s);
    REP(i,m) {
      getline(cin,s);
      query[i]=s;
    }
    memset(F,-1,sizeof(F));
    int sol = inf;
    REP(i,n) sol<?=f(i,0);
    cout << "Case #"<<C<<": "<<sol<<endl;
  }
}
