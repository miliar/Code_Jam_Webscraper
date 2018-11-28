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
const int INF = 1000*1000*1000 ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

LL d[10100], l[10100] ;
LL t[10100] ;

main()
{
	ios_base::sync_with_stdio(0) ;
	int tests ;
	cin >> tests ;
	for(int test=1 ; test<=tests ; test++) {
		cout << "Case #" << test << ": " ;
		int n, i, j ;
		cin >> n ;
		for(i=0 ; i<n ; i++) cin >> d[i] >> l[i] ;
		cin >> d[n] ;
		l[n] = 0 ;
		for(i=1 ; i<=n ; i++) t[i] = -1 ;
		t[0] = d[0] ;
		for(i=0 ; i<n ; i++) {
//			cout << i << " ) " << t[i] << endl ;
			int dl = t[i] ;
			for(j=i+1 ; j<=n && d[i]+dl >= d[j] ; j++) {
				//cout << i << " " << j << " " << d[i] << " " << dl << " " << d[j] << endl ;
				t[j] = max(t[j], min(l[j], d[j]-d[i])) ;
			}
		}
	//	cout << t[n] << endl ;
		if(t[n]==-1) cout << "NO" << endl ;
		else cout << "YES" << endl ;
	}
}

