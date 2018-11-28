#include <sstream> 
#include <iostream>
#include <string.h>
#include <algorithm>
#include <stdlib.h> 
#include <stdio.h> 
#include <numeric>
#include <math.h>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

int dx[] = { -1 , 0 , 0 , 1 };
int dy[] = { 0 , -1 , 1 , 0 };

map < vector < pair < int , int > >, int > used;
queue < pair < vector < pair < int , int > > , int > > q;
vector < pair < int , int > > cur;
int n , m;
char a[32][32] , b[32][32];
int u[32][32];
int cnt;
int have[4];

void read() {
	char buf[32];
	int i , j;
	
	scanf ( "%d%d" , &n , &m );
	for (i = 1; i <= n; i++) {
		scanf ( "%s" , buf + 1 );
		
		for (j = 1; j <= m; j++) {
			if ( buf[j] == 'o' || buf[j] == 'w' ) a[i][j] = 'x';
			if ( buf[j] == 'x' || buf[j] == 'w' ) b[i][j] = 'x';
			
			if ( buf[j] == '.' || buf[j] == '#' ) a[i][j] = b[i][j] = buf[j];
			if ( buf[j] == 'o' ) b[i][j] = '.';
			if ( buf[j] == 'x' ) a[i][j] = '.';
		}
	}
}

void dfs ( int x , int y ) {
//	printf ( "--------- %d %d\n" , x , y );
	u[x][y] = cnt;
	have[cnt] ++;
	int i , q , w;
	
	for (i = 0; i < 4; i++) {
		q = x + dx[i];
		w = y + dy[i];
		
		if ( q > 0 && w > 0 && q <= n && w <= m && !u[q][w] && a[q][w] == 'x' ) 
			dfs ( q , w );
	}
}

vector < pair < int , int > > getboard() {
	vector < pair < int , int > > ans;
	int i , j;
	
	for (i = 1; i <= n; i++)
		for (j = 1; j <= m; j++)
			if ( a[i][j] == 'x' )
				ans.push_back ( make_pair ( i , j ) );
			
	return ans;
}

int ok ( int x , int y ) {
	if ( x > 0 && y > 0 && x <= n && y <= m && a[x][y] == '.' )
		return 1;
	return 0;
}

int canmove ( int x , int y , int d ) {
	if ( ok ( x + dx[d] , y + dy[d] ) && ok ( x - dx[d] , y - dy[d] ) ) {
		a[x][y] = '.';
		a[ x + dx[d] ][ y + dy[d] ] = 'x';
		
		return 1;
	}
	
	return 0;
}

int havenei () {
	int i , j , k;
	int q , w;
	
	for (i = 1; i <= n; i++)
		for (j = 1; j <= m; j++)
			if ( a[i][j] == 'x' ) {
				for (k = 0; k < 4; k++) {
					q = i + dx[k];
					w = j + dy[k];
					
					if ( q > 0 && w > 0 && q <= n && w <= m && a[q][w] == 'x' )
						break;
				}
				
				if ( k == 4 )
					return 0;
			}
				
	return 1;
}

void retmove ( int x , int y , int d ) {
	a[x][y] = 'x';
	a[ x + dx[d] ][ y + dy[d] ] = '.';
}

void print() {
	int i , j;
	
	for (i = 1; i <= n; i++) { for (j = 1; j <= m; j++) printf ( "%c" , a[i][j] ); printf ( "\n" ); } printf ( "\n" );
}

void solve() {
	int i , j , k , d;
	int bad;
	int t;
	int bau;
	
	used.clear();
	cur.clear();
	while ( !q.empty() ) q.pop();
	
	cur = getboard();
	
	used[ cur ] = 0;
	q.push ( make_pair ( cur , 1 ) );
	
//	for (i = 1; i <= n; i++) { for (j = 1; j <= m; j++) printf ( "%c" , a[i][j] ); printf ( "\n" ); } printf ( "\n" );
	
	while ( !q.empty() ) {
		cur = q.front().first;
		bau = q.front().second;
		q.pop();
		
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++) {
				if ( a[i][j] == 'x' ) a[i][j] = '.';
				u[i][j] = 0;
			}
			
		bad = 0;
		for (i = 0; i < (int)cur.size(); i++) {
			a[ cur[i].first ][ cur[i].second ] = 'x';
			if ( b[ cur[i].first ][ cur[i].second ] != 'x' )
				bad = 1;
		}
		
	//	for (i = 1; i <= n; i++) { for (j = 1; j <= m; j++) printf ( "%c" , a[i][j] ); printf ( "\n" ); } printf ( "\n" );
		
		t = used[cur];
		if ( !bad ) {
			printf ( "%d\n" , t );
			return ;
		}
		
		memset ( have , 0 , sizeof have );
		cnt = 0;
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++)
				if ( !u[i][j] && a[i][j] == 'x' ) {
					++ cnt;
					dfs ( i , j );
				}
				
		if ( bau == 2 && cnt > 1 ) continue;
		if ( cnt == 1 ) bau = 0;
			
				for (j = 1; j <= n; j++)
					for (k = 1; k <= m; k++)
						if ( a[j][k] == 'x' ) {
		//					printf ( "%d %d             %d %d\n" , j , k , have[1] , have[2] );
							for (d = 0; d < 4; d++) {
							//	printf ( " {{{{{{{{{{{{{{{{{{{       %d %d\n " , j , k );
							//	print();
								if ( canmove ( j , k , d ) ) {
							//		print();
							//		printf ( " }}}}}}}}}}}}}}}}}\n " );
		//							printf ( "%d %d    %d        %d %d           %d\n" , j , k , d , j + dx[d] , k + dy[d] , havenei ( j + dx[d] , k + dy[d] ) );
								//	if ( havenei () ) {
										cur = getboard();
									
										if ( used.find ( cur ) == used.end() ) {
											q.push ( make_pair ( cur , bau + 1 ) );
											used[cur] = t + 1;
										}
										retmove ( j , k  , d );
									}
										
									
						//		}
						}
						}
		
	//	for (i = 1; i <= n; i++) { for (j = 1; j <= m; j++) printf ( "%c" , a[i][j] ); printf ( "\n" ); } printf ( "\n" );		printf ( "----------------- \n\n" );
	//	break;
	
	//	getchar();
	}
	
	printf ( "-1\n" );
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

