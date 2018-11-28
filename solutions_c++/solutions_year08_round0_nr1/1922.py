#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

const int C1 = 1005, C2 = 105;
int DP[C1][C2];
int ntest = 0;

void solve() {
	for (int i = 0; i < C1; i++) {
		for (int j = 0; j < C2; j++) {
			DP[i][j] = 100000000;
		}
	}
	
	int S, Q;
	scanf("%d ",&S);

	vector<string> engines, queries;
	for (int i = 0; i < S; i++) {
		char line[1000];
		gets(line);
		engines.push_back(line);
	}

	scanf("%d ",&Q);

	for (int j = 0; j < Q; j++) {
		DP[0][j] = 0;
	}

	for (int i = 0; i < Q; i++) {
		char line[1000];
		gets(line);
		queries.push_back(line);
	}

	
	for (int i = 0; i < Q; i++) {
		for (int j = 0; j < S; j++) {
			for (int k = 0; k < S; k++) {
				if (j != k) {
					DP[i+1][k] = min(DP[i+1][k], DP[i][j] + 1);
				}
				else if (queries[i] != engines[j]) {
					DP[i+1][k] = min(DP[i+1][k], DP[i][j]);
				}
			}
		}
	}

	/*for (int i = 0; i <= Q; i++) {
		for (int j = 0; j < S; j++) {
			cout << DP[i][j] << " ";
		}
		cout << endl;
	}*/

	int best = 1000000000;
	for (int i = 0; i <= Q; i++) {
		best = min(best, DP[Q][i]);
	}

	printf("Case #%d: %d\n", ++ntest, Q == 0 ? 0 : best);
}

int main() {
	freopen("test.in", "rt", stdin);
	freopen("test.out", "wt", stdout);
	int N; scanf("%d ",&N);
	for (int i = 0; i < N; i++)
		solve();
	
	return 0;
}