#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");
#define cin fin
#define cout fout

using namespace std;

#define int64 long long

int t, n, test = 1;
int64 arr[2000000], ptr, d;

int main() {
	for( cin >> t; t--; ) {
		cerr<< t << endl;;
		cin >> n >> d;
		ptr = 0;	
		for( int i = 0; i < n; i++ ) {
			int a, b;
			cin >> a >> b;
			for( int j = 0; j < b; j++ )
				arr[ptr++] = a;
		}
		double l = 0., r = 1e13;
		for( int i = 0; i < 100; i++ ) {
			double mid = (l + r) / 2.;
			bool good = true;
			double pos = arr[0] - mid;
			for( int j = 1; j < ptr; j++ ) {
				double npos = max( pos + d, arr[j] - mid );
				if( abs(npos - arr[j]) > mid + 1e-5 ) {
					good = false;
					break;
				}
				pos = npos;
			}
			if(good)
				r = mid;
			else
				l = mid;
		}
		cout.precision(2);
		cout.setf(ios::fixed | ios::showpoint);
		cout << "Case #" << test++ << ": " << l + 1e-5 << endl;
	}
	return 0;
}