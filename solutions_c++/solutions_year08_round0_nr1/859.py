#include <iostream>
#include <map>
using namespace std;

#define MAXS 101
#define MAXQ 1001

map<string,int> engine;
int dp[MAXQ][MAXS];

int main() {
	int n;
	cin >> n;
	for(int t = 1; t <= n; ++t) {
		engine.clear();

		int S,Q;
		string s;
		cin >> S;
		cin.ignore();
		for(int i = 0; i < S; ++i) {
			getline(cin,s);
			engine[s] = i;
			dp[0][i] = 0;
		}

		cin >> Q;

		if(Q == 0) {
			cout << "Case #" << t << ": 0" << endl;
			continue;
		}

		cin.ignore();
		getline(cin,s);
		int p = engine[s];
		dp[0][p] = 1<<20;
		for(int i = 1; i < Q; ++i) {
			getline(cin,s);
			p = engine[s];
			dp[i][p] = 1<<20;
			for(int j = 0; j < S; ++j) {
				if(j != p) {
					dp[i][j] = dp[i-1][j];
					for(int k = 0; k < S; ++k) {
						if(j != k)
							dp[i][j] = min(dp[i][j], dp[i-1][k]+1);
					}
				}
			}
		}

		int ret = 1<<20;
		for(int i = 0; i < S; ++i)
			ret = min(ret, dp[Q-1][i]);

		cout << "Case #" << t << ": " << ret << endl;
	}
	return 0;
}
