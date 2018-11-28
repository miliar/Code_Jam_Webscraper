#include <algorithm>
#include <iostream>
#include <climits>
#include <list>
#include <map>
#include <cmath>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

#define REP(i, n) for(int i=0; i<(int)(n); i++)
#define FOR(i, s, e) for (int i = (int)(s); i < (int)(e); i++)

int main() {
    int T;

    cin >> T;
    REP(t, T) {
	int N;
	cin >> N;

	vector<long long> d(N);
	vector<long long> len(N);
	long long D;
	REP(i, N)
	    cin >> d[i] >> len[i];
	cin >> D;

	vector<long long> dp(N);
	REP(i, N) dp[i] = -1;
	dp[0] = d[0];

	for (int i = 0; i < N; i++) {
	    if (dp[i] == -1)
		continue;

	    for (int j = i+1; j < N; j++) {
		if (d[j] - d[i] <= dp[i])
		    dp[j] = max(dp[j], min(len[j], d[j] - d[i]));
	    }
	}

	string ret = "NO";
	REP(i, N)
	    if (D-d[i] <= dp[i])
		ret = "YES";

	cout << "Case #" << t+1 << ": " << ret << endl;

    }

    return 0;
}
