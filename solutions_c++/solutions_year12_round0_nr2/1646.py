#include <cstdio>
#include <cstring>

const int maxn = 105;

int a[maxn] , n , m , k;

int getmax( int flag , int x )
{
	return (x<2||!flag) ? (x%3==0?x/3:x/3+1) : (x%3==0?x/3+1:(x%3==1?x/3+1:x/3+2));
}

int main()
{
	int cas;
	scanf( "%d" , &cas );
	for ( int d = 1; d <= cas; d++ ) {
		scanf( "%d%d%d" , &n , &m , &k );
		for ( int i = 0; i < n; i++ ) scanf( "%d" , &a[i] );
		int ans = 0;
		for ( int i = 0; i < n; i++ ) {
			if ( getmax(0,a[i]) >= k ) ans++;
			else if ( m && getmax(1,a[i]) >= k ) {
				ans++;
				m--;
			}
		}
		printf( "Case #%d: %d\n" , d , ans );
	}
	return 0;
}
