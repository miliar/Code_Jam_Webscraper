#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int a[1001000];

main(){
	int T, tt = 0;
	int L, n, m, i;
	long long res, dis, t;
	
	freopen( "BL.in", "r", stdin );
	freopen( "BL.out", "w", stdout );
	
	scanf ( "%d", &T );
	while( T -- ){
		cin >> L >> t >> n >> m;
		for ( i = 0; i < m; i ++ )
			scanf ( "%d", a + i );
		for ( i = m; i < n; i ++ )
			a[i] = a[ i - m ];
		res = 0;
		dis = t / 2;
		for ( i = 0; i < n; i ++ )
			if ( dis > a[i] ){
				res += a[i] * 2;
				dis -= a[i];
			}
			else{
				res += dis * 2;
				a[i] -= dis;
				break;
			}
		sort ( a + i, a + n );
		for ( ; i < n; i ++ )
			if ( i >= n - L )
				res += a[i];
			else
				res += a[i] * 2;
		cout << "Case #" << ++ tt << ": " << res << endl;
	}
	
	return 0;
}
