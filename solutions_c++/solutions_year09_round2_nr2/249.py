#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <deque>
#include <cstring>
#include <algorithm>
#include <cassert>
#include <cstdio>

using namespace std;

typedef long long LL;

int main() {
	int cases;
	char s[100];
	char s2[100];
	
	scanf( "%d", &cases );
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		scanf( "%s", s );
		int n = strlen( s );
		
//		printf( "read: %s\n", s );
		
		LL res;
		if( next_permutation( s, s+n ) ) {
			strcpy( s2, s );
			res = atoll( s );
		} else {
			sort( s, s+n );
			strcpy( s2+1, s );
			for( int i = 1; ; ++i ) {
				if( s2[i] != '0' ) {
					s2[0] = s2[i];
					s2[i] = '0';
					res = atoll( s2 );
					break;
				}
			}
		}
		printf( "Case #%d: %s\n", caseid, s2 );
	}
	return 0;
}

