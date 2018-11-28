#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n , m , kk;
char a[128][8] , b[128][8] , c[128];
vector < char > ans;

void read() {
	int i;
	
	scanf ( "%d" , &n );
	for (i = 1; i <= n; i++)
		scanf ( "%s" , a[i] );
	
	scanf ( "%d" , &m );
	for (i = 1; i <= m; i++)
		scanf ( "%s" , b[i] );
	
	scanf ( "%d" , &kk );
	scanf ( "%s" , c );
}

void solve() {
	int i , j , k , d;
	
	ans.clear();
	for (i = 0; i < kk; i++) {
		ans.push_back ( c[i] );
		
		for (j = 1; j <= n; j++)
			if ( (int)ans.size() >= 2 ) {
				if ( (ans.back() == a[j][0] && ans[ (int)ans.size() - 2 ] == a[j][1]) ||
				     	(ans.back() == a[j][1] && ans[ (int)ans.size() - 2 ] == a[j][0]) ) {
					ans.pop_back();
					ans.pop_back();
					
					ans.push_back ( a[j][2] );
				}
			}
			
		for (j = 1; j <= m; j++)
			for (k = 0; k < (int)ans.size(); k++)
				for (d = 0; d < (int)ans.size(); d++)
					if ( ans[k] == b[j][0] && ans[d] == b[j][1] )
						ans.clear();
	}
	
	printf ( "[" );
	for (i = 0; i < (int)ans.size(); i++) {
		printf ( "%c" , ans[i] );
		if ( i + 1 < (int)ans.size() )
			printf ( ", " );
	}
	printf ( "]\n" );
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
