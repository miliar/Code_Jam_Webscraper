#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
char a[128];
vector < int > f;

void read() {
	scanf ( "%s" , a );
	n = (int)strlen ( a );
	f.clear();
}

void solve() {
	long long t = 0 , p , u;
	int i , j;
	
	for (i = 0; i < n; i++)
		if ( a[i] == '?' ) f.push_back ( i );
		
	for (i = 0; i < (1 << (int)f.size()); i++) {
		for (j = 0; j < (int)f.size(); j++)
			if ( i & (1 << j) )
				a[ f[j] ] = '1';
			else
				a[ f[j] ] = '0';
			
		t = 0;
		for (j = 0; j < n; j++)
			t = t * 2 + (a[j] - '0');
		
		p = (long long)sqrt ( (double)t );
		int ok = 0;
		
		for (u = p - 3; u <= p + 3; u++)
			if ( u * u == t && u > 0 ) {
// 				printf ( "%lld   %lld\n" , u , t );
				ok = 1;
			}
			
		if ( ok ) {
			printf ( "%s\n" , a );
			fprintf ( stderr , "%s\n" , a );
		}
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
