/**
 *
 */
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long LL;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }


int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int T;	cin >> T;
	for(int tc = 1; tc <= T; ++tc) {

		int R, C, D;
		cin >> R >> C >> D;
		string s;

		vvi g(R, vi(C));

		for(int i = 0; i < R; ++i) {
			cin >> s;
			for(int j = 0; j < C; ++j) {
				g[i][j] = D + s[j]-'0';
			}
		}

		vector<vector<LL> > cx, cy, cm;
		cx.resize( R, vector<LL>(C) );
		cy.resize( R, vector<LL>(C) );
		cm.resize( R, vector<LL>(C) );

		cx[0][0] = 0*g[0][0];
		cy[0][0] = 0*g[0][0];
		cm[0][0] = g[0][0];

		for(int i = 1; i < C; ++i) {
			cx[0][i] = cx[0][i-1] + (LL)i*g[0][i];
			cy[0][i] = cy[0][i-1] + (LL)0*g[0][i];
			cm[0][i] = cm[0][i-1] + g[0][i];
		}
		for(int i = 1; i < R; ++i) {
			cx[i][0] = cx[i-1][0] + (LL)0*g[i][0];
			cy[i][0] = cy[i-1][0] + (LL)i*g[i][0];
			cm[i][0] = cm[i-1][0] + g[i][0];
		}

		for(int i = 1; i < R; ++i) {
			for(int j = 1; j < C; ++j) {
				cx[i][j] = cx[i-1][j] + cx[i][j-1] - cx[i-1][j-1] + (LL)j*g[i][j];
				cy[i][j] = cy[i-1][j] + cy[i][j-1] - cy[i-1][j-1] + (LL)i*g[i][j];
				cm[i][j] = cm[i-1][j] + cm[i][j-1] - cm[i-1][j-1] + g[i][j];
			}
		}

//		for(int i = 0; i < R; ++i) {
//			for(int j = 0; j < C; ++j) {
//				cout << cx[i][j] << '\t';
//			}
//			cout << endl;
//		}

		int K = -1;
		for(int i = 2; i < R; ++i) {
			for(int j = 2; j < C; ++j) {
				for(int k = 3; k <= min(i,j)+1; ++k) {
					if( k < K ) continue;
					//cout << "try k = " << k << endl;

					LL x = cx[i][j];
					LL y = cy[i][j];
					LL m = cm[i][j];

					if( i-k >= 0 ) {
						x -= cx[i-k][j];
						y -= cy[i-k][j];
						m -= cm[i-k][j];
					}
					if( j-k >= 0 ) {
						x -= cx[i][j-k];
						y -= cy[i][j-k];
						m -= cm[i][j-k];
					}
					if( i-k >= 0 && j-k >= 0 ) {
						x += cx[i-k][j-k];
						y += cy[i-k][j-k];
						m += cm[i-k][j-k];
					}

					x -= j*g[i][j];
					x -= (j-k+1)*g[i][j-k+1];
					x -= (j-k+1)*g[i-k+1][j-k+1];
					x -= j*g[i-k+1][j];

					y -= i*g[i][j];
					y -= i*g[i][j-k+1];
					y -= (i-k+1)*g[i-k+1][j-k+1];
					y -= (i-k+1)*g[i-k+1][j];

					m -= g[i][j];
					m -= g[i][j-k+1];
					m -= g[i-k+1][j-k+1];
					m -= g[i-k+1][j];

					//cout << i << ", " << j << ", " << k << " -> " << x << ", " << y << ", " << m << endl;

					LL xx = 2*j-k+1;
					LL yy = 2*i-k+1;
					x += x;
					y += y;

					if( ((x%m) == 0) && ((y%m) == 0) && x/m == xx && y/m == yy )
						K = max(K, k);
				}
			}
		}

		if( K < 0 )
			cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << tc << ": " << K << endl;
	}


	return 0;
}
