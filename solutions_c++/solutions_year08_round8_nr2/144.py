#include <iostream>
#include <set>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int T, N;

string col[1000];
int A[1000];
int B[1000];

struct Cover {
	int a, b;
};

bool operator<(Cover a, Cover b) {
	return a.a < b.a;
}

int main() {
	cin >> T;
	for (int tcs = 1; tcs <= T; tcs++) {
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> col[i] >> A[i] >> B[i];
		}
		int res = -1;
		for (int i = 0; i < (1 << N); i++) {
			set<string> s;
			vector<Cover> cov;
			for (int j = 0; j < N; j++) {
				if ((i >> j) & 1) {
					Cover c = {A[j], B[j]};
					cov.push_back(c);
					s.insert(col[j]);
				}
			}
			if (s.size() > 3) continue;
			int to = 0;
			sort(cov.begin(), cov.end());
			bool poss = true;
			for (int j = 0; j < (int) cov.size(); j++) {
				if (cov[j].a > to+1) poss = false;
				to = max(to, cov[j].b);
			}
			if (to < 10000) poss = false;
			if (poss) {
				if (res == -1 || (int) cov.size() < res) res = (int) cov.size();
			}
		}
		if (res == -1) {
			cout << "Case #" << tcs << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << tcs << ": " << res << endl;
		}
	}
	return 0;
}

