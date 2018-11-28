#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector < int > a[128] , b[128];

void read() {
	int next = 0;
	int i , j;
	int row , col;
	int x;
	
	scanf ( "%d" , &n );
	
	for (i = 1; i <= 2 * n; i++) {
		a[i].clear();
		b[i].clear();
	}
	
	for (i = 1; i <= n; i++) {
		++ next;
		
		row = i;
		col = n - row;
	
		for (j = 1; j <= i; j++) {
			scanf ( "%d" , &x );
			a[next].push_back ( x );
			
			b[col].push_back ( x );
			col += 2;
		}
	}
	for (i = n - 1; i >= 1; i--) {
		++ next;
		
		row = i;
		col = n - row;
		
		for (j = 1; j <= i; j++) {
			scanf ( "%d" , &x );
			a[next].push_back ( x );
			
			b[col].push_back ( x );
			col += 2;
		}
	}
}

int can ( int x , int y ) {
	int i , j;
	int l , r;
	
	for (i = 1; i < 2 * n; i++) {
		l = 0;
		r = (int)a[i].size() - 1;
		
		r -= x;
		l += y;
		
		for (j = l; j <= r; j++)
			if ( a[i][j] != a[i][r - (j - l)] )
				return 0;
	}
	
	return 1;
}

int can2 ( int x , int y ) {
	int i , j;
	int l , r;
	
	for (i = 1; i < 2 * n; i++) {
		l = 0;
		r = (int)b[i].size() - 1;
		
		r -= x;
		l += y;
		
		for (j = l; j <= r; j++)
			if ( b[i][j] != b[i][r - (j - l)] )
				return 0;
	}
	
	return 1;
}

void solve() {
	int i , j;
	int t1 = 1 << 30 , t2 = 1 << 30;
	/*
	for (i = 1; i <= 2 * n; i++) {
		printf ( "%d ==> " , i );
		for (j = 0; j < (int)b[i].size(); j++)
			printf ( "%d , " , b[i][j] );
		printf ( "\n" );
	}
	*/
	for (i = 0; i <= n; i++)
		for (j = 0; j <= n; j++) {
			if ( i && j ) continue;
			int now = n + i + j;
			
			if ( now < t1 && can ( i , j ) )
				t1 = now;
		}
		
	for (i = 0; i <= n; i++)
		for (j = 0; j <= n; j++) {
			if ( i && j ) continue;
			int now = n + i + j;
			
			if ( now < t2 && can2 ( i , j ) )
				t2 = now;
		}
		
//	printf ( "%d %d\n" , t1 , t2 );
		
	printf ( "%d\n" , (t1 + t2 - n) * (t1 + t2 - n) - n * n );
}

int main() {
	int i , cases;

	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d: " , i );
		read();
		solve();
	}
	
	return 0;
}
