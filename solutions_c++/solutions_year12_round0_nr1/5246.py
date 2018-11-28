/*
	with the help of god
*/
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <stack>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define GL ({ll t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i < _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);
#define VAR(a,b) __typeof(b) a=(b)
#define FORSTL(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REV(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
#define pi 3.1415926535897932384626433832795028841971
typedef pair<int,int> PII;
typedef pair<string,string> PSS;
typedef long long int ll;
typedef vector <int> VI;
typedef vector <string> VS;
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class T> T sqr (T x) {return x * x;}
int main(){
  int t;
  cin>>t;
  scanf("\n");
  string a="yhesocvxduiglbkrztnwjpfmaq";
  REP(j,t){
    string b;
    getline(cin,b);
    string c="";
    REP(i,b.size()){
      if(b[i]!=' '){
      c+=a[b[i]-'a'];
      }
      else
	c+=b[i];
    }
    cout<<"Case #"<<j+1<<": "<<c<<endl;
  }  
  
}

