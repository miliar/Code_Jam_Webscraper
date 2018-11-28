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

int num[2000],n;

bool read() {
	cin >> n;
	fr(i,0,n) cin >> num[i];
	
	int res = 0;
	fr(i,0,n) if( num[i] ) {
		int t = 1;
		int at = num[i]-1;
		num[i] = 0;
		while( at != i ) {
			int pr = num[at]-1;
			num[at] = 0;
			at = pr;
			t++;
		}
		if( t > 1 ) res += t;
	}
	
	
	static int caso  =1;
	cout << "Case #" << caso++ << ": ";
	cout << res << ".000000" << endl;
	
	return true;	
}

int main() {
	int t = -1;
	cin >> t;
	while( t-- && read() );
	return 0;
}
