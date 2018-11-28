#include <cstdio>
#include <algorithm>

const int MOD = 10007;
const int MAXN = 1 << 7;

int n , m;
int bad[MAXN][MAXN];
int dp[MAXN][MAXN];

void read() {
	memset ( bad , 0 , sizeof bad );
	int x , y , r;
	
	scanf ("%d%d%d",&n,&m,&r);
	while ( r -- ) {
		scanf ("%d%d",&x,&y);
		bad[x][y] = 1;
	}
}

int go ( int x , int y ) {
	if ( x == 1 && y == 1 ) return 1;
	if ( x < 1 || y < 1 || x > n || y > m || bad[x][y] ) return 0;
	if ( dp[x][y] != -1 ) return dp[x][y];
	
	return dp[x][y] = (go ( x - 2 , y - 1 ) + go ( x - 1 , y - 2 )) % MOD;
}

void solve() {
	memset ( dp , -1 , sizeof dp );
	printf ("%d\n",go(n,m));
}

int main() {
	int i , k;
	
	scanf ("%d",&k);
	
	for (i=1;i<=k;i++) {
		read();
		printf ("Case #%d: ",i);
		solve();	
	}
	
	return 0;
}
