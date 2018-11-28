#include <cstdio>
#include <cstring>

const int MAXN = 1 << 9;
const int MAXM = 1 << 5;

int n , m;
char a[MAXN];
char s[MAXM] = "welcome to code jam";
int dp[MAXN][MAXM];

void read() {
	gets ( a );
	
	n = (int)strlen ( a );
	m = (int)strlen ( s );
}

void solve() {
	int i , j;
	int ans;
	
	for (i = 0; i <= n; i++)
		dp[i][0] = 1;
	
	for (i = 1; i <= n; i++)
		for (j = 1; j <= m; j++) {
			dp[i][j] = dp[i - 1][j];
	
			if ( a[i - 1] == s[j - 1] )
				dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % 10000;
		}
		
	ans = dp[n][m];
	
	if ( ans < 1000 )
		printf ( "0" );
	if ( ans < 100 )
		printf ( "0" );
	if ( ans < 10 )
		printf ( "0" );
	printf ( "%d\n" , ans );
}

int main() {
	int cases;
	int i;
	
	scanf ( "%d\n" , &cases );
	
	for (i = 1; i <= cases; i++) {
		read();
		
		printf ( "Case #%d: " , i );
		solve();
	}
	
	return 0;
}
