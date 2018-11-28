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
string dp[1001][5];
void precompute(){
  REP(i,1001){
    int i1=0;
    stringstream s;
    s<<i;
    string a=s.str();
    // dp[i][i1++]=a;
    if(a.size()==1)
      continue;
    else{
      FOR(j,1,a.size()){
	string b=a.substr(j,a.size())+a.substr(0,j);
	if(b!=a){
	  dp[i][i1++]=b;
	}
	//	cout<<b<<endl;
      }
    }
  }
}

int main(){
  int t;
  precompute();
  cin>>t;
  REP(i1,t){
    int a,b;
    cin>>a>>b;
    int c=0;
    FOR(i,a,b+1){
      vector <int> d(1001);
      REP(j,5){
	string d1=dp[i][j];
	if(d1=="")
	  break;
	stringstream s;
	s<<d1;
	int d2;
	s>>d2;
	//	cout<<d2<<endl;
	if(d2<=b&&d[d2]==0&&d2>=a){
	  d[d2]=1;
	  c++;
	}
      }
    }
    cout<<"Case #"<<i1+1<<": "<<(int)c/2<<endl;
  }
}

