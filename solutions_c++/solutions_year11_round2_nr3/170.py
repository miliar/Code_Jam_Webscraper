#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 1 << 11;

int n , m;
int q[MAXN] , w[MAXN];
vector < int > have[MAXN];
vector < int > st;

int fnd;
int col[MAXN];
int save[MAXN];
int used[MAXN];
int c;

vector < vector < int > > t;

void read() {
	int i;
	
	c = 0;
	for (i = 0; i < MAXN; i++) have[i].clear();
	t.clear();
	st.clear();
	
	scanf ( "%d%d" , &n , &m );
	for (i = 1; i <= m; i++) scanf ( "%d" , &q[i] );
	for (i = 1; i <= m; i++) scanf ( "%d" , &w[i] );
}

int ok ( int cols ) {
	int i , j;
	
	for (i = 0; i < (int)t.size(); i++) {
		++ c;
		for (j = 0; j < (int)t[i].size(); j++)
			used[ col[ t[i][j] ] ] = c;
		
		for (j = 1; j <= cols; j++)
			if ( used[j] != c )
				return 0;
	}
	
	return 1;
}

void go ( int x , int y ) {
	if ( fnd ) return ;
	int i;
	
	if ( x == n + 1 ) {
		if ( ok ( y ) ) {
			for (i = 1; i <= n; i++)
				save[i] = col[i];
			fnd = 1;
		}
			
		return ;
	}
	
	for (i = 1; i <= y; i++) {
		col[x] = i;
		go ( x + 1 , y );
	}
}

void solve() {
	int i , j;
	vector < int > cur;
	
	for (i = 1; i <= m; i++)
		have[ w[i] ].push_back ( q[i] );
	
	for (i = 1; i <= n; i++) {
		sort ( have[i].rbegin() , have[i].rend() );
		
		for (j = 0; j < (int)have[i].size(); j++) {
			cur.clear();
			
			cur.push_back ( i );
			while ( st.back() > have[i][j] ) {
				cur.push_back ( st.back() );
				st.pop_back();
			}
			cur.push_back ( st.back() );
			
			t.push_back ( cur );
		}
		
		st.push_back ( i );		
	}
	t.push_back ( st );

	for (i = 1; i <= n; i++) {
		fnd = 0;
		go ( 1 , i );		
		
		if ( !fnd )
			break;
	}
	
	printf ( "%d\n" , i - 1 );
	for (i = 1; i <= n; i++) {
		printf ( "%d" , save[i] );
		if ( i == n )
			printf ( "\n" );
		else
			printf ( " " );
	}
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
