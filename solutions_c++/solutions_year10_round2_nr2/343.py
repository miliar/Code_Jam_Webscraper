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
int X[100] ;
int V[100] ;
main()
{
	ios_base::sync_with_stdio(0) ;
	int C ;
	cin >> C ;
	for(LL cc=1 ; cc<=C ; cc++) {
		cout << "Case #" << cc << ": " ;
		int N, K, B, T, i ;
		cin >> N >> K >> B >> T ;
		REP(i,N) cin >> X[i] ;
		REP(i,N) cin >> V[i] ;
		int nieudacznicy = 0 ;
		int odp = 0 ;
		int dobiegnie = 0 ;
		for(i=N-1 ; i>=0 ; i--) {
			if(dobiegnie >= K) break ;
			if(B-X[i] <= T*V[i]) {
				dobiegnie ++ ;
				odp += nieudacznicy ;
			}
			else nieudacznicy ++ ;
		}
		if(dobiegnie >= K) cout << odp << endl ;
		else cout << "IMPOSSIBLE" << endl ;
	}
}

