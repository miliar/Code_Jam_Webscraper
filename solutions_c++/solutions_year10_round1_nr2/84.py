#include <cstdio>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

int dp[101][256];

int doit(int index, int value, vector <int> &seq, int D, int I, int M)
{
	if (index >= seq.size()) {
		return 0;
	}
	if (dp[index][value] >= 0) {
		return dp[index][value];
	}
	int ret = 1 << 30;
	ret = min(ret, D + doit(index + 1, value, seq, D, I, M));
	if (M == 0) {
		int diff = abs(seq[index] - value);
		ret = min(ret, diff + doit(index + 1, value, seq, D, I, M));
	} else for (int i = 0; i < 256; i++) {
		int diff = abs(seq[index] - i);
		int ins = max(0, (abs(value - i) - 1)) / M;
		ret = min(ret, diff + ins * I + doit(index + 1, i, seq, D, I, M));
	}
	return dp[index][value] = ret;
}

int MakeItSmooth(vector <int> seq, int D, int I, int M, int N)
{
	memset(&(dp[0][0]), -1, sizeof(dp));
	int ret = 1 << 30;
	for (int i = 0; i < 256; i++) {
		ret = min(ret, doit(0, i, seq, D, I, M));
	}
	return ret;
}

int main()
{
	string line;

	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int D, I, M, N;
		cin >> D >> I >> M >> N;
		vector <int> seq(N);
		for (int i = 0; i < N; i++) {
			cin >> seq[i];
		}

		int ret = MakeItSmooth(seq, D, I, M, N);

		cout << "Case #" << caseno << ": " << ret << endl;
		//cout << setiosflags(ios::fixed) << setprecision(8) << setw(10);
		//printf("Case #%d: %d\n", caseno, ret);
	}

	return 0;
}
