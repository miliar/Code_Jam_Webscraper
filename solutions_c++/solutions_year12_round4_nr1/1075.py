#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <set>
#include <algorithm>
#include <stdio.h>
#include <string.h>
using namespace std;

int N;
int d[10010];
int l[10010];
int D;

int f(int a, int b, int x) {
	if (d[a]+x < d[b])
		return 0;
	if (d[b]-d[a]<=l[b])
		return d[b]-d[a];
	return l[b];
}

int dp[10010];

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		for (int j = 0; j < N; j++) {
			cin >> d[j] >> l[j];
		}
		cin >> D;
		memset(dp, 0, sizeof(dp));
		dp[0] = d[0];
		for (int j = 1; j < N; j++) {
			for (int k = 0; k < j; k++) {
				int y = f(k, j, dp[k]);
				dp[j] = max(dp[j], y);
			}
			//cout << dp[j] << endl;
		}
		bool ans = false;
		for (int j = 0; j < N; j++) {
			if (dp[j] > 0 && dp[j]+d[j] >= D)
				ans = true;
		}
		cout << "Case #" << i+1 << ": ";
		if (ans)
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}
}
