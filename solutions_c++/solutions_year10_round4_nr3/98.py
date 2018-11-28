#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
int a[1 << 10][1 << 10] , b[1 << 10][1 << 10];

void read() {
	int i , j;
	int x1 , x2 , y1 , y2;
	
	memset ( a , 0 , sizeof a );
	
	scanf ( "%d" , &n );
	while ( n -- ) {
		scanf ( "%d%d%d%d" , &x1 , &y1 , &x2 , &y2 );
		
		for (i = x1; i <= x2; i++)
			for (j = y1; j <= y2; j++)
				a[i][j] = 1;
	}
}

void solve() {
	int ok;
	int ans = 0;
	int i , j;
	
	while ( ++ ans ) {
		for (i = 1; i <= 200; i++)
			for (j = 1; j <= 200; j++) {
				if ( a[i][j] && !a[i - 1][j] && !a[i][j - 1] )
					b[i][j] = 0;
				else
					if ( !a[i][j] && a[i - 1][j] && a[i][j - 1] )
						b[i][j] = 1;
					else
						b[i][j] = a[i][j];
			}
			
		ok = 0;
			
		for (i = 1; i <= 200; i++)
			for (j = 1; j <= 200; j++) {
				a[i][j] = b[i][j];
				
				if ( b[i][j] )
					ok = 1;
			}
			
		if ( !ok ) break; 
	}
	
	printf ( "%d\n" , ans );
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
