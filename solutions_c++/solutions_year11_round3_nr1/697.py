#include <map>
#include <set>
#include <list>

#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>

#include <bitset>
#include <cctype>
#include <cstdio>
#include <limits>
#include <string>
#include <vector>

#include <cassert>
#include <climits>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>

#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

void solve (void) {
	
	int N, M;
	char s[64][64];
	
	scanf ( "%d%d", &N, &M );
	for ( int i=0; i<N; ++i ) scanf ( "%s", s[i] );
	
	for ( int i=0; i<N-1; ++i )
		for ( int j=0; j<M-1; ++j ) {
			
			if ( s[i][j] == '#' && s[i][j+1] == '#' && s[i+1][j] == '#' && s[i+1][j+1] == '#' ) {
				s[i][j] = '/';
				s[i][j+1] = '\\';
				s[i+1][j+1] = '/';
				s[i+1][j] = '\\';
				}
			
			}
	
	bool key = false;
	for ( int i=0; i<N; ++i ) for ( int j=0; j<M; ++j ) key |= ( s[i][j] == '#' );
	
	if ( key ) printf ( "Impossible\n" );
	else for ( int i=0; i<N; ++i ) printf ( "%s\n", s[i] );
	
}

int main (void) {
	
	int T;
	scanf ( "%d", &T );
	for ( int t=1; t<=T; ++t ) {
		
		printf ( "Case #%d:\n", t );
		solve ();
		
		}
	
}
