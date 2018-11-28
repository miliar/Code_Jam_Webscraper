#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int INF = (1 << 30) - 3;
const int MAXN = 1 << 11;

int n , m;
int a[MAXN];
int val[MAXN];
int mx[MAXN][MAXN];

int dp[MAXN][16];

void read() {
	int i;
	
	scanf ( "%d" , &n );
	m = 1 << n;
	for (i = 1; i <= m; i++) {
		scanf ( "%d" , &a[i] );
		a[i] = n - a[i];
	}
}

int go ( int x , int y , int l , int r ) {
	int &ans = dp[x][y];
	if ( ans != -1 ) return ans;
	if ( mx[l][r] <= y ) return ans = 0;
	if ( l == r ) return INF;
	
	int mid = l + (r - l) / 2 , cur;
	ans = INF;
	
	if ( y < 11 ) {
		cur = go ( x * 2 , y + 1 , l , mid ) + go ( x * 2 + 1 , y + 1 , mid + 1 , r );
		
		if ( cur < ans )
			ans = min ( ans , cur + val[x] );
	}
	ans = min ( ans , go ( x * 2 , y , l , mid ) + go ( x * 2 + 1 , y , mid + 1 , r ) );
	
	return ans;
}

void solve() {
	int i , j;
	
	for (i = 1; i <= m; i++) {
		mx[i][i] = a[i];
		for (j = i + 1; j <= m; j++)
			mx[i][j] = max ( mx[i][j - 1] , a[j] );
	}
	
	memset ( dp , -1 , sizeof dp );
	
	for (i = 1; i <= n; i++) {
	//	printf ( "%d %d\n" , (1 << (n - i)) , 1 << (n - i + 1) );
		for (j = (1 << (n - i)); j < (1 << (n - i + 1)); j++) {
			scanf ( "%d" , &val[j] );
	//		printf ( "%d\n" , val[j] );
		}
	}
		
	printf ( "%d\n" , go ( 1 , 0 , 1 , m ) );
}

int main() {
	int cases;
	int i;
	
	scanf ( "%d" , &cases );
	
	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d: " , i );
		read();
		solve();
	}
	
	return 0;
}
