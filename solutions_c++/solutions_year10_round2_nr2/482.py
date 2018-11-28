#include <string>
#include <set>
#include <iostream>
#include <vector>

using namespace std;

int main ( ) {

	int cases;
	cin >> cases; 
	for ( int caseno = 1; caseno <= cases; caseno++) {
		int N, K, B, T;
		cin >> N >> K >> B >> T;
		vector < double > times;
		vector < double > pozs;
		vector < double > speeds;
		for ( int i =0; i < N; i++) {
			int x; cin >>x;
			pozs.push_back (x);
		}
		for ( int i =0; i < N; i++) {
			int v; cin >>v;
			speeds.push_back (v);
			times.push_back ( ((double) B - pozs[i]) / speeds[i] );
		}
		int count = 0;
		int wolne = 0;
		int dobre = 0;
		for ( int i = N-1; i >= 0; i --) {
			if ( times[i] <= T ) {
				dobre += 1;
				count += wolne;
			}
			else {
				wolne += 1;
			}

			if ( dobre >= K ) {
				break;
			}
		}
		if ( dobre >= K )
		cout << "Case #" << caseno << ": " << count << endl;
		else 
			cout << "Case #" << caseno << ": " << "IMPOSSIBLE" << endl;

	}

	return 0;

}