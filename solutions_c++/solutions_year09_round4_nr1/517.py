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
#define maxn 50
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin

int n,M[maxn][maxn],x[maxn],y[maxn];

#define _cp(a,b) ((a)<=(b))
int _tmp[maxn];
int inv(int n,int* a){
  int l=n>>1,r=n-l,i,j;
  int ret=(r>1?(inv(l,a)+inv(r,a+l)):0);
  for (i=j=0;i<=l;_tmp[i+j]=a[i],i++)
    for (ret+=j;j<r&&(i==l||!_cp(a[i],a[l+j]));_tmp[i+j]=a[l+j],j++);
  memcpy(a,_tmp,sizeof(int)*n);
  return ret;
}


int main(){
  int T;
  cin>>T;
  FOR(K,1,T) {
    cin>>n;
    string s;
    memset(y,0,sizeof(y));
    REP(i,n) {
      cin>>s;
      int m;
      for(m=n-1; m>=0; m--) if(s[m]=='1') break;
      if(m<0) m++;
      for(;y[m];m++);
      y[m]=1;
      x[i]=m;
    }
    //int sol = -hungary(n,n,M,x,y);
    //sol /= 2;
    int sol = inv(n,x);
    cout << "Case #"<<K<<": "<<sol<<endl;
  }
}
