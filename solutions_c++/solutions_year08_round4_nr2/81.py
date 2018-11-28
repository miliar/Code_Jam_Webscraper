#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<map>
#include<algorithm>
using namespace std;

int main( void )
{
	int N;
	cin >> N;
	char *v = new char[(10000 * 10000 + 1)];
	for( int CC = 0; CC < N; CC ++ ){
		int N, M, A;
		cin >> N >> M >> A;
		bool inter = false;
		int x1 = -1, y1 = -1, x2 = -1, y2 = -1;
		int MAX = N*M+1;

		if( A > MAX ) goto not_found;

		if( N > M ){ int t = M; M = N, N = t; inter = true; }
		memset( v, 0, sizeof(char) * MAX );
		for( int y = 1; y <= M; y ++ ){
			for( int x = min(N,y); x >= 0; -- x ){
				int a = x * y;
				v[a] = true;
				if( a-A >= 0 && v[a-A] ){
					x2 = x, y1 = y;
					if( a-A == 0 ) x1 = 0, y2 = 0;
					else{
						for( int x = 1; x <= N; x ++ ){
							if( (a-A) % x == 0 && (a-A) / x <= M ){
								x1 = x, y2 = (a-A) / x;
								break;
							}
						}
					}
					goto found;
				}
				if( a+A < MAX && v[a+A] ){
					x2 = x, y1 = y;
					for( int x = 1; x <= N; x ++ ){
						if( (a+A) % x == 0 && (a+A) / x <= M ){
							x1 = x, y2 = (a+A) / x;
							break;
						}
					}
					goto found;
				}
			}
		}

	not_found:
		printf( "Case #%d: IMPOSSIBLE\n", CC + 1 );
		continue;

	found:
		if( inter )
			printf( "Case #%d: %d %d %d %d %d %d\n", CC + 1, 0, 0, y1, x1, y2, x2 );
		else
			printf( "Case #%d: %d %d %d %d %d %d\n", CC + 1, 0, 0, x1, y1, x2, y2 );
		continue;
	}
	delete v;
	return 0;
}
