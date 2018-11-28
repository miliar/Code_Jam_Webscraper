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
	
	int N, L, H, a[1024];	
	scanf ( "%d%d%d", &N, &L, &H );
	for ( int i=0; i<N; ++i ) scanf ( "%d", a+i );
	
	bool key = true;
	int ans = -1;
	for ( int x=L; x<=H; ++x ) {
		
		key = true;
		for ( int i=0; i<N; ++i ) if ( x % a[i] != 0 && a[i] % x != 0 ) {
			key = false;
			}
		if ( key ) { ans = x; break; }
		
		}
	
	if ( ans < 0 ) printf ( "NO\n" );
	else printf ( "%d\n", ans );
	
}

int main (void) {
	
	int T;
	scanf ( "%d", &T );
	for ( int t=1; t<=T; ++t ) {
		
		printf ( "Case #%d: ", t );
		solve ();
		
		}
	
}
