#include <cstdio>
#include <cstdio>

int n;
int a[1024] , sum;

void read() {
	int i;
	
	sum = 0;
	scanf ( "%d" , &n );
	for (i = 1; i <= n; i++) {
		scanf ( "%d" , &a[i] );
		sum += a[i];
	}
}

void solve() {
	int i , mn = 1 << 30;
	int xxor = 0;
	
	for (i = 1; i <= n; i++) {
		if ( a[i] < mn ) mn = a[i];
		xxor ^= a[i];
	}
	
	if ( xxor == 0 )
		printf ( "%d\n" , sum - mn );
	else
		printf ( "NO\n" );
}

int main() {
	int i , cases;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d: " , i );
		read();
		solve();
	}
	
	return 0;
}
