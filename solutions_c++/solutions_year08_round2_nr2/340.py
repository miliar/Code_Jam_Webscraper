#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cassert>
#include <cmath>
using namespace std;
#define SZ(A) ((int)A.size())
typedef long long LL;
const int mn = 1111;
int color[mn], P ;
int getcolor ( int u ) {
	return color[u] = ( color[u] == u ? u : getcolor ( color[u] ) );
}
int check ( int a , int b ) {
	int g = __gcd ( a , b );
	for ( int i=2;i*i<=g;i++ ) if ( g % i == 0 ) {
		if ( i >= P ) return 1;
		while ( g % i == 0 ) g/= i;
	}
	return g>= P;
}
int main () {
	int t;
	cin >> t;
	for ( int kase = 1 ; kase <= t ; kase ++ ) {
		cout <<"Case #" << kase << ": " ;
		int lo , hi;
		cin >> lo >> hi >> P;
		int cnt = hi - lo + 1;
		for ( int i=lo;i<=hi;i++ ) color[i] = i;
		for ( int i=lo;i<=hi;i++ )
			for ( int j=i+1;j<= hi ; j++ ) {
				int ca = getcolor(i) , cb = getcolor(j);
				if ( ca == cb ) continue;
				if ( check ( i , j ) ) cnt -- , color[ca] = cb;
			}
		cout << cnt << endl;
	}
	return 0;
}

