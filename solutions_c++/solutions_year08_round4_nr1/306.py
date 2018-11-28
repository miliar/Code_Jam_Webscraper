#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1 << 14;
const int inf = (1 << 30) - 2;

int n , goal;
int op[MAXN];
int ch[MAXN];

int dp[MAXN][2];

void read() {
	int i;
	
	scanf ("%d%d",&n,&goal);
	
	for (i=1;i<=n;i++) {
		scanf ("%d",&op[i]);
		if ( 2 * i <= n ) 
			scanf ("%d",&ch[i]);
	}
}

int go ( int x , int y ) {
	if ( dp[x][y] != -1 ) return dp[x][y];
	if ( 2 * x > n ) {
		if ( op[x] == y )
			return dp[x][y] = 0;
		return dp[x][y] = inf;
	}
	int ans = inf;
	int o = op[x];
	
	if ( y == 0 ) {
		if ( o )
			ans = min ( go ( 2 * x , 0 ) , go ( 2 * x + 1 , 0 ) );
		else
			ans = min ( inf , go ( 2 * x , 0 ) + go ( 2 * x + 1 , 0 ) );
	} else {
		if ( o ) 
			ans = min ( inf , go ( 2 * x , 1 ) + go ( 2 * x + 1 , 1 ) );
		else
			ans = min ( go ( 2 * x , 1 ) , go ( 2 * x + 1 , 1 ) );
	}
	
	if ( !ch[x] ) return dp[x][y] = ans;
	o ^= 1;
	
	if ( y == 0 ) {
		if ( o )
			ans = min ( ans , min ( go ( 2 * x , 0 ) , go ( 2 * x + 1 , 0 ) ) + 1 );
		else
			ans = min ( ans , min ( inf , go ( 2 * x , 0 ) + go ( 2 * x + 1 , 0 ) ) + 1 );
	} else {
		if ( o ) 
			ans = min ( ans , min ( inf , go ( 2 * x , 1 ) + go ( 2 * x + 1 , 1 ) ) + 1 );
		else
			ans = min ( ans , min ( go ( 2 * x , 1 ) , go ( 2 * x + 1 , 1 ) ) + 1 );
	}
	
	return dp[x][y] = ans;
}

void solve() {
	memset ( dp , -1 , sizeof dp );
	
	if ( go ( 1 , goal ) == inf ) printf ("IMPOSSIBLE\n");
	else
		printf ("%d\n",go(1,goal));
}

int main() {
	int k;
	int i;
	
	scanf ("%d",&k);
	
	for (i=1;i<=k;i++) {
		printf ("Case #%d: ",i);
		read();
		solve();
	}

	return 0;
}
