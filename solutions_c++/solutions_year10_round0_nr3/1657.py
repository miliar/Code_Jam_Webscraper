#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>

#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

long long seqSum(vector<long long> predPeriod, vector<long long> period, int length) {
	long long res = 0;
	if (length <= (int)predPeriod.size()) {
		res = accumulate(predPeriod.begin(), predPeriod.begin() + length, (long long)0);
	}
	else {
		long long periodSum = accumulate(period.begin(), period.end(), (long long)0);
		length -= predPeriod.size();
		int periodTimes = length / period.size();
		int periodRest = length % period.size();
		res = accumulate(predPeriod.begin(), predPeriod.end(), (long long)0)
				+ periodSum * periodTimes
				+ accumulate(period.begin(), period.begin() + periodRest, (long long)0);
	}
	return res;
}

long long solve(int R, int k, vector<int> g) {
	int n = g.size();
	vector<int> next(n);
	vector<long long> value(n);

	int len = 0;
	long long gSum = 0;
	for (int i = 0; i < n; ++i) {
		while (len < n && gSum + g[(i + len) % n] <= k) {
			gSum += g[(i + len) % n];
			++len;
		}
		next[i] = (i + len) % n;
		value[i] = gSum;
		gSum -= g[i];
		--len;
	}

	vector<int> prevPos(n, -1);
	vector<long long> seq;
	for (int i = 0;;) {
		seq.push_back(value[i]);
		prevPos[i] = seq.size() - 1;
		i = next[i];
		if (prevPos[i] != -1) {
			return seqSum(vector<long long>(seq.begin(), seq.begin() + prevPos[i]),
				vector<long long>(seq.begin() + prevPos[i], seq.end()), R);
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		int R, k, N;
		cin >> R >> k >> N;
		vector<int> g(N);
		for (int i = 0; i < (int)g.size(); ++i) {
			cin >> g[i];
		}

		long long res = solve(R, k, g);

		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}
