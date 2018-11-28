#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
#include <ext/numeric>
using namespace std ;
using namespace __gnu_cxx ;
typedef long long LL ;
const int INF = 1000000000 ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
main()
{
	ios_base::sync_with_stdio(0) ;
	int C ;
	cin >> C ;
	for(int cc=1 ; cc<=C ; cc++) {
		cout << "Case #" << cc << ": " ;
		LL n, k ;
		cin >> n >> k ;
		if( k % power(2ll, n) == (power(2ll, n)-1) ) cout << "ON" << endl ;
		else cout << "OFF" << endl ;
	}
}

