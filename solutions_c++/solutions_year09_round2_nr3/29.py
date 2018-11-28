#include <queue>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

const int dx[] = { -1 , 0 , 0 , 1 };
const int dy[] = { 0 , -1 , 1 , 0 };

const int ZERO = 1 << 9;
const int MAX = ZERO << 1;

struct el {
	int x , y;
	int c;
	int val;
	
	el () {}
	el ( int _x , int _y , int _c , int _val ) {
		x = _x;
		y = _y;
		c = _c;
		val = _val;
	}
};

struct el2 {
	int x , y , c;
	
	el2 () {}
	el2 ( int _x , int _y , int _c ) {
		x = _x; y = _y; c = _c;
	}
};

struct Cmp {
	bool operator () ( el a , el b ) {
		return a.val > b.val;
	}
};

int n , m;
char a[32][32];
int b[64];
int dp[32][32][MAX];
string p[32][32][MAX];
int ans[64];
string ret[64];

priority_queue < el , vector < el > , Cmp > pq;

void read() {
	int i;
	
	scanf ( "%d%d" , &n , &m );
	for (i = 1; i <= n; i++)
		scanf ( "%s" , a[i] + 1 );
}

int calc ( int x , char c , int y ) {
	if ( c == '+' ) return x + y;
	return x - y;
}

void psh ( int x , int y , int c , int val , int lx , int ly , int lc ) {
	if ( c < 0 || c >= MAX ) return ;
	
	if ( dp[x][y][c] == -1 || (dp[x][y][c] > val || dp[x][y][c] == val && p[lx][ly][lc] + a[x][y] < p[x][y][c]) ) {
		if ( lx == -1 ) p[x][y][c] = a[x][y];
		else p[x][y][c] = p[lx][ly][lc] + a[x][y];
		dp[x][y][c] = val;
		pq.push ( el ( x , y , c , val ) );
	}
}

void dijkstra () {
	int i;
	int x , y;
	
//	printf ( "BAU\n" );
//	psh ( x , y , ZERO + a[x][y] - '0' , 1 , -1 , -1 , -1 );
	
	while ( !pq.empty() ) {
		el t = pq.top();
		pq.pop();
		
	//	printf ( "asasda\n" );
		if ( dp[ t.x ][ t.y ][ t.c ] > t.val ) continue;
		
//		printf ( "%d %d %d      %d\n" , t.x , t.y , t.c , t.val );
		
		for (i = 0; i < 4; i++) {
			x = t.x + dx[i];
			y = t.y + dy[i];
			
			if ( x > 0 && y > 0 && x <= n && y <= n ) {
				if ( a[ t.x ][ t.y ] == '+' || a[ t.x ][ t.y ] == '-' )
					psh ( x , y , calc ( t.c , a[ t.x ][ t.y ] , a[x][y] - '0' ) , t.val + 1 , t.x , t.y , t.c );
				else
					psh ( x , y , t.c , t.val + 1 , t.x , t.y , t.c );
			}
		}
	}
}

void solve() {
	int i , j , k , d , e;
	string temp;
	
	memset ( dp , -1 , sizeof dp );
	
	for (i = 1; i <= m; i++) {
		scanf ( "%d" , &b[i] );
		ans[i] = 1 << 30;
	}
	
	memset ( dp , -1 , sizeof dp );
	
	for (i = 1; i <= n; i++)
		for (j = 1; j <= n; j++)
			if ( a[i][j] != '+' && a[i][j] != '-' ) {
			//	printf ( "HERE\n" );
				psh ( i , j , ZERO + a[i][j] - '0' , 1 , -1 , -1 , -1 );
			//	printf ( "OUT\n" );
			}
			
	dijkstra();
				
				for (d = 1; d <= n; d++)
					for (e = 1; e <= n; e++)
						for (k = 1; k <= m; k++) {
					//		printf ( "%d %d      %d %d         %d            %d\n" , i , j , d , e , k , dp[d][e][ ZERO + b[k] ] );
							if ( dp[d][e][ ZERO + b[k] ] != -1 )
								if ( dp[d][e][ ZERO + b[k] ] <= ans[k] ) {
									temp = p[d][e][ ZERO + b[k] ];
							//		printf ( "%s\n" , printpath ( d , e , ZERO + b[k] ).c_str() );
									
									if ( dp[d][e][ ZERO + b[k] ] < ans[k] || (dp[d][e][ ZERO + b[k] ] == ans[k] && temp < ret[k]) ) {
										ans[k] = dp[d][e][ ZERO + b[k] ];
										ret[k] = temp;
									}
								}
						}
				
	for (i = 1; i <= m; i++) 
		printf ( "%s\n" , ret[i].c_str() );
	
	fflush ( stdout );
}

int main() {
	int cases , i;
	
	scanf ( "%d" , &cases );
	
	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d:\n" , i );
		read();
		solve();
	}
	
	return 0;
}
