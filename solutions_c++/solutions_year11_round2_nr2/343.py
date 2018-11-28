#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n , d;
vector < double > a;

void read() {
	int i;
	int x , y;
	
	a.clear();
	
	scanf ( "%d%d" , &n , &d );
	for (i = 1; i <= n; i++) {
		scanf ( "%d%d" , &x , &y );
		
		while ( y -- )
			a.push_back ( x );
	}
	
	n = (int)a.size();
}

int can ( double x ) {
	double f = a[0] - x;
	int i;
	
	for (i = 1; i < n; i++) {
		if ( a[i] + x - f < d )
			return 0;
		
		if ( (a[i] - x) <= f + d )
			f = f + d;
		else
			f = a[i] - x;
	}
	
	return 1;
}

void solve() {
	double l , r , mid;
	
	sort ( a.begin() , a.end() );	
	
	l = 0;
	r = 1e10;
	
	for (int iter = 0; iter < 200; iter++) {
		mid = (l + r) / 2.;	
		
// 		printf ( "%lf %lf     %lf        %d\n" , l , r , mid , can ( mid ) );
		
		if ( can ( mid ) )
			r = mid;
		else
			l = mid;
	}
	
	printf ( "%.9lf\n" , (l + r) / 2. );
}

int main() {
	int i , cases;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d: " , i );
		solve();
	}
	
	return 0;
}
