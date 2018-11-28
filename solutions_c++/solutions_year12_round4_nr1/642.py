#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cstdio>

using namespace std;

ifstream fin( "A-large.in" );
ofstream fout( "A-large.out" );

#define int64 long long
#define pii pair< int, int >

#define cin fin
#define cout fout

int t, n, test = 1;

int64 d[20000], l[20000], r[20000];

int main() {
	for( cin >> t; t--; ) {
		cin >> n;
		for( int i = 0; i < n; i++ ) {
			cin >> d[i] >> l[i];
		}
		cin >> d[n++];
		r[0] = d[0];
		int ptr = 1;
		for( int i = 0; i < ptr; i++ ) {
			int64 ll = ptr - 1, rr = n - 1;
			while( ll < rr ) {
				int64 mid = (ll + rr + 1) / 2;
				if( d[mid] - d[i] <= r[i] )	ll = mid;
				else						rr = mid - 1;
			}
			for( int j = ptr; j <= ll; j++ ) {
				r[j] = min( l[j], d[j] - d[i] );
			}
			ptr = ll + 1;
		}
		cout << "Case #" << test++ << ": " << (ptr == n ? "YES" : "NO") << endl;
	}
	return 0;
}
