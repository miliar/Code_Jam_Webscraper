#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

int main() {
	int C;
	cin >> C;
	for (int i = 0; i < C; i++) {
		int N, M;
		cin >> N >> M;
		vector<vector<pair<int,int> > > customers = vector<vector<pair<int,int> > >(M,vector<pair<int,int> >());
		for (int j = 0; j < M; j++) {
			int T;
			cin >> T;
			for (int k = 0; k < T; k++) {
				int X, Y; cin >> X >> Y;
				customers[j].push_back(make_pair(X,Y));
			}
		}
#ifdef _DSEBUG
		cout << "Case: " << i+1 << "\n";
		for (int k = 0; k < customers.size(); k++) {
			cout << "Customer: " << k+1 << "\n";
			for (int m = 0; m < customers[k].size(); m++) {
				cout << customers[k][m].first << "," << customers[k][m].second << "\n";
			}
		}
#endif
		bool stat = false;
		int config = 0;
		int best = 100000;
		for (int j = 0; j < (1 << N); j++) {
			bool okouter = true;
			//cout << "config: " << j << "\n";
			for (int k = 0; k < customers.size(); k++) {
				bool ok = false;
				for (int m = 0; m < customers[k].size(); m++) {
					int idx = customers[k][m].first-1;
					int malted = customers[k][m].second;
					if ((j & (1 << idx)) && malted) {
						ok = true;
						break;
					} else if (!(j & (1 << idx)) && !malted) {
						ok = true;
						break;
					}
				}
				if (!ok) {
					okouter = false;
					//cout << "customer " << k << " no match.\n";
					break;
				}
				//cout << "customer " << k << " match.\n";
			}
			if (okouter) {
				int cnt = 0;
				int t = j;
				stat = true;
				while (t > 0) { if (t%2 != 0) cnt++; t /= 2; }
				if (best > cnt) {
					cnt = best;
					config = j;
				}
				break;
			}
		}
		if (!stat) { cout << "Case #" << i+1 << ": IMPOSSIBLE\n"; continue; }
		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < N; j++) {
			if (config & (1 << j)) {
				cout << "1";
			} else {
				cout << "0";
			}
			if (j != N-1) cout << " ";
		}
		cout << "\n";
	}
	return 0;
}