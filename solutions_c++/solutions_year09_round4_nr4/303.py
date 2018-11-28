#include <cmath>
#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 4;

struct point {
	int x , y;
	int r;
	
	void read() {
		scanf ( "%d%d%d" , &x , &y , &r );
	}
};

int n;
point a[MAXN];

void read() {
	int i;
	
	scanf ( "%d" , &n );
	for (i = 1; i <= n; i++)
		a[i].read();
}

inline double dist ( double x1 , double y1 , double x2 , double y2 ) {
	return sqrt ( (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) );
}

double get ( point a , point b ) {
	if ( a.x == b.x && a.y == b.y ) 
		return max ( a.r , b.r );
	
	return (dist ( a.x , a.y , b.x , b.y ) + a.r + b.r) / 2.;
}

void solve() {
	double ans = 1e100;
	
	if ( n == 1 ) {
		printf ( "%d\n" , a[1].r );
	} else
		if ( n == 2 )
			printf ( "%d\n" , max ( a[1].r , a[2].r ) );
		else {
			ans = min ( ans , max ( (double)a[1].r , get ( a[2] , a[3] ) ) );
			ans = min ( ans , max ( (double)a[2].r , get ( a[1] , a[2] ) ) );
			ans = min ( ans , max ( (double)a[3].r , get ( a[1] , a[3] ) ) );
			
			printf ( "%lf\n" , ans );
		}
}

int main() {
	int cases , i;
	
	scanf ( "%d" , &cases );
	
	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d: " , i );
		read();
		solve();
	}
	
	return 0;
}

