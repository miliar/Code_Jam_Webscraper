#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
using namespace std;
#define PB			push_back
#define ALL(v)			(v).begin() , (v).end()
#define SZ(v)			( (int) v.size() )
#define Set(v,x)		memset(  v , x , sizeof(v))
#define two(n)			( 1 << (n) )
#define contain(S,i)		( (S) & two(i) ) 
#define SQR(v)			( (v) * (v) )
#define ABS(x)			( ( (x) >= 0 ) ? (x) : -(x) )
#define foreach(v,it)		for( typeof((v).begin()) it = (v).begin() ; it != (v).end() ; it++ )

int x[3] , y[3] , N , r[3];

void solve() {
	double res = 0;
	cin >> N;
	for (int i = 0 ; i < N ; i++)
		cin >> x[i] >> y[i] >> r[i];
	if ( N == 1 )
		res = r[0];
	else if ( N == 2)
		res = max( r[0] , r[1]);
	else {
		double d = max( 1.0 * r[0] , 0.5 * (sqrt( SQR((x[1]-x[2])) + SQR((y[1] - y[2]))) + r[1]+r[2]));
		res = d;
		d = max( 1.0 * r[1] , 0.5* (sqrt( SQR((x[0]-x[2])) + SQR((y[0] - y[2]))) + r[0]+r[2]));
		res = min(res, d) ;
		d = max( r[2] * 1.0 , 0.5* (sqrt( SQR((x[1]-x[0])  ) + SQR( (y[1] - y[0] ) )) + r[1]+r[0]));
		res = min(res, d) ;
	}

	printf("%.6f\n", res );
}

int main() {
	int C , nc;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cout << "Case #" << nc << ": ";
		solve();
	}	
	return 0;
}
