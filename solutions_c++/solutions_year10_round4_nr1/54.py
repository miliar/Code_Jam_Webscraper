#include <iostream>
#include <vector>
using namespace std;
#define MOD 100003

int ORG[64][64];

int main( void )
{
	int C;
	cin >> C;
	for( int CC = 1; CC <= C; CC ++ ){
		int k;
		cin >> k;
		for( int i = 0, x = 0, y = 0; i < k * k; i ++ ){
			cin >> ORG[y][x];
			x ++, y --;
			while( x >= k && y >= 0 ){ x ++, y --; }
			if( y < 0 ){ y = x; x = 0; }
			while( y >= k ){ x ++, y --; }
		}

/*
		for( int y = 0; y < k; y ++ ){
			for( int x = 0; x < k; x ++ )
				cerr << ORG[y][x];
			cerr << endl;
		}
*/
		long long ret = 1000000000;
		for( int k2 = k; ; k2 ++ ){ // 51
			for( int x0 = 0; x0 <= k2-k; x0 ++ ){ // 51
				for( int y0 = 0; y0 <= k2-k; y0 ++ ){ // 51
					for( int y = 0; y < k; y ++ ){ // 51
						for( int x = 0; x < k; x ++ ){ // 51
							{
								int xx = k2-1 - (y+y0) - x0;
								int yy = k2-1 - (x+x0) - y0;
								if( 0 <= xx && xx < k && 0 <= yy && yy < k && ORG[y][x] != ORG[yy][xx] ) goto NG;
							}
							{
								int xx = (y+y0) - x0;
								int yy = (x+x0) - y0;
								if( 0 <= xx && xx < k && 0 <= yy && yy < k && ORG[y][x] != ORG[yy][xx] ) goto NG;
							}
						}
					}
					ret = (long long)k2 * k2 - (long long)k * k;
					goto OK;
					NG:;

				}
			}
		}
		OK:;
		printf( "Case #%d: %lld\n", CC, ret );
	}
	return 0;
}
