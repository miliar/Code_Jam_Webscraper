#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1 << 6;

int n;
int a[MAXN];

void read() {
	char buf[MAXN];
	int i , j;
	
	scanf ( "%d" , &n );
	for (i = 1; i <= n; i++) {
		scanf ( "%s" , buf + 1 );
		
		for (j = n; j >= 1; j--)
			if ( buf[j] == '1' )
				break;
			
		a[i] = j;
	}
}

void solve() {
	int i , j;
	int ans = 0;
	
	for (i = 1; i <= n; i++) {
		for (j = i; j <= n; j++)
			if ( a[j] <= i )
				break;
			
		for ( ; j > i; j--) {
			swap ( a[j] , a[j - 1] );
			++ ans;
		}
	}
	
	printf ( "%d\n" , ans );
}

int main() {
	int cases , i;
	
	scanf ( "%d" , &cases );
	
	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d: " , i );
		read();
		solve();
	}
	
	return 0;
}

