#include <cstdio>
#include <cstring>
#include <algorithm>

const int MAXN = 64;

int n;
char a[MAXN];
int cnt[32] , b[MAXN] , h[32];

void read() {
	scanf ( "%s" , a );
	n = (int)strlen ( a );
}

void solve() {
	int i , j , k;
	int smallest = 10;
	
	memset ( cnt , 0 , sizeof cnt );
	
	for (i = 0; i < n; i++) {
		b[i] = a[i] - '0';
		++ cnt[ b[i] ];
		if ( b[i] < smallest && b[i] )
			smallest = b[i];
	}
	
	for (i = 1; i < n; i++)
		if ( b[i - 1] < b[i] )
			break;
		
	if ( i == n ) {
		printf ( "%d" , smallest );
		-- cnt[ smallest ];
		
		for (i = 0; i <= cnt[0]; i++)
			printf ( "0" );
		
		for (i = 1; i < 10; i++)
			if ( cnt[i] ) {
				-- cnt[i];
				printf ( "%d" , i );
				-- i;
			}
	} else {
		for (i = n - 1; i >= 0; i--) {
			memset ( h , 0 , sizeof h );
			for (j = i; j < n; j++)
				++ h[ b[j] ];
			
			for (j = b[i] + 1; j < 10; j++)
				if ( h[j] ) 
					break;
				
			if ( j == 10 ) continue;
		
			-- h[j];
			for (k = 0; k < i; k++)
				printf ( "%d" , b[k] );
			printf ( "%d" , j );
			for (i = 0; i <= 10; i++)
				if ( h[i] ) {
					-- h[i];
					printf ( "%d" , i );
					-- i;
				}
				
			break;
		}
	}
}

int main() {
	int cases , i;
	
	scanf ( "%d" , &cases );
	
	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d: " , i );
		read();
		solve();
		printf ( "\n" );
	}
	
	return 0;
}
