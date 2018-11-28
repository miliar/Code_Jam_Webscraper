#include <queue>
#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 16;

struct el {
	int x , y;
	int m1 , m2;
	
	el () {
		x = y = m1 = m2 = 0;
	}
	
	el ( int _x , int _y , int _m1 , int _m2 ) {
		x = _x; y = _y; m1 = _m1; m2 = _m2;
	}
};

int n , m , f;
int used[16][8][1 << 6][1 << 6];
char c[MAXN][MAXN];
int a[MAXN][MAXN];

deque < el > q;

void read() {
	int i;
	
	scanf ( "%d%d%d" , &n , &m , &f );
	for (i = 0; i < n; i++)
		scanf ( "%s" , c[i] );
}

void psh ( int x , int y , int m1 , int m2 , int d , int ch ) {
	if ( used[x][y][m1][m2] == -1 ) {
		used[x][y][m1][m2] = d;
		
		if ( !ch )
			q.push_front ( el ( x , y , m1 , m2 ) );
		else
			q.push_back ( el ( x , y , m1 , m2 ) );
	}
}

inline int contain ( int mask , int x ) {
	return mask & (1 << x);
}

inline int del ( int mask , int x ) {
	return mask & ~(1 << x);
}

int get ( int x ) {
	if ( x == n ) return 0;
	int mask = 0;
	int i;
	
	for (i = 0; i < m; i++)
		mask |= a[x][i] << i;
	
	return mask;
}

void solve() {
	int i , j;
	int x = 0 , y = 0 , m1 , m2;
	int e;
	int ans = -1;
	
	for (i= 0; i < n; i++)
		for (j = 0; j < m; j++)
			a[i][j] = (c[i][j] == '#');
	
	for (i = 0; i < m; i++) {
		x |= a[0][i] << i;
		y |= a[1][i] << i;
	}
	
	while ( !q.empty() ) q.pop_front();
	memset ( used , -1 , sizeof used );
	
	psh ( 0 , 0 , x , y , 0 , 0 );
	
	while ( !q.empty() ) {
		el t = q.front();
		q.pop_front();
		
		x = t.x;
		y = t.y;
		m1 = t.m1;
		m2 = t.m2;
		
		e = used[x][y][m1][m2];
		
//		printf ( "%d %d %d %d          %d\n" , x , y , m1 , m2 , e );
		
		if ( x == n - 1 ) {
			if ( ans == -1 || e < ans )
				ans = e;
			continue;
		}
		
		if ( y && !contain ( m1 , y - 1 ) && contain ( m2 , y - 1 ) )
			psh ( x , y - 1 , m1 , m2 , e , 0 );
		if ( y < m - 1 && !contain ( m1 , y + 1 ) && contain ( m2 , y + 1 ) )
			psh ( x , y + 1 , m1 , m2 , e , 0 );
		
		if ( y && !contain ( m1 , y - 1 ) && contain ( m2 , y - 1 ) )
			psh ( x , y , m1 , del ( m2 , y - 1 ) , e + 1 , 1 );
		
		if ( y < m - 1 && !contain ( m1 , y + 1 ) && contain ( m2 , y + 1 ) )
			psh ( x , y , m1 , del ( m2 , y + 1 ) , e + 1 , 1 );
		
		if ( y && !contain ( m1 , y - 1 ) && !contain ( m2 , y - 1 ) ) {
			for (i = x + 2; i < n; i++)
				if ( a[i][y - 1] )
					break;
			-- i;
			
			if ( i - x <= f ) {
				if ( x + 1 == i )
					psh ( i , y - 1 , m2 , get ( i + 1 ) , e , 0 );
				else
					psh ( i , y - 1 , get ( i ) , get ( i + 1 ) , e , 0 );
			}
		}
		
		if ( y < m - 1 && !contain ( m1 , y + 1 ) && !contain ( m2 , y + 1 ) ) {
			for (i = x + 2; i < n; i++)
				if ( a[i][y + 1] )
					break;
			-- i;
			
		//	printf ( " --- %d \n" , i );
			
			if ( i - x <= f ) {
				if ( x + 1 == i ) {
				//	printf ( "aaaaaaaaaa %d %d %d %d\n" , i , y + 1 , m2 , get ( i + 1 ) );
					psh ( i , y + 1 , m2 , get ( i + 1 ) , e , 0 );
				} else
					psh ( i , y + 1 , get ( i ) , get ( i + 1 ) , e , 0 );
			}
		}
	}
	
	if ( ans == -1 )
		printf ( "No\n" );
	else
		printf ( "Yes %d\n" , ans );
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

