#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <cmath>
#include <sstream>
using namespace std;
typedef long long LL;
typedef vector < int > VI;
#define SZ(X) ((int)X.size())
int area ( int xa , int ya , int xb ,int yb ,int xc ,int yc ) {
	return abs (( xb*ya - xa*yb) + ( xc*yb - xb*yc ) + (xa*yc - xc*ya ) );
}
int main() {
	int t;
	cin >> t;
	for ( int n__ = 1 ; n__ <= t; n__ ++ ) {
		cout << "Case #" << n__ <<": " ;
		int N,M , req;
		cin >> N >> M >> req;
		for ( int x1 = 0 ; x1 <= N ; x1 ++ )
		for ( int y1 = 0 ; y1 <= M ; y1 ++ )
		for ( int x2 = 0;  x2 <= N ; x2 ++ )
		for ( int y2 = 0; y2 <= M ; y2 ++ ) {
			if ( area ( 0 , 0 , x1 , y1 , x2 , y2 ) == req ) {
			cout <<"0 0 " << x1<<" " << y1 <<" " << x2 <<" " << y2 << endl;
			goto next1;
			}
		}
		cout << "IMPOSSIBLE" << endl;
		next1:;
		continue;
	}
	return 0;
}
