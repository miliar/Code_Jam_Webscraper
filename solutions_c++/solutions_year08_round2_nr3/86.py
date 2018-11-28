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
#define maxn 1000010
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin

#define lowbit(x) ((x)&((x)^((x)-1)))
struct sum{
  int a[maxn],c[maxn],ret;
  int n;
  void init(int i){memset(a,0,sizeof(a));memset(c,0,sizeof(c));n=i;}
  void update(int i,int v){for (v-=a[i],a[i++]+=v;i<=n;c[i-1]+=v,i+=lowbit(i));}
  int query(int i){for (ret=0;i;ret+=c[i-1],i^=lowbit(i));return ret;}
};

int K;
int S[maxn];
sum s;

int find(int x) {
  // find largest index i such that query(i)=x
  int left=0, right=s.n;
  while(left<right-1) {
    int m = (left+right)/2;
    if(s.query(m)>x) right=m;
    else left=m;
  }
  return left;
}

void doit() {
  s.init(K);
  REP(i,K) s.update(i,1);
  int tot=K,prev=0;
  for(int cur=1; cur<=K; cur++) {
    int ptot = s.query(prev);
    int ct = (ptot+cur+tot-1)%tot;
    int t = find(ct);
    s.update(t,0);
    S[t]=cur;
    prev=t;
    tot--;
  }
}

int main(){
  int T;
  cin>>T;
  for(int C=1; C<=T; C++) {
    cin>>K;
    doit();
    cout << "Case #"<<C<<":";
    int n;
    cin>>n;
    REP(i,n) {
      int x;
      cin>>x;
      cout << ' '<<S[x-1];
    }
    cout << endl;
  }
}
