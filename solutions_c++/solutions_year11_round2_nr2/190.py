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
const LL INF = 1000ll*1000ll*1000ll*1000ll ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
vector<int> t ;
int D ;
bool ok(long double czas) {
	long double last = -2*INF ;
	int i ;
	FOREACH(q,t) {
		int nast = *q ;
		if(last + D <= nast) last = max(last + D, nast-czas) ;
		else if(nast + czas <= last + D)  return false ;
		else last = last+D ;
	}
	return true ;
}
main()
{
	ios_base::sync_with_stdio(0) ;
	int tests ;
	cin >> tests ;
	for(int test=1 ; test<=tests ; test++) {
		cerr << "Case #" << test << endl ;
		cout << "Case #" << test << ": " ;
		t.clear() ;
		int C, i, j, P, V ;
		cin >> C >> D ;
		while(C--) {
			cin >> P >> V ;
			while(V--) t.PB(P) ;
		}
		sort(ALL(t)) ;

		long double l = 0, p = INF ;
		while(p-l > 1e-6) {
			long double s = (l+p)/2 ;
			//			cerr << s << endl ;
			if(ok(s)) p = s ;
			else l = s ;
		}
		cout.setf(ios::fixed) ;
		cout.precision(8) ;
		cout << l << endl ;
	}
}

