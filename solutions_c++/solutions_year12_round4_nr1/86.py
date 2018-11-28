#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Swinging Wild
char dp[10002][10002];

int doit(int cur, int hold, vector <int> &d, vector <int> &l)
{
	if (hold == d.size() - 1) {
		return 1;
	}
	if (dp[cur][hold] >= 0) {
		return dp[cur][hold];
	}
	int ret = 0;
	int len = min(d[hold] - d[cur], l[hold]);
	for (int i = hold + 1; i < d.size(); i++) {
		if (d[i] - d[hold] > len) {
			break;
		}
		ret |= doit(hold, i, d, l); 
	}
	return dp[cur][hold] = ret;
}

int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int N;
		cin >> N;
		vector <int> d(N + 2, 0);
		vector <int> l(N + 2, 0);
		for (int i = 0; i < N; i++) {
			cin >> d[i + 1] >> l[i + 1];
		}
		cin >> d[N + 1];
		memset(dp, -1, sizeof(dp));
		int ret = doit(0, 1, d, l);
		cout << "Case #" << caseno << ": " << (ret ? "YES" : "NO") << endl;
	}

	return 0;
}
