#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

ifstream fin( "B-large.in" );
ofstream fout( "B-large.out" );

#define cin fin
#define cout fout

int main() {
	int t;
	cin >> t;
	for( int T = 0; T < t; T++ ) {
		int n, s, p;
		int res = 0;
		cin >> n >> s >> p;
		int cnt[4] = {};
		for( int i = 0; i < n; i++ ) {
			int a;
			cin >> a;
			int can = 0;
			for( int j = p; j <= 10; j++ ) {
				for( int jj = j; jj + 2 >= j; jj-- ) {
					for( int jjj = j; jjj + 2 >= j; jjj-- ) {
						if( j + jj + jjj != a )	continue;
						if( j - min( jj, jjj ) == 2 ) {
							can |= 1;
						} else {
							can |= 2;
						}
					}
				}
			}
			if( a >= 2 && a <= 28 ) {
				cnt[can]++;
			} else if( can & 2 ) {
				res++;
			}
		}
		int sz = min( s, cnt[1] );
		s -= sz;
		res += sz + cnt[3];
		cnt[2] -=  min( max(0, s - cnt[3]), cnt[2] );
		res += cnt[2];
		cout << "Case #" << T + 1 << ": " << res << endl;
	}
	return 0;
}