/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <ctime>
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

template<class T>
void check_max( T&a, T b ){
	if ( a <  b ) a = b;
}
template<class T>
void check_min( T&a, T b ){
	if ( a > b ) a = b;
}

//#define debug
const int MAXN = 120;
const int MAXL = 10;
int rc[MAXN][MAXL], l[MAXN];
int ans;
int jz;
int frc[MAXN];
void dfs( int n, int last, int d ){
	if ( n == 0 ){
		ans++;
	//	cout << "found: ";
//		REP(i,0,d)cout <<" "<<frc[i];
//		cout << endl;
		return;
	}
	if ( n < last ) return;
	int ii;
	REP(i,last,n+1){
		l[d] = 0;
		ii = i;
		while ( ii ){
			rc[ d ][ l[d] ] = ii%jz;
			ii /= jz;
			l[d]++;
		}
		bool ok = true;
		REP(j,0,d){
			REP(ps,0,min(l[j],l[d]))
				if ( rc[j][ps] == rc[d][ps] ){
					ok = false; break;
				}
			if ( !ok ) break;
		}
		frc[d] = i;
		if ( ok ){
		//	cout << "d="<< d<< " i =  " << i << endl;;
			dfs(n-i,i,d+1);
		}
	}
}
int main(){
	int T;cin>>T;
	REP(Case,1,T+1){
		int n;
		cin >> n >> jz;
		ans = 0;
		dfs(n,1,0);
		cout << "Case #"<<Case<<": "<<ans<<endl;
	}
	return 0;
}
