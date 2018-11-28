#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;

int main() {
	int T;
	cin >> T;

	for (int kase = 1; kase <= T; ++kase) {
		int R, K, N;
		cin >> R >> K >> N;

		LL totalSum = 0;
		vector<int> G(N);
		for (int i = 0; i < N; ++i) {
			cin >> G[i];
			totalSum += G[i];
		}


		int cur = 0;
		vector<bool> seen(N);
		vector<int> next(N);
		vector<LL> groupSum(N);

		for (int i = 0; ; ++i) {
			if (seen[cur]) break;
			seen[cur] = true;

			int j = cur;
			LL curSum = 0;
			for ( ; curSum <= K && curSum <= totalSum; j = j + 1, j %= N)
				curSum += G[j];

			--j;
			j += N;
			j %= N;

			curSum -= G[j];

			groupSum[cur] = curSum;
			next[cur] = j;
			cur = j;
		}

		long long cycleSum = 0;
		int cycleLength = 0, c = cur, cycleStart = cur;

		while (true) {
//			cout << c << " -> ";
			cycleSum += groupSum[c];
			++cycleLength;
			c = next[c];
			if (c == cur) break;
		}
//		cout << endl;
//		cout << cycleLength << ' ' << cycleSum << endl;

		long long moneyMade = 0;
		int steps = 0;
		cur = 0;
		for (int i = 0; i < R; ++i) {
			moneyMade += groupSum[cur];
			cur = next[cur];
			++steps;

			if (cur == cycleStart)
				break;
		}

		R -= steps;
		moneyMade += (R / cycleLength) * cycleSum;
		R %= cycleLength;

		for (int i = 0; i < R; ++i) {
			moneyMade += groupSum[cur];
			cur = next[cur];
		}

		cout << "Case #" << kase << ": " << moneyMade << endl;
	}
}
