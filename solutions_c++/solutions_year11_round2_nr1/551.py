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

string A[107], B[107] ;
int n ;

vector<double> WP_List()
{
	vector<double> WP ;
	REP(i,n) {
		int win = 0 ;
		int lose = 0 ;
		REP(j,n)
			if ( A[i][j] == '1' ) win++;
			else if ( A[i][j] == '0' ) lose++ ;
			
		if ( win + lose == 0 ) {
			WP.push_back( 0.0 ) ;
			continue ;
		}
		WP.push_back( (double)win / ( win + lose ) ) ;
	}
	return WP ;
}

void process()
{
	cin >> n ;
	REP(i,n) cin >> A[i] ;
		
	vector<double> WP = WP_List() ;
	
	vector<double> OWP ;
	REP(i,n) OWP.push_back( 0.0 ) ;
	vector<double> OOWP ;
	REP(i,n) OOWP.push_back( 0.0 ) ;
	
	REP(i,n) {
		REP(j,n) B[j] = A[j] ;
		REP(j,n) A[j][i] = A[i][j] = '.' ;
		vector<double> WPP = WP_List() ;
		REP(j,n) A[j] = B[j] ;
		
		int total = 0 ;
		REP(j,n) 
			if ( A[j][i] != '.'  ) {
				OWP[i] += WPP[j] ;
				total++ ;
			}
			
		if ( !total ) 
			continue ;
		OWP[i] *= (double)1.0 / total ;
	}

	REP(i,n) {
		int total = 0 ;
		REP(j,n) {
			if ( A[j][i] != '.' ) {
				OOWP[i] += OWP[j] ;
				total++ ;
			}
		}
		if ( !total) 
			continue ;
		OOWP[i] *= (double)1.0 / total ;
	}
	
	REP(i,n) {
		double val = WP[i] * 0.25 + OWP[i] * 0.5 + OOWP[i] * 0.25 ;
		printf("%.6lf\n",val) ;
	}
}

main()
{
	int nTest ;
	cin >> nTest ;
	FOR(Case,1,nTest) {
		cout << "Case #" << Case << ":" << endl ;
		process() ;
	}
}