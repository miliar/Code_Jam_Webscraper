#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <iomanip>
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

vector< pair< pair<int, int>, int > > A ;

void solve( int Case )
{
	int X, S, R, t, N ;
	cin >> X >> S >> R >> t >> N ;
	A.clear() ;
	REP(i, N) {
		int bi, ei, wi ;		
		cin >> bi >> ei >> wi ;
		A.push_back( make_pair( make_pair( bi, ei), wi ) ) ;
	}
	sort( all(A) ) ;
	
	vector< pair<int, int> > B ;
	int xp = 0 ;
	REP(i, N) {
		int bi = A[i].first.first ;
		int ei = A[i].first.second ;
		if ( xp < bi ) {
			B.push_back( make_pair( 0, bi - xp ) ) ;
		}
		B.push_back( make_pair( A[i].second, ei - bi ) ) ;
		xp = ei ;
	}
	if ( xp < X ) B.push_back( make_pair( 0, X - xp ) ) ;
	sort( all(B) ) ;
	
	REP(i,size(B) ) B[i] = make_pair( B[i].second, B[i].first ) ;
	double tang = t ;
	double res = 0  ;
	REP(i, size(B) ) {
		if ( tang > 0 ) {
			int vtm = R + B[i].second ;
			if ( vtm * tang >= B[i].first ) {
				tang -= B[i].first / (double)vtm ;
				res += B[i].first / (double)vtm ;
			}
			else {
				res += tang ;
				res += ( B[i].first - vtm * tang ) / (double)( S + B[i].second ) ;
				tang = 0 ;
			}
		}
		else {
			int vtm = S + B[i].second ;
			res += B[i].first / (double)vtm ;
		}
	}
	cout << fixed << setprecision(6) << "Case #" << Case << ": " << res << endl ;
}

main()
{
	int Test ;
	cin >> Test ;
	FOR(Case,1,Test) solve( Case ) ;
}