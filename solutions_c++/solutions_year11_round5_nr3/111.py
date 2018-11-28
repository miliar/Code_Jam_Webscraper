#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

int n , m;
char a[8][8];
vector < pair < int , int > > b[8][8];
int used[8][8];

void read() {
	int i;
	
	scanf ( "%d%d" , &n , &m );
	for (i = 0; i < n; i++)
		scanf ( "%s" , a[i] );
}

int dfs ( int x , int y , int sx , int sy ) {
	used[x][y] = 1;
	int i;
	
	for (i = 0; i < (int)b[x][y].size(); i++)
		if ( used[ b[x][y][i].first ][ b[x][y][i].second ] ) {
			if ( b[x][y][i].first == sx && b[x][y][i].second == sy ) return 0;
			return 1;
		} else
			if ( dfs ( b[x][y][i].first , b[x][y][i].second , sx , sy ) )
				return 1;
		
	return 0;
}

void solve() {
	int ans = 0;
	int i , j , k;
	int mask;
	
	for (i = 0; i < (1 << (n * m)); i++) {
		mask = i;
		
		for (j = 0; j < n; j++)
			for (k = 0; k < m; k++) {
				b[j][k].clear();
				
				if ( mask & 1 ) {
					if ( a[j][k] == '/' )
						b[j][k].push_back ( make_pair ( (j - 1 + n) % n , (k + 1) % m ) );
					
					if ( a[j][k] == '\\' )
						b[j][k].push_back ( make_pair ( (j - 1 + n) % n , (k - 1 + m) % m ) );
					
					if ( a[j][k] == '-' )
						b[j][k].push_back ( make_pair ( j ,  (k - 1 + m) % m  ) );
					
					if ( a[j][k] == '|' )
						b[j][k].push_back ( make_pair ( (j - 1 + n) % n , k ) );
				} else {
					if ( a[j][k] == '/' )
						b[j][k].push_back ( make_pair ( (j + 1 + n) % n , (k - 1 + m) % m ) );
					
					if ( a[j][k] == '\\' )
						b[j][k].push_back ( make_pair ( (j + 1 + n) % n , (k + 1 + m) % m ) );
					
					if ( a[j][k] == '-' )
						b[j][k].push_back ( make_pair ( j ,  (k + 1 + m) % m  ) );
					
					if ( a[j][k] == '|' )
						b[j][k].push_back ( make_pair ( (j + 1 + n) % n , k ) );
				}
				
				mask >>= 1;
			}
			
		memset ( used , 0 , sizeof used );
		int ok = 0;
			
		for (j = 0; j < n; j++)
			for (k = 0; k < m; k++)
				if ( !used[j][k] )
					ok |= dfs ( j , k , j , k );
				
		if ( !ok ) {
			++ ans;
// 			for (j = 0; j < n; j++) {
// 				for (k = 0; k < m; k++)
// 					printf ( "(%d,%d) " , b[j][k][0].first , b[j][k][0].second );
// 				printf ( "\n" );
// 			}
// 			printf ( "\n" );
		}
	}
	
	printf ( "%d\n" , ans );
}

int main() {
	int i , cases;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d: " , i );
		solve();
		
// 		break;
	}
	
	return 0;
}