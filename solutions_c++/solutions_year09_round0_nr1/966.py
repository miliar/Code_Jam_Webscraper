#include <cstdio>

const int MAXD = 1 << 13;
const int MAXL = 1 << 4;

int l , d , n;
char a[MAXD][MAXL] , s[MAXL * 32];
int ok[MAXD];
int t[32];

void read() {
	int i;
	
	scanf ( "%d%d%d" , &l , &d , &n );
	for (i = 1; i <= d; i++)
		scanf ( "%s" , a[i] );
}

void solve() {
	int i , j;
	int p = 0;
	int ans = 0;
	
	for (i = 1; i <= d; i++)
		ok[i] = 1;
	
	for (i = 0; s[i] != '\0'; i++) {
		for (j = 0; j < 26; j++) t[j] = 0;
		
		if ( s[i] == '(' ) {	
			while ( s[i] != ')' ) 
				t[ s[i ++] - 'a' ] = 1;
		} else
			t[ s[i] - 'a' ] = 1;
		
		for (j = 1; j <= d; j++)
			ok[j] &= t[ a[j][p] - 'a' ];
		++ p;
	}
	
	for (i = 1; i <= d; i++)
		ans += ok[i];
	
	printf ( "%d\n" , ans );
}

int main() {
	int i;
	
	read();
	for (i = 1; i <= n; i++) {
		scanf ( "%s" , s );
		printf ( "Case #%d: " , i );
		solve();
	}
	
	return 0;
}
