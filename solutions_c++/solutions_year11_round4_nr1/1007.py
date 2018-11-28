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
bool po_predkosci(const pair<long double,long  double> &a, const pair<long double,long double> &b) {
	return a.SE < b.SE ;
}
main()
{
	ios_base::sync_with_stdio(0) ;
	int tests ;
	cin >> tests ;
	for(int test=1 ; test<=tests ; test++) {
		cout << "Case #" << test << ": " ;
		long double X, S, R, t, n ;
		cin >> X >> S >> R >> t >> n ;
		long double ost = 0 ;
		long double puste = 0 ;
		long double a, b, c ;
		vector<pair<long double,long  double> > pom ;
		int i ;
		for(i=0 ; i<n ; i++) {
			cin >> a >> b >> c ;
			puste += a-ost ;
			pom.PB(MP(b-a,c)) ;
			ost = b ;
		}
		puste += X-ost ;
		pom.PB(MP(puste,0)) ;
		sort(ALL(pom), po_predkosci) ;
	///FOREACH(q, pom) cout << "(" << q->FI << " " << q->SE << ") " ;
	//	cout << endl ;
		long double odp = 0 ;
		FOREACH(q, pom) {
			long double czas_biegniecia = min( t, q->FI/(q->SE+R)) ;
			odp += czas_biegniecia ;
			t  -= czas_biegniecia ;
			long double pozostaly_czas = (q->FI - czas_biegniecia*(q->SE+R))/(q->SE+S) ;
	//		cout << "pozostaly = " << pozostaly_czas << endl ;
			odp += pozostaly_czas ;
		}
		cout.setf(ios::fixed) ;
		cout.precision(8) ;
		cout << odp << endl ;
	}
}

