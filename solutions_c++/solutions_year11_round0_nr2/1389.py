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
#include <queue> 
#include <cfloat>
#include <vector> 
#include <string> 
#include <climits> 
#include <cstring> 
#include <cassert> 
#include <complex>

using namespace std;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3FFFFFFFFF

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define ALL(V) V.begin(), V.end()
#define S(V) (int)V.size()

#define pb push_back
#define mp make_pair

template<typename T> T inline SQR( const T &a ){ return a*a; }
template<typename T> T inline ABS( const T &a ){ return a < 0 ? -a : a; }
template<typename T> T inline MIN( const T& a, const T& b){ if( a < b ) return a; return b; }
template<typename T> T inline MAX( const T& a, const T& b){ if( a > b ) return a; return b; }

typedef long long int64;
typedef unsigned long long uint64;

int64 MOD = 1000000007LL;

int64 mypow( int64 a, int64 p ){
	if( p ) return 1LL;
	int64 ans = mypow( a, p/2 );
	ans *= ans;
	ans %= MOD;
	if( p&1 ) return ( a * ans ) % MOD;
	return ans;
}

int main(){
	ios::sync_with_stdio( false );
	int t;
	cin>>t;
	REP(k, t){
	    int c, d, n;
	    cin>>c;
	    vector<string> comb(c);
	    REP(i, c) cin>>comb[i];
	    cin>>d;
	    vector<string> opp(d);
	    REP(i, d) cin>>opp[i];
	    vector<char> res;
	    cin>>n;
	    vector<char> serie(n);
	    REP(i, n){
	      cin>>serie[i];
	      res.pb(serie[i]);
	      if(S(res)>=2){
		  REP(j, c){
		      if(S(res)<2) break;
		      if((res[S(res)-1]==comb[j][0] && res[S(res)-2]==comb[j][1]) || (res[S(res)-1]==comb[j][1] && res[S(res)-2]==comb[j][0])){
			  res.pop_back();
			  res.pop_back();
			  res.pb(comb[j][2]);
			  j=0;
		      }
		  }
		  bool leave;
		  if(S(res)>=2){
		    leave = false;
		    REP(j, d){
		      leave = false;
		      char count='w';
		      for(int l=S(res)-1; l>=0; l--){
			  if((res[l]==opp[j][0] || res[l]==opp[j][1]) && res[l]!=count){
			      if(count=='w'){
				  count = res[l];
			      }else{
				  leave = true;
				  break;
			      }
			  }
		      }
		      if(leave) break;
		    }
		    if(leave) res.clear();
		  }
	      }
	    }
	    cout<<"Case #"<<(k+1)<<": [";
	    if(!res.empty()){
		cout<<res[0];
		FOR(i, 1, S(res)){
		    cout<<", "<<res[i];
		}
	    }
	    cout<<"]"<<endl;
	}
	return 0;
}

