#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

char robot[110];
int pos[110];

main(){
	freopen( "AL.in", "r", stdin );
	freopen( "AL.out", "w", stdout );
	
	int t, tt = 0;
	int i, left, res, o, b, n, add;
	char last;
	
	scanf ( "%d", &t );
	while( t -- ){
		scanf ( "%d", &n );
		for ( i = 0; i < n; i ++ )
			scanf ( "%s %d", robot + i, pos + i );
		left = res = 0;
		o = b = 1;
		last = 'N';
		for ( i = 0; i < n; i ++ ){
			if ( robot[i] == 'O' ){
				if ( last == robot[i] ){
					left += abs( pos[i] - o ) + 1;
					res += abs( pos[i] - o ) + 1;
				}
				else{
					add = max( 0, abs( pos[i] - o ) - left );
					res += add + 1;
					left = add + 1;
				}
				o = pos[i];
			}
			else{
				if ( last == robot[i] ){
					left += abs( pos[i] - b ) + 1;
					res += abs( pos[i] - b ) + 1;
				}
				else{
					add = max( 0, abs( pos[i] - b ) - left );
					res += add + 1;
					left = add + 1;
				}
				b = pos[i];
			}
			last = robot[i];
		}
		printf( "Case #%d: %d\n", ++ tt, res );
	}
	
	return 0;
}
