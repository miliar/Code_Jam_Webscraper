#include <cstdio>
#include <algorithm>

const int MAXN = 12;

int n , m;
char a[MAXN][MAXN];
int dp[MAXN][1 << MAXN];

void read() {
	int i;
	
	scanf ("%d%d",&n,&m);
	for (i=0;i<n;i++)
		scanf ("%s",a[i]);
}

int go ( int x , int mask ) {
//	printf ("%d %d\n",x,mask);
	if ( x == -1 ) return 0;
	if ( dp[x][mask] != -1 ) return dp[x][mask];
	int put = 0;
	int i , j;
	int ans = 0;
	int next;
	
	for (i=m - 1;i>=0;i--) {
		put <<= 1;
		if ( a[x][i] == 'x' || (mask & (1 << i)) ) continue;
		put ^= 1;
	}
	
	for (i=put;i>0;i=(i-1)&put) {
		for (j=1;j<m;j++)
			if ( (i & (1 << j)) && (i & (1 << (j-1))) )
				break;
		if ( j != m ) continue;
		
		next = 0;
		for (j=0;j<m;j++) 
			if ( i & (1 << j) ) {
				if ( j ) next |= (1 << (j-1));
				if ( j != m - 1 ) next |= (1 << (j+1));
			}
			
		if ( go ( x - 1 , next ) + __builtin_popcount(i) > ans )
			ans = go ( x - 1 , next ) + __builtin_popcount(i);
	}
	
	if ( go ( x - 1 , 0 ) > ans )
		ans = go ( x - 1 , 0 );
	
	return dp[x][mask] = ans;
}

void solve() {
	memset ( dp , -1 , sizeof dp );
	printf ("%d\n",go ( n - 1 , 0 ));
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
