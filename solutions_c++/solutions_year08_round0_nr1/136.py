#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <map>

using namespace std;

string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}

int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}

int solveIt(vector<int> &q, int S) {
	int Q = q.size();
	if (S > Q) return 0;
	vector<vector<int> > dp(S, vector<int>(Q, 0));
	vector<int> mn(Q, 10000);
	mn[0] = 0;
	for (int i = 0; i < Q; i++) {
		dp[q[i]][i] = 10000;
		for (int j = 0; j < S; j++) if (dp[j][i] < mn[i])
			mn[i] = dp[j][i];
		for (int j = i+1; j < Q; j++) dp[q[i]][j] = mn[i]+1;
	}

	return mn[Q-1];
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		int S, Q;

		map<string, int> smap;
		S = readIntLine();
		for (int i = 0; i < S; i++) smap[readLine()] = i;

		Q = readIntLine();
		vector<int> qrs(Q);
		for (int i = 0; i < Q; i++) qrs[i] = smap[readLine()];

		int res = solveIt(qrs, S);

		printf("Case #%d: %d\n", cn, res);
	}
	return 0;
}

