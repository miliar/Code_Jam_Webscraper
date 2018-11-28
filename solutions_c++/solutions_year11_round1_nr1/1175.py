#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

int T;
int pd,pg;
long long n;

bool work() {
	
	int tpd = pd;

	// 化简
	int d = 100;
	if ( pd%2==0 ) {
		pd /= 2;
		d /= 2;
	}
	if ( pd%2==0 ) {
		pd /= 2;
		d /= 2;
	}
	if ( pd%5==0 ) {
		pd /= 5;
		d /= 5;
	}
	if ( pd%5==0 ) {
		pd /= 5;
		d /= 5;
	}
	if ( d>n ) return false;
	
	pd = tpd;
	
	if ( pg==0 ) {
		if ( pd==0 ) return true;
		else return false;
	} 
	else if ( pg==100 ) {
		if ( pd==100 ) return true;
		else return false;
	}
	else return true;
}

int main() {
	freopen( "a.in", "r", stdin );
	freopen( "aa.out", "w", stdout );
	cin >> T;
	for ( int i=1; i<=T; i++ ) {
		cout << "Case #" << i << ": ";
		cin >> n >> pd >> pg;
		if ( work() ) cout << "Possible" << endl;
		else cout << "Broken" << endl;
	}
	
	return 0;
}
