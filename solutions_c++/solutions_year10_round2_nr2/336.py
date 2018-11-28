#include <iostream>
#include <vector>
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

	int TC; cin >> TC;
	for(int tc = 1; tc <= TC; ++tc) {
		cout << "Case #" << tc << ": ";

		int N, K, B, T;
		cin >> N >> K >> B >> T;

		vi X(N), V(N);
		for(int i = 0; i < N; ++i) {
			cin >> X[i];
		}
		for(int i = 0; i < N; ++i) {
			cin >> V[i];
		}


		while( K>0 && sz(X)>0 && (B-X.back()) <= T*V.back() ) {
			X.pop_back();
			V.pop_back();
			--K;
		}

		int am = 0;

		for(int i = sz(X)-1; K>0 && i>=0; --i) {

			if( (B-X[i]) > T*V[i] ) {
				X[i] = -1;
				continue;
			}

			int cnt = count(&X[i], &X[0]+sz(X), -1);
			am += cnt;
			--K;
		}


		if( K == 0 )
			cout << am << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}

	return 0;
}
