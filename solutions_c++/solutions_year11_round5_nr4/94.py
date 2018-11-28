/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
/* IOstream Libs */
#include <iostream>
#include <fstream>
#include <sstream>
/* String Libs */
#include <string>
/* STL Containers */
#include <bitset>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
/* STL Algorithm */
#include <algorithm>
/* Miscellaneous */
#include <complex>
#include <functional>
#include <iterator>
//#include <limits>
#include <numeric>
#include <typeinfo>
#include <utility>
#include <valarray>

using namespace std;

#define REP(i,s,t) for(int _t=t,i=s;i<_t;i++ )
#define REPP(i,s,t) for(int _t=t,i=s;i<=_t;i++)

#define LET(x,a) __typeof(a) x (a)
#define ITER(i,a,b) for(LET(i,a);i!=(b);++i)
#define FOREACH(it,v) ITER(it,v.begin(),v.end())

#define FILLA(a,x) memset(&a,x,sizeof(a))
#define FILL(a,x) memset(a,x,sizeof(a))
#define CLEARA(a,x) FILLA(a,0)
#define CLEAR(a) FILL(a,0)

#define m_p make_pair
#define fst first
#define snd second
typedef pair<int,int> PII;
typedef long long ll;
template<class T> void check_max( T&a, T b ){ if ( a < b ) a = b; }
template<class T> void check_min( T&a, T b ){ if ( a > b ) a = b; }

//#define debug

string i22 ( ll n ){
	if ( n == 0 ) return "";
	return i22(n/2) + char( n%2 + '0' );
}
bool ok( ll v ){
	double dv = v;
	double sq = sqrt(dv);
	ll sqi = ll(sq);
	REP(d,-2,3){
		ll x = sqi + d;
		if ( x >= 0 && x*x == v )
			return true;
	}
	return false;
}
int main(){
	int T; cin >> T;
	REP(Case,1,T+1){
		string s;
		cin >> s;
		int l = s.length();
		ll known = 0;
		vector<int> ps;
		for( int i = 0; i < l; i++ ){
			char ch = s[l-1-i];
			if ( ch == '?' )
				ps.push_back( i );
			else{
				ll x = ch - '0';
				known += x << i;
			}
		}
		int maxs = 1 << int(ps.size());
		REP(s,0,maxs){
			ll more = 0;
			REP(i,0,ps.size()) if ( s&(1<<i) )
				more |= 1LL << ps[i];
			ll n = known + more;
			if ( ok (n ) ){
				printf("Case #%d: ",Case);
				cout << i22( n ) << endl;
				break;
			}
		}
	}
	return 0;
}
