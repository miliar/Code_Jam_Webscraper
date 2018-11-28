#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n;
int a[1 << 14];
vector < int > f[1 << 14];

void read() {
	int i , x;
	
	for (i = 0; i < (1 << 14); i++) a[i] = 0;
	
	scanf ( "%d" , &n );
	for (i = 1; i <= n; i++) {
		scanf ( "%d" , &x );
		a[x] ++;
	}
}

void solve() {
	int i , j;
	int ans = 1 << 30;
	
	for (i = 0; i < (1 << 14); i++) f[i].clear();

	for (i = 1; i < (1 << 14); i++) {
		for (j = 0; j < min ( (int)f[i - 1].size() , a[i] ); j++)
			f[i].push_back ( f[i - 1][j] + 1 );
		
		for (j = 0; j < a[i] - (int)f[i - 1].size(); j++)
			f[i].push_back ( 1 );
		
		if ( a[i] < (int)f[i - 1].size() )
			ans = min ( ans , f[i - 1][ a[i] ] );
		
		sort ( f[i].begin() , f[i].end() );
	}
	
	if ( !n ) ans = 0;
	
	printf ( "%d\n" , ans );
}

int main() {
	int i , cases;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d: " , i );
		solve();
	}
	
	return 0;
}
