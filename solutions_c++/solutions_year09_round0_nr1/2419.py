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
#define maxn 5050
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin

int n,m,I;

string S[maxn];
int M[15][128];
string s;

void parse(int i) {
  if(s[I]=='(') {
    I++;
    while(s[I]!=')') M[i][s[I++]]=1;
    I++;
  }
  else {
    M[i][s[I++]] = 1;
  }
  if(i<n-1) parse(i+1);
}

int main() {
  int C;
  cin >> n >> m >> C;
  REP(i,m) {
    cin>>S[i];
  }
  FOR(K,1,C) {
    int sol = 0;
    memset(M,0,sizeof(M));
    cin >> s;
    I = 0;
    parse(0);
    REP(i,m) {
      int d = 1;
      REP(j,n) {
        if(!M[j][S[i][j]]) d=0;
      }
      sol += d;
    }
    cout << "Case #"<<K<<": "<<sol<<endl;
  }
}
