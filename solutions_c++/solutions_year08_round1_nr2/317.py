#include <iostream>
#include <vector>

using namespace std;

typedef pair<int,int> PI;

int main() {
	int cases;
	cin >> cases;
	vector<PI> cust[2010];
	
	for( int c = 1; c <= cases; ++c ) {
		int n, m;
		cin >> n >> m;
		for( int i = 0; i < m; ++i ) {
			int t;
			cin >> t;
			cust[i].resize( t );
			for( int j= 0; j < t; ++j ) {
				cin >> cust[i][j].first >> cust[i][j].second;
				cust[i][j].first--;
			}
		}
		
		int best = n+1;
		int best_mask = 0;
		for( int i = (1<<n)-1; i >= 0; --i ) {
			int ok = 1;
			for( int j=  0; j < m; ++j ) {
				int satis = 0;
				for( int k =0; k < (int)cust[j].size(); ++k ) {
					if( !cust[j][k].second ) {
						if( !(i & (1<<cust[j][k].first)) ) {
							satis = 1;
							break;
						}
					} else {
						if( i & (1<<cust[j][k].first) ) {
							satis = 1;
							break;
						}
					}
				}
				if( !satis ) {
					ok = 0;
					break;
				}
			}
			if( ok ) {
				int cnt = 0;
				for( int j = 0; j < n; ++j ) {
					if( i & (1<<j) ) ++cnt;
				}
				if( cnt < best ) {
					best = cnt;
					best_mask = i;
				}
			}
		}
		cout << "Case #" << c << ": ";
		if( best == n+1 ) {
			cout << "IMPOSSIBLE\n";
		} else {
			for( int i = 0; i < n; ++i ) {
				if( i > 0 ) cout << ' ';
				cout << ((best_mask & (1<<i)) ? 1 : 0);
			}
			cout << endl;
		}
	}
	return 0;
}

