#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 1 << 7;

struct el {
	int x , y;
	int val;
	
	el () {}
	el ( int _x , int _y , int _val ) {
		x = _x; y = _y; val = _val;
	}
};

int dx[] = { -1 , 0 , 0 , 1 };
int dy[] = { 0 , -1 , 1 , 0 };

int n , m;
int a[MAXN][MAXN];
el b[MAXN * MAXN];
int used[MAXN][MAXN];
vector < pair < int , int > > f[MAXN][MAXN];
char ans[32];
int t;
int c;

void read() {
	int i , j;
	
	t = 0;
	scanf ( "%d%d" , &n , &m );
	for (i = 1; i <= n; i++)
		for (j = 1; j <= m; j++) {
			scanf ( "%d" , &a[i][j] );
			b[ ++ t ] = el ( i , j , a[i][j] );
		}
}

int cmp ( el a , el b ) {
	return a.val < b.val;
}

void dfs ( int x , int y ) {
	used[x][y] = c;
	int i;
	
	for (i = 0; i < (int)f[x][y].size(); i++)
		dfs ( f[x][y][i].first , f[x][y][i].second );
}

void solve() {
	int i , j , k;
	int q , w;
	int best , idx;
	char let = 'a';
	
	sort ( b + 1 , b + t + 1 , cmp );
	
	c = 0;
	memset ( used , 0 , sizeof used );
	memset ( ans , 0 , sizeof ans );
	for (i = 1; i <= n; i++)
		for (j = 1; j <= m; j++)
			f[i][j].clear();
	
	for (i = 1; i <= n; i++)
		for (j = 1; j <= m; j++) {
			best = -1;
			idx = -1;
			
			for (k = 0; k < 4; k++) {
				q = i + dx[k];
				w = j + dy[k];
				
				if ( q > 0 && w > 0 && q <= n && w <= m && (best == -1 || a[q][w] < best) ) {
					best = a[q][w];
					idx = k;
				}
			}
			
			if ( best != -1 && best < a[i][j] )
				f[ i + dx[idx] ][ j + dy[idx] ].push_back ( make_pair ( i , j ) );
		}
	
	for (i = 1; i <= t; i++)
		if ( !used[ b[i].x ][ b[i].y ] ) {
			++ c;
			dfs ( b[i].x , b[i].y );
		}
		
	for (i = 1; i <= n; i++)
		for (j = 1; j <= m; j++) {
			if ( ans[ used[i][j] ] == 0 )
				ans[ used[i][j] ] = let ++;
			printf ( "%c" , ans[ used[i][j] ] );
			
			if ( j == m )
				printf ( "\n" );
			else
				printf ( " " );
		}
}

int main() {
	int cases , i;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		
		printf ( "Case #%d: \n" , i );
		solve();
	}
	
	return 0;
}
