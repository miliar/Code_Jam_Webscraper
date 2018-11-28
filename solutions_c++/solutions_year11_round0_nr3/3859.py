#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool bs( vector<int> vc, vector<int> vs )
{
	int m = 0, n = 0;
	for( int i = 0; i < vs.size(); i++ ) {
		if( vs[i]) {
			m = m ^ vc[i];
		} else {
			n = n ^ vc[i];
		}
	}
	return (m==n);
}

int ss( vector<int> vc, vector<int> vs )
{
	int m = 0;
	for( int i = 0; i < vs.size(); i++ ) {
		if( vs[i] ) {
			m = m + vc[i];
		}
	}
	return m;
}

void main2()
{
	vector <int> vc, vs;
	int t, n, k = -1;
	cin >> n;
	for( int i = 0; i < n; i++ ) {
		cin >> t;
		vc.push_back( t );
		vs.push_back( 1 );
	}
	for( int l = 0; l < n; l++ ) {
		for( int j = 0; j <= l; j++ ) {
			vs[j] = 0;
		}
		if( bs( vc,vs ) ) {
			t = ss( vc, vs );
			if( t > k ) {
				k = t;
			}		
		}
		while( next_permutation( vs.begin(), vs.end() ) ) {
			if( bs( vc,vs ) ) {
				t = ss( vc, vs );
				if( t > k ) {
					k = t;
				}
			}
		}
	}
	if( k == -1 )
		cout << "NO";
	else
		cout << k;
}
int main()
{
	int T;
	cin >> T;
	for( int i = 0; i < T; i++ ) {
		cout << "Case #"<<i+1<<": ";
		main2();
		cout << endl;
	}
	return 0;
}
