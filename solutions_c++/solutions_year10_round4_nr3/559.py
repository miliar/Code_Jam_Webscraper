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

int A[300][300], B[300][300] ;

main()
{
	int test ;
	cin >> test ; 
	FOR(Case,1,test) {
		memset( A, 0, sizeof(A) ) ;
		int R ;
		cin >> R ;
		int ok = 0 ;
		REP(i,R) {
			int X1, Y1, X2, Y2 ;
			cin >> X1 >> Y1 >> X2 >> Y2 ;
			
			FOR(x,X1,X2)
				FOR(y,Y1,Y2) {
					A[x][y] = 1 ;
					ok = 1 ;
				}
		}
		
		if ( !ok ) {
			cout << "Case #" << Case << ": " << 0 << endl ;
			continue ;
		}
		
//		   1.  If a bacterium has no neighbor to its north and no neighbor to its west, then it will die.
   //      2. If a cell has no bacterium in it, but there are bacteria in the neighboring cells to the north and to the west, then a new bacterium will be born in that cell. 
   
   		int res = 0 ;
   		while (true) {
   			FOR(x,1,200)
   				FOR(y,1,200) {   					   					
   					if ( A[x][y] ) {
   						if ( !A[x-1][y] && !A[x][y-1] ) B[x][y] = 0 ;
   						else B[x][y] = 1 ;
   					}
   					else {
   						if ( A[x-1][y] && A[x][y-1] ) B[x][y] = 1 ;
   						else B[x][y] = 0 ;
   					}
   				}
   				
   			int conlai = 0 ;
   			FOR(x,1,200)
   				FOR(y,1,200) {
   					A[x][y] = B[x][y] ;
   					conlai += A[x][y] ;   					
   				}
   				
   			if ( !conlai ) break ;
   			else res++ ;
   		}
   		cout << "Case #" << Case << ": "<< res+1 << endl ;
	}
}