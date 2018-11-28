#include <cstdio>

int n;
int a[1 << 10];

void read() {
	int i;
	
	scanf ( "%d" , &n );
	for (i = 1; i <= n; i++)
		scanf ( "%d" , &a[i] );
}

void solve() {
	int i;
	int ans = 0;
	
	for (i = 1; i <= n; i++)
		if ( i != a[i] ) 
			++ ans;
		
	printf ( "%d.000000\n" , ans );
}

int main() {
	int cases , i;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d: " , i );
		solve();
	}
	
	return 0;
}
