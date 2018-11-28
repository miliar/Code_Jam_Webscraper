#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
using namespace std ;

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()

typedef vector<int> VI ;
typedef vector<string> VS ;
template<class T> inline int size(const T&c) { return c.size(); }  

double eps = 1e-7 ;
int D, C ;
int P[207], No[207] ;

int ok( double Distance ) 
{
	double last = -(10e+10) ;
	REP(i,C) {
		double maxi = P[i] + Distance ;
		REP(j,No[i]) {
			double pos = max( last + D, P[i] - Distance ) ;
			if ( pos - maxi > eps )
				return 0 ;
			last = pos ;
		}
	}
	return 1 ;
}

void process()
{
	cin >> C >> D ;
	REP(i,C) cin >> P[i] >> No[i] ;
	
	double l = 0.0, r = 1e+13 ;
	while ( r-l > eps ) {
		double mid = (l+r) / 2 ;
		if ( ok(mid) ) r = mid ;
		else l = mid ;
	}
	printf("%.6lf\n",r) ;
}

main()
{
	int nTest ;
	cin >> nTest ;
	FOR(Case,1,nTest) {
		cout << "Case #" << Case << ": " ;
		process() ;
	}
}