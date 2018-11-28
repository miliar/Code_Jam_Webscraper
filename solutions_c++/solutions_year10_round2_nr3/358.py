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

const int MOD = 100003 ;
LL C[120][120] ;

LL komb(int a, int b) {
	if(a < b) return 0 ;
	else return C[a][b] ;
}

struct trojka {
	int p, k ;
	LL ile ;
	trojka(int pp=0, int kk=0, LL iile=0) {
		p = pp ;
		k = kk ;
		ile = iile % MOD ;
	}
} ;

main()
{
	ios_base::sync_with_stdio(0) ;
	int tests, i, j ;
	for(i=0 ; i<=100 ; i++) C[i][0] = 1 ;
	for(i=1 ; i<=100 ; i++)
		for(j=1 ; j<=i ; j++) {
			C[i][j] = C[i-1][j] + C[i-1][j-1] ;
			C[i][j] %= MOD ;
		}
	cin >> tests ;
	for(LL cc=1 ; cc<=tests ; cc++) {
		cout << "Case #" << cc << ": " ;
		int n ;
		cin >> n ;
		LL odp = 0 ;
		queue<trojka> kolejka ;
		kolejka.push(trojka(0,1,1)) ;
		while(!kolejka.empty()) {
			trojka a = kolejka.front() ; kolejka.pop() ;
		//	cout << "sciaglem " << a.p << " " << a.k << " " << a.ile << endl ;
			for(i=a.k+1 ; i<=n ; i++) {
				trojka b(a.k, i, a.ile * komb(i-a.k-1, a.k-a.p-1)) ;
				if(b.ile == 0) continue ;
			//	cout << b.p << " " << b.k << " " << b.ile << endl ;
				if(b.k == n) {
					odp += b.ile ;
					odp %= MOD ;
				}
				else kolejka.push(b) ;
			}
		}
		cout << odp % MOD << endl ;
	}
}

