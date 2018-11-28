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

	int T; cin >> T;

	for(int tc = 1; tc <= T; ++tc) {
		int N; cin >> N;

		vector<string> data(N);
		for(int i = 0; i < N; ++i)
			cin >> data[i];

		vector<double> wp(N), owp(N), oowp(N);

		for(int i = 0; i < N; ++i) {
			int W = 0, L = 0;
			for(int j = 0; j < N; ++j) {
				if( data[i][j] == '1')
					++W;
				else if( data[i][j] == '0')
					++L;
			}
			wp[i] = (double)W/(W+L);
		}

		for(int k = 0; k < N; ++k) {
			int n = 0;
			double s = 0.0;

			for(int i = 0; i < N; ++i) {
				if( data[k][i] == '.' )
					continue;

				int W = 0, L = 0;
				for(int j = 0; j < N; ++j) {
					if( j == k )
						continue;
					if( data[i][j] == '1')
						++W;
					else if( data[i][j] == '0')
						++L;
				}
				s += (double)W/(W+L);
				n += 1;
			}

			owp[k] = s/n;
		}

		for(int k = 0; k < N; ++k) {
			int n = 0;
			double s = 0.0;

			for(int i = 0; i < N; ++i) {
				if( data[k][i] == '.' )
					continue;

				s += owp[i];
				n += 1;
			}

			oowp[k] = s/n;
		}


		cout << "Case #" << tc << ":\n";
		for(int i = 0; i < N; ++i) {
			cout << fixed << setprecision(12) << (0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]) << "\n";
		}
	}


	return 0;
}
