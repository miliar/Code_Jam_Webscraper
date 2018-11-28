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
	
	long long L, t, N, C, a[1024], s[1024];
	memset ( s, 0 , sizeof s ); memset ( a, 0 , sizeof a );
	
	scanf ( "%lld%lld%lld%lld", &L, &t, &N, &C );
	for ( int i=0; i<C; ++i ) scanf ( "%lld", a+i );
	for ( int i=C; i<N; ++i ) a[i] = a[i-C];
	s[0] = 0;
	for ( int i=1; i<=N; ++i ) {
		s[i] = s[i-1] + ( a[i-1] << 1 );
		}
	
	if ( L == 0 ) printf ( "%lld\n", s[N] );
	
	if ( L == 1 ) {
		
		long long ans = s[N], temp, r = 0;
		for ( int i=0; i<N; ++i ) {
			
//			printf ( "i=%d\n", i );
			
			temp = s[i];
			
//			printf ( "temp = %lld\n", temp );
			
			if ( temp >= t ) temp += a[i], r = a[i];
			else if ( s[i+1] >= t ) temp += t-temp + ( ( ( a[i] << 1 ) - ( t-temp ) ) >> 1 ), r = ( ( ( a[i] << 1 ) - ( t-temp ) ) >> 1 );
			else temp += a[i] << 1, r = 0;
			
//			printf ( "temp = %lld r=%lld\n", temp, r );
			
			temp += s[N]-s[i+1];
//			printf ( "temp = %lld\n", temp );	
			
			if ( ans > temp ) ans = temp;
			
			}
		
		printf ( "%lld\n", ans );
		
		}
	
	if ( L == 2 ) {
		
		long long ans = s[N] << 1, temp, r = 0;
		for ( int i=0; i<N; ++i ) {
			
			for ( int j=i+1; j<N; ++j ) {
			
				temp = s[i];
				if ( temp >= t ) temp += a[i], r = a[i];
				else if ( s[i+1] >= t ) temp += t-temp + ( ( ( a[i] << 1 ) - ( t-temp ) ) >> 1 ), r = ( ( ( a[i] << 1 ) - ( t-temp ) ) >> 1 );
				else temp += a[i] << 1, r = 0;
				
				temp += s[j] - s[i+1];
				
				if ( temp >= t ) temp += a[j], r += a[j];
				else if ( s[j+1]-r >= t ) temp += t-temp + ( ( ( a[j] << 1 ) - ( t-temp ) ) >> 1 ), r += ( ( ( a[j] << 1 ) - ( t-temp ) ) >> 1 );
				else temp += a[j] << 1, r += 0;
				
				temp += s[N] - s[j+1];
				
				if ( ans > temp ) ans = temp;
				
				}
			
			}
		
		printf ( "%lld\n", ans );
		
		}
	
}

int main (void) {
	
	int T;
	scanf ( "%d", &T );
	for ( int t=1; t<=T; ++t ) {
		
		printf ( "Case #%d: ", t );
		solve ();
		
		}
	
}
