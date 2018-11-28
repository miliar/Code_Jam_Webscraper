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

const int maxn = 1007 ;

main()
{
	int test ;
	cin >> test ;
	FOR(Case,1,test) {
		
		int R, K, N ;
		cin >> R >> K >> N ;
		int Group[maxn] ;
		REP(i,N) cin >> Group[i] ;
			
		long long fuckingLoop[maxn] ;
		int numberOfRound[maxn] ;
		memset( fuckingLoop, -1, sizeof(fuckingLoop) ) ;
		memset( numberOfRound, 0, sizeof(numberOfRound) ) ;
		
		long long res = 0 ;
		int start = 0 ;
		int currentRound = 0 ;
		while ( R ) {
			
			if ( fuckingLoop[start] > -1 ) {				
				long long loop = res - fuckingLoop[start] ;
				int roundsInLoop = currentRound - numberOfRound[start] + 1 ;
				res += loop * ( R / roundsInLoop ) ;
				R %= roundsInLoop ;
				memset( fuckingLoop, -1, sizeof(fuckingLoop) ) ;
				memset( numberOfRound, 0, sizeof(numberOfRound) ) ;
				continue ;
			}
			
			numberOfRound[start] = ++currentRound ;
			fuckingLoop[start] = res ;	
			int seat = 0 ;
			REP(i,N) {
				if ( seat + Group[start] > K ) break ;
				seat += Group[start] ;
				start = ( start + 1 ) % N ;
			}			
			R-- ;
			res += seat ;
		}		
		cout << "Case #" << Case << ": " << res << endl ;
	}
}