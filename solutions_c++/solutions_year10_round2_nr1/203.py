#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <set>
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

main()
{
	int test ;
	cin >> test ;
	FOR(Case,1,test) {
		int N, M ;
		cin >> N >> M ;
		
		set<string> folders ;
		REP(i,N) {
			string thu_muc ;
			cin >> thu_muc ;
			
			REP(j,size(thu_muc)) 
				if ( thu_muc[j] == '/' ) thu_muc[j] = ' ' ;
			
			istringstream sin( thu_muc ) ;
			string path = "/" ;
			string ss ;
			while ( sin >> ss ) {
				path += ss ;
				if ( folders.find(path) == folders.end() ) {
					folders.insert( path ) ;					
				}
				path += '/' ;
			}
		}
		
		int res = 0 ;
		REP(i,M) {
			string thu_muc ;
			cin >> thu_muc ;
			
			REP(j,size(thu_muc)) 
				if ( thu_muc[j] == '/' ) thu_muc[j] = ' ' ;
			//cout << thu_muc << endl ;
			istringstream sin( thu_muc ) ;
			string path = "/" ;
			string ss ;
			while ( sin >> ss ) {
				path += ss ;
				if ( folders.find(path) == folders.end() ) {
					res++ ;
					folders.insert( path ) ;					
				}
				path += '/' ;
			}
		}
		
		cout << "Case #" << Case  << ": " << res << endl ;
	}
}