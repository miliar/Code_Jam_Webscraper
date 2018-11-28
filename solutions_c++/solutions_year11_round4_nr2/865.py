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
const LL INF = 1000ll*1000ll*1000ll*1000ll ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
char t[510][510] ;
pair<int,int> do_dodania(int n_i, int n_j, int i, int j,  char x) {
	int co = x - '0' ;
	return MP(co*(n_i-i), co*(n_j-j)) ;
}
main()
{
	ios_base::sync_with_stdio(0) ;
	int tests ;
	cin >> tests ;
	for(int test=1 ; test<=tests ; test++) {
		cout << "Case #" << test << ": " ;
		int n, m, D ;
		cin >> n >> m >> D ;
		int i, j, k, p ;
		for(i=0 ; i<n ; i++) cin >> t[i] ;
		int odp = 0 ;
		for(i=0 ; i<n ; i++)
			for(j=0 ; j<m ; j++) { // wybieramy srodek				
				for(k=3 ; i+k-1<n && j+k-1 <m ; k++) {
					LL s1 =0, s2=0 ;
					for(int p=0 ; p<k ; p++) {
						for(int q=0 ; q<k ; q++) {
				//			cout << "dodaje " << i+p << " " << j+q << " " ;
							pair<int,int> pom = do_dodania(2*(i+p)+1,2*(j+q)+1, 2*i+k, 2*j+k, t[i+p][j+q]) ;
							s1 += pom.FI ;
							s2 += pom.SE ;
			//				cout << s1 << " " << s2 << endl ;
						}
					}
					pair<int, int> pom = do_dodania(2*(i)+1,2*(j)+1, 2*i+k, 2*j+k, t[i][j]) ;
					s1 -= pom.FI ;
					s2 -= pom.SE ;
					pom = do_dodania(2*(i)+1,2*(j+k-1)+1, 2*i+k, 2*j+k, t[i][j+k-1]) ;
					s1 -= pom.FI ;
					s2 -= pom.SE ;
					pom = do_dodania(2*(i+k-1)+1,2*(j)+1, 2*i+k, 2*j+k, t[i+k-1][j]) ;
					s1 -= pom.FI ;
					s2 -= pom.SE ;
					pom = do_dodania(2*(i+k-1)+1,2*(j+k-1)+1, 2*i+k, 2*j+k, t[i+k-1][j+k-1]) ;
					s1 -= pom.FI ;
					s2 -= pom.SE ;
				//	cout << i << " " << j << " " << j << " " << s1 << " " << s2 << endl ;
					if(s1==0 && s2==0) odp = max(odp, k) ;
				}
			}
		
		if(odp>=3)cout << odp << endl ;
		else cout << "IMPOSSIBLE" << endl ;
	}
}

