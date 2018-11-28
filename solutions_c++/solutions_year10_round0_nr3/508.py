
#include <vector>
#include <iostream>
using namespace std;

typedef long long LL;

LL solve(int next, int R, int k, int N, vector<int> _g) {
	LL res = 0;
	vector<int> g = _g;
	for (int i = 0; i < N; ++i)
		g.push_back(g[i]);
	vector<LL> sum(N, 0);
	vector<int> was(N, -1);
	was[next] = 0;
	sum[next] = 0;
	for (int i = 0; i < R; ++i) {
		int am = 0;
		int next2 = next;
		for (int j = 0; j < N; ++j) {
			if (am + g[next + j] > k)
				break;
			am += g[next + j];
			next2 = next + j + 1;
		}
		res += LL(am);
		next = next2 % N;
		if (was[next] == -1) {
			was[next] = i + 1;
			sum[next] = res;
		} else {
			int cycleLen = i + 1 - was[next];
			LL cycleSum = res - sum[next];
			return (LL(R - was[next]) / cycleLen) * cycleSum + solve(0, (R - was[next]) % cycleLen + was[next], k, N, _g);
		}
	}
	return res;
}

int main() {
	int cases;
	cin >> cases;
	for (int cas = 0; cas < cases; ++cas) {
		int R, k, N;
		cin >> R >> k >> N;
		vector<int> g(N);
		for (int i = 0; i < N; ++i)
			cin >> g[i];
		cout << "Case #" << cas + 1 << ": " << solve(0, R, k, N, g) << "\n";
	}
	return 0;
}