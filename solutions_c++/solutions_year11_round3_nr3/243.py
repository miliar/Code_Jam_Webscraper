#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

int n,l,h;
int a[120];

bool work() {
	for ( int i=l; i<=h; i++ ) {
		bool t = true;
		for ( int j=1; j<=n; j++ ) {
			if ( i>a[j] && i%a[j]!=0 ) { t = false; break; }
			if ( i<a[j] && a[j]%i!=0 ) { t = false; break; }
		}
		if ( t ) {
			cout << i << endl;
			return true;
		}
	}
	
	return false;
}

int main() {

	freopen( "c.in", "r", stdin );
	freopen( "c.out", "w", stdout );
	
	int T;
	cin >> T;
	
	for ( int i=1; i<=T; i++ ) {
		printf( "Case #%d: ", i );
		cin >> n >> l >> h;
		for ( int j=1; j<=n; j++ ) cin >> a[j];
		if ( work()==false ) cout << "NO" << endl; 
	}
	
	return 0;
}
