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

int but[1000], n;
char rob[1000], tmp[100];
int prox0[1000], prox1[1000], t0, t1;

bool read() {
	cin >> n;
	t0 = t1 = 0;
	fr(i,0,n) {
		cin >> rob+i >> but[i];
		if( rob[i] == 'O' ) prox0[t0++] = but[i];
		else prox1[t1++] = but[i];
	}
	
	int i0 = 0, i1 = 0;
	int l0 = 1, l1 = 1;
	int x0 = 0, x1 = 0, x = 0;
	
	fr(i,0,n) {
		if( rob[i] == 'O' ) {
			int tmp = abs(but[i]-l0);
			l0 = but[i];
			if( tmp >= x-x0 ) x += tmp-x+x0;
			x++;
			x0 = x;
		} else {
			int tmp = abs(but[i]-l1);
			l1 = but[i];
			if( tmp >= x-x1 ) x += tmp-x+x1;
			x++;
			x1 = x;
		}
	}
	static int caso = 1;
	cout << "Case #" << caso++ << ": " << x << endl;
	
	
	return true;	
}

int main() {
	int t = -1;
	cin >> t;
	while( t-- && read() );
	return 0;
}
