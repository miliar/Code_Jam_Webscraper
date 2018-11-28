#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>

using namespace std;
#define _ << ", " <<
#define db(x) cout << #x " == " << x << endl
#define fr(a,b,c) for(int a = b ; a < c ; ++a )


bool read() {
	int n, tmp;
	cin >> n;
	int meo = 1<<30;
	int res = 0;
	int som = 0;
	fr(i,0,n) {
		cin >> tmp;
		meo = min(meo,tmp);
		res ^= tmp;
		som += tmp;
	}
	
	static int caso = 1;
	cout << "Case #" << caso++ << ": ";
	
	if( res ) cout << "NO" << endl;
	else cout << som-meo << endl;
	
	return true;	
}

int main() {
	int t = -1;
	cin >> t;
	while( t-- && read() );
	return 0;
}
