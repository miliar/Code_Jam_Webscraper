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
const LL INF = 1000000000000000000ll ;
vector<map<int, LL> > t[20] ;

main()
{
	ios_base::sync_with_stdio(0) ;
	int tests, P, i, k ;
	LL a ;
	cin >> tests ;
	for(int test=1 ; test<=tests ; test++) {
		cout << "Case #" << test << ": " ;
		cin >> P ;
		for(i=0 ; i<=15; i++) t[i].clear() ;
		int n = power(2, P) ;
		for(i=0 ; i<n ; i++) {
			cin >> a ;
			t[0].PB(map<int,LL>()) ;
			t[0][i][a] = 0 ;
		}
		for(k=1 ; k<=P ; k++) {
			n = power(2, P-k) ;
			for(i=0 ; i<n ; i++) {
				cin >> a ;
				t[k].PB(map<int,LL>()) ;
				FOREACH(q, t[k-1][i*2])
					FOREACH(q2, t[k-1][i*2+1]) {
						int ile = min(q->first, q2->first) ;
						if(t[k][i].find(ile) == t[k][i].end()) t[k][i][ile] = INF ;
						t[k][i][ile] = min(t[k][i][ile], q->second + q2->second + a) ;
						if(ile != 0) {
							ile -- ;
							if(t[k][i].find(ile) == t[k][i].end()) t[k][i][ile] = INF ;
							t[k][i][ile] = min(t[k][i][ile], q->second + q2->second) ;
						}
					}
			}
		}
		LL odp = INF ;
		FOREACH(q, t[P][0]) odp = min(odp, q->second) ;
		cout << odp << endl ;
	}
}

