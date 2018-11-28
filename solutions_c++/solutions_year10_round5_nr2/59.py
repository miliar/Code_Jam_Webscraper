#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

long long t;
int n;
int a[128];

int d[1 << 17];
deque < int > q;

void read() {
	int i;

	scanf ( "%lld%d" , &t , &n );

	for (i = 1; i <= n; i++)
		scanf ( "%d" , &a[i] );
}

long long calc ( int x ) {
	while ( !q.empty() ) q.pop_front();
	int i , y;
	int next;

//	printf ( "%d\n" , x );
	
	memset ( d , -1 , sizeof d );
	d[0] = 0;
	q.push_front ( 0 );

	while ( !q.empty() ) {
		y = q.front();
		q.pop_front();

	//	printf ( "%d   %d  %d %d %d\n" , y , d[y] , a[1] , a[2] , a[3] );

		if ( (t - y) % x == 0 )
			return (long long)d[y] + (t - y) / (long long)x;

		for (i = 1; i <= n; i++)
			if ( y + a[i] >= x ) {
				next = (y + a[i]) % x;
				if ( d[next] == -1 || d[next] > d[y] ) {
					q.push_front ( next );
					d[ next ] = d[y];
				}
			} else {
				if ( d[ y + a[i] ] == -1 ) {
					q.push_back ( y + a[i] );
					d[ y + a[i] ] = d[y] + 1;
				}
			}
	}

	return -1;
}

void solve() {
	int i;
	long long ans;
	int x = -1;

//	printf ( "%lld\n" , calc ( 39 ) );	return ;
	
for (i = 1; i <= n; i++)
		if ( x < a[i] )
			x = a[i];

	ans = calc ( x );
	
	if ( ans == -1 )
		printf ( "IMPOSSIBLE\n" );
	else
		printf ( "%lld\n" , ans );
}

int main() {
	int i , cases;

	scanf ( "%d" , &cases );

	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d: " , i );
		read();
		solve();

		fflush ( stdout );

	//	break;
	}

	return 0;
}
