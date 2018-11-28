#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

double a[1100];
double b[1100];
int c[1100];

main(){
	freopen( "DL.in", "r", stdin );
	freopen( "DL.out", "w", stdout );
	
	int t, tt = 0;
	int i, j, k, n;
	double res;
	int cnt;
	
	a[1] = b[1] = 0;
	a[2] = 2;
	b[2] = 0.5;
	for ( i = 3; i < 1100; i ++ ){
		a[i] = b[i] = 0;
		for ( j = 1; j < i; j ++ )
			b[i] += a[j] + b[i-j] + ( a[i-j] + 1 ) / ( i - j );
		b[i] /= i;
		a[i] = ( b[i] * i * 1.0 / ( i - 1 ) ) + 1.0 / ( i - 1 );
	}
//	cout << a[2] << " " << b[3] << " " << a[3] << " " << b[4] << " " << a[4] << endl;
	scanf ( "%d", &t );
	while ( t -- ){
		scanf ( "%d", &n );
		for ( i = 0; i < n; i ++ ){
			scanf ( "%d", c + i );
			c[i] --;
		}
		res = 0;
		for ( i = 0; i < n; i ++ )
			if ( c[i] != -1 ){
				cnt = 1;
				j = c[i];
				c[i] = -1;
				while( c[j] != -1 ){
					k = c[j];
					c[j] = -1;
					j = k;
					cnt ++;
				}
				res += a[cnt];
			}
		
		printf( "Case #%d: %.10lf\n", ++ tt, res );
	}
	
	return 0;
}
