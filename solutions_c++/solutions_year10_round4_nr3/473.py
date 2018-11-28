#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
#include <sstream>
#include <ext/numeric>
using namespace std ;
using namespace __gnu_cxx ;

#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL ;
const int INF = 1000000000 ;
bool t[300][300] ;

main()
{
	ios_base::sync_with_stdio(0) ;
	int tests ;
	cin >> tests ;
	for(int test=1 ; test<=tests ; test++) {
		cout << "Case #" << test << ": " ;
		int R, x1, y1, x2, y2, i, j ;
		memset(t, 0, sizeof(t)) ;
		cin >> R ;
		while(R--) {
			cin >> x1 >> y1 >> x2 >> y2 ;
			for(i=x1 ; i<=x2 ; i++)
				for(j=y1 ; j<=y2 ; j++) t[i][j] = true ;
		}
			int odp = 0 ;
			while(true) {
				odp ++ ;
				bool dodalem = false ;
				for(i=210 ; i>=1 ; i--) {
					for(j=210 ; j>=1 ; j--) {
						if(t[i][j] == 0) {
							if(t[i-1][j] && t[i][j-1]) {
								dodalem = true ;
								t[i][j] = true ;
							}
						}
						else {
							if(!t[i-1][j] && !t[i][j-1]) t[i][j] = false ;
							else dodalem = true ;
						}
					}
				}
				if(!dodalem) break ;
			}
			cout << odp << endl ;
	}
}

