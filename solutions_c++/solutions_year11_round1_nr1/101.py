#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>

#define _ << ", " <<
#define db(x) cout << #x " == " << x << endl
#define fr(a,b,c) for( int a = b ; a < c ; ++a )

using namespace std;

long long mdc(long long a, long long b){
	if( b ) return mdc(b,a%b);
	return a;
}

bool read() {
	long long n, pd, pg;
	cin >> n >> pd >> pg;
	
	static int caso = 1;
	if( pd != 100 && pg == 100 || pd != 0 && pg == 0 || 100/mdc(100,pd) > n ) {
		cout << "Case #" << caso++ << ": Broken" << endl;
		return true;
	}
	cout << "Case #" << caso++ << ": Possible" << endl;
	
	return true;
}

int main() {
	int t = -1;
	cin >> t;
	while( t-- && read() );
	return 0;
}
