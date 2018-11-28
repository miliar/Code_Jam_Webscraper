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

int sum(int a, int b){
    int out = 0;
    REP(j, 21){
	if(((a & (1<<j)) && (b & (1<<j))) || (!(a & (1<<j)) && !(b & (1<<j)))){
	   out &= ~(1<<j); 
	}else out |= (1<<j);
    }
    return out;
}

int main(){
	ios::sync_with_stdio( false );
	int t, n;
	cin>>t;
	REP(k, t){
	    cin>>n;
	    vector<int> vec(n);
	    REP(i, n){
		cin>>vec[i];
	    }
	    sort(vec.begin(), vec.end());
	    int res=0;
	    FOR(i, 1, n){
		res = sum(res, vec[i]);
	    }
	    cout<<"Case #"<<(k+1)<<": ";
	    if(res==vec[0]){
		int sum = 0;
		FOR(i, 1, n){
		    sum+=vec[i];
		}
		cout<<sum<<endl;
	    }else cout<<"NO"<<endl;
	}
	return 0;
}

