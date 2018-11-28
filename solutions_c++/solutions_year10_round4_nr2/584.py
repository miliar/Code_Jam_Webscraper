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

map<int, int> D[2000], F[2000] ;

main()
{
	int test ;
	cin >> test ;
	FOR(Case,1,test) {
		int P, M[2000] ;
		cin >> P ;
		REP(i,(1<<P)) cin >> M[i] ;
		
		REP(i,(1<<P)) {
			D[i].clear() ;
			D[i][M[i]] = 0 ;
		}
		
		DOW(i,P-1,0) {
			REP(j,(1<<i)) {
				int cost ;
				cin >> cost ;
				F[j].clear() ;				
				int left  = j * 2 ;
				int right = j * 2 + 1 ;
				FOREACH(it1,D[left])
					FOREACH(it2,D[right]) {
						int x = it1->first ;
						int y = it2->first ;
						int val = min( x, y ) ;
						if ( val == 0 ) {
							if ( F[j].find( val ) != F[j].end() ) F[j][val] = min( F[j][val], it1->second + it2->second + cost ) ;
							else F[j][val] = it1->second + it2->second + cost ;
						}
						else {
							if ( F[j].find( val ) != F[j].end() ) F[j][val] = min( F[j][val], it1->second + it2->second + cost ) ;
							else F[j][val] = it1->second + it2->second + cost ;
							
							if ( F[j].find( val-1 ) != F[j].end() ) F[j][val-1] = min( F[j][val-1], it1->second + it2->second  ) ;
							else F[j][val-1] = it1->second + it2->second ;
						}
					}
			}
			REP(j,1<<i) D[j] = F[j] ;			
		}
		
		int res = 2000000000 ;
		FOREACH(it,F[0]) res = min( res, it->second ) ;
		cout << "Case #" << Case << ": "<< res << endl ;
	}
}