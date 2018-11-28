#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<long long,int> P;

int main() {
	int cases;
	vector<long long> a, b;
	vector<P> w;
	
	cin >> cases;
	for( int c = 1; c <= cases; ++c ) {
		int n;
		cin >> n;
		a.clear();
		b.clear();
		
		for( int i = 0; i < n; ++i ) {
			long long x;
			cin >> x;
			a.push_back( x );
		}
		for( int i = 0; i < n; ++i ) {
			long long x;
			cin >> x;
			b.push_back( x );
		}
		
		sort( a.begin(), a.end() );
		sort( b.begin(), b.end() );
		
		long long sum = (long long)1 << 62;
		do {
			long long tmp = 0;
			for( int i =0 ; i < n; ++i ) {
				tmp += a[i] * b[i];
			}
			sum = min( sum, tmp );
		} while( next_permutation( a.begin(), a.end() ) );
		
		cout << "Case #" << c << ": " << sum << endl;
	}
	return 0;
}
