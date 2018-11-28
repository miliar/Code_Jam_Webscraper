#include <iostream>
using namespace std;

int main() {
	int tn;
	cin >> tn;
	
	int C[15];
	for(int cc = 1 ; cc <= tn ; ++cc ) {
		int n;
		cin >> n;
		for(int i=0;i<n;++i) cin >> C[i];

		cout << "Case #" << cc << ": ";


		int ret = -1;
		for(int s = 0 ; s < ( 1 << n ) ; ++s) {
			int patriksum = 0;
			int seansum = 0;
			int seanbit = 0;
			for( int i = 0 ; i < n ; ++ i ) {
				if( ( s >> i ) & 1 ) {
					seansum += C[i];
					seanbit ^= C[i];
				}
				else {
					patriksum ^= C[i];
				}
			}
			if( patriksum > 0 && patriksum == seanbit ) ret = max( ret, seansum );
		}

		if( ret == -1 ) cout << "NO" << endl;
		else cout << ret << endl;
	}
}
