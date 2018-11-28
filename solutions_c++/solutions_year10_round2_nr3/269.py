// {{{
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cfloat>
#include <queue>
#include <complex>
#include <cstring>
#include <climits>

using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define REPS(i,x) for(int i=0;i<(int)((x).size());++i)
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,a,b) for(int i=(int)(b);i>=(int)(a);--i)
#define FOREACH(it,x) for(typeof((x).begin()) it=(x).begin();it!=(x).end();++it)
#define SIZE(x) (int)(x).size()
#define ALL(x) x.begin(),x.end()
#define SORT(A) sort(A.begin(),A.end())
#define RSORT(A) sort(A.rbegin(),A.rend())
#define CLEAR(a) memset(a,0,sizeof a)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define PB push_back
#define MP make_pair
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FOREACH(it,x) cerr << *it << ","; cerr << "\n";
typedef vector<bool> VB;
typedef vector< vector<bool> > VVB;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long LL;
typedef vector<long long> VLL;
typedef vector< vector<long long> > VVLL;
typedef vector<double> VD;
typedef vector< vector<double> > VVD;
typedef pair<int,int> PII;
typedef pair<long long,long long> PLL;
typedef vector<string> VS;

vector<string> split(string s, string delimiter=" ") {
  vector<string> res;
  string word="";
  FOREACH(it,s) 
    if(find(ALL(delimiter),*it)==delimiter.end())
      word += *it;
    else {
      res.push_back(word);
      word="";
    }
  res.push_back(word);
  return res;
}

int string2int(string s) { istringstream i(s); int x; i>>x; return x; }
LL string2LL(string s) { istringstream i(s); LL x; i>>x; return x; }

string int2string(int n) { ostringstream o; o<<n; return o.str(); }

VI string2VI(string s, string delimiter=" ") {
  VS v = split(s,delimiter);
  VI res;
  FOREACH(it,v) res.push_back(string2int(*it));
  return res;
}

VI string2VLL(string s, string delimiter=" ") {
  VS v = split(s,delimiter);
  VI res;
  FOREACH(it,v) res.push_back(string2LL(*it));
  return res;
}

string mergeVS(VS v) {
  string s; FOREACH(it,v) s += *it; return s;
}

template<class T> inline T checkmin(T &a,T b){if(b<a) a=b; return a;}

template<class T> inline T checkmax(T &a,T b){if(b>a) a=b; return a;}

template<class T> T gcd(T a, T b){if(b==0) return a; else return gcd(b,a%b);}
template<class T> T gcdv(vector<T> v){
  if(v.size()==1) return v[0]; 
  else return gcd(v[0],gcdv(vector<T>(v.begin()+1,v.end())));
}

template<class T> T lcm(T a, T b){ return a/gcd(a,b)*b;}
template<class T> T lcmv(vector<T> v){
  if(v.size()==1) return v[0]; 
  else return lcm(v[0],lcmv(vector<T>(v.begin()+1,v.end())));
}
int LOWBIT(int n){ return (n^(n-1))&n;}
int COUNTBIT(int n){ return __builtin_popcount(n);}

long long CHOOSE(long long N, long long K){
  long long res=1;
  REP(i,K){
    res*=N-i;
    res/=i+1;
  }
  return res;
}

template<class T> T ceilfrac(T a, T b){if(a%b) return a/b+1; else return a/b;}
// }}}

const LL MOD=100003;
LL u[501][501];
LL bin[501][501];
LL f[501];


void run(int case_index) {
  int res=0;
  int n;
  cin >> n;
  res=f[n];
	printf("Case #%d: %d\n",case_index,res);
}


int main(int argc, char* argv[]) {

  CLEAR(bin);
  FOR(n,0,500){
    bin[n][0]=1;
    REP(k,n){
      bin[n][k+1] = bin[n-1][k]+bin[n-1][k+1];
      bin[n][k+1] %= MOD;
    }
  }
  
  CLEAR(u);
  u[2][1]=1;
  FOR(n,3,500){
    FOR(k,2,n-1){
      u[n][k]=0;
      FOR(i,1,k-1){
        u[n][k] += u[k][i]*bin[n-k-1][k-1-i];
        u[n][k] %=  MOD;
      }
    }
  }

  CLEAR(f);
  FOR(n,2,500){
    f[n]=0;
    FOR(k,1,n-1){
      f[n] += u[n][k];
      f[n] %= MOD;
    }
  }


	int n; 
  cin >> n;
	FOR(i,1,n){
    cerr << i << " ";
    run(i);
  }
  cerr << endl;
	return 0;
}
